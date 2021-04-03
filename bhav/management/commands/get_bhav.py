from django.conf import settings
import logging
from django.core.management.base import BaseCommand
import kronos
from datetime import datetime, timedelta
import requests
import csv, zipfile, os
from io import TextIOWrapper
import pandas as pd

import redis

redis_client = redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0
)

logging.basicConfig(level = logging.INFO, filename = 'get_bhav.log')

class Bhav():

    def modify_url(self, url, date):
        
        url = url.replace('-##day##-', date[0])
        url = url.replace('-##month##-', date[1])
        url = url.replace('-##year##-', date[2])
        
        return url

    def unzip(self, source):

        logging.info("Unzipping %s" % (source))

        with zipfile.ZipFile(source, "r") as zip_ref:
            for file in zip_ref.namelist():

                logging.info("Extracting %s from zip" % file)
                data = []
                with zip_ref.open(file) as myfile:
                    reader = csv.reader(TextIOWrapper(myfile, 'utf-8'))
                    for row in reader:
                        data.append(row)
                return data

    def get_bhav(self):
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
        }
        
        date = datetime.today().strftime("%d-%m-%y").split('-')
        
        url = self.modify_url(settings.BHAV_URL, date)
        
        response = requests.get(url, headers = headers, timeout = 5)
        
        response.raise_for_status()
            
        target_zip = 'zerodha.zip'
        
        with open(target_zip, "wb") as file:
            
            file.write(response.content)
            file.close()
            
            data = self.unzip(target_zip)

        bhav_df = pd.DataFrame(data)
        bhav_df.columns = bhav_df.iloc[0]
        
        bhav_df = bhav_df[1:] 

        bhav_df['DAY'] = date[0]
        bhav_df['MONTH'] = date[1]
        bhav_df['YEAR'] = date[2]
        
        
        return(bhav_df[[
            'SC_CODE', 
            'SC_NAME', 
            'OPEN', 
            'HIGH', 
            'LOW', 
            'CLOSE', 
            'DAY', 
            'MONTH', 
            'YEAR'
        ]])

@kronos.register('* 6 * * *')
class Command(BaseCommand):

    def handle(self, *args, **options):

        logging.info("Calling get_bhav function : "+ str(datetime.now()))

        bhav = Bhav()

        try:
            bhav_df = bhav.get_bhav()
            logging.info(bhav_df)
            
            for index, data in bhav_df.iterrows():
            
                key = ':'.join(['SC' ,data['SC_NAME'], data['DAY'], data['MONTH'], data['YEAR']])

                for col in bhav_df.columns:
                    if col in ['SC_CODE', 'OPEN', 'HIGH', 'LOW', 'CLOSE']:   

                        redis_client.hset(key, col, data[col])

            redis_client.bgsave()
            logging.info('Snapshot created')
            
        except: 
            logging.info('No data for the day')