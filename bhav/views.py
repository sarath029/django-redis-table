from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from datetime import datetime, timedelta
import json
import redis
import logging
import time

logging.basicConfig(level = logging.INFO, filename = 'list_bhav.log')


redis_client = redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0
)

class BhavListView(APIView):

    def list_data(self, name):
        
        data = []
        
        name = "".join(["SC:", name, "*"])
        
        for key in redis_client.scan_iter(name):
            row_data = {}

            row = redis_client.hgetall(key)
            
            for row_key in row:

                row_data[row_key.decode("utf-8")] = row[row_key].decode("utf-8")

            key_fields = key.decode("utf-8").split(':')
            
            row_data['SC_NAME'] = key_fields[1]
            row_data['DAY'] = key_fields[2]
            row_data['MONTH'] = key_fields[3]
            row_data['YEAR'] = key_fields[4]

            data.append(row_data)
            
        return(data)


    def post(self, request):
        
        name = request.data.get('name')

        start_time = time.time()
        logging.info("New Request :" + json.dumps(request.data))

        if name:
            data = self.list_data(name)
        else:
            data = self.list_data("")

        logging.info("Response Time: " + str(time.time() - start_time))

        return Response(data)