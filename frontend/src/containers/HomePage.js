import React, { useEffect, useState } from 'react'
import axios from 'axios'
import BhavTable from './BhavTable'
import { CSVLink, CSVDownload } from "react-csv";
import {
    Navbar,
    Nav,
    Form,
    FormControl,
    Button,
    Table
} from 'react-bootstrap'

const HomePage = () => {

    const [data, setData] = useState([])
    const [name, setName] = useState('')

    useEffect(() => {

        console.log(name);

        const url = '/bhav'
        const data = {
            'name': name
        }

        axios.post(url, data)
            .then((response) => {
                console.log(response.data)
                setData(response.data)
            });

    }, [name])

    return (
        <div>
            <Navbar bg="light" variant="light">
                <Navbar.Brand href="#home">Zerodha Bhav</Navbar.Brand>
                <Nav className="mr-auto">
                    <CSVLink
                        data={data}
                        filename={"bhav" + name + ".csv"}
                    >Download as CSV</CSVLink>
                </Nav>
                <Form inline>
                    <FormControl
                        type="text"
                        placeholder="Search by Name"
                        className="mr-sm-2"
                        onChange={(e) => { setName(e.target.value) }}
                    />
                </Form>
            </Navbar>
            <div style={{ "margin": "4%" }}>
                <BhavTable
                    data={data}
                ></BhavTable>
            </div>

        </div>

    )
}

export default HomePage;