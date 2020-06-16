Urls
http://127.0.0.1:8000/admin/	#admin saction
http://127.0.0.1:8000/api/	# all data
http://127.0.0.1:8000/temp/	#filter by date and temperature greater than 100 F
http://127.0.0.1:8000/dates/    # filter by date 

1. Using GET request and url http://127.0.0.1:8000/api/
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "pub_date": "2020-06-16",
        "temp_reading": 102,
        "Employee_id": {
            "id": 1,
            "first_name": "Kalpesh",
            "last_name": "Jaiswal",
            "email": "kalpesh@gmail.com",
            "address": "Jaipur"
        },
        "Device_id": {
            "id": 1,
            "device_name": "Keysight_tech"
        }
    },
    {
        "id": 2,
        "pub_date": "2020-06-16",
        "temp_reading": 96,
        "Employee_id": {
            "id": 2,
            "first_name": "shivam",
            "last_name": "tomar",
            "email": "tomar@gmail.com",
            "address": "Gwalior"
        },
        "Device_id": {
            "id": 2,
            "device_name": "IR_based"
        }
    },
    {
        "id": 3,
        "pub_date": "2020-06-16",
        "temp_reading": 92,
        "Employee_id": {
            "id": 3,
            "first_name": "gulati",
            "last_name": "singh",
            "email": "gulati@gmail.com",
            "address": "Delhi"
        },
        "Device_id": {
            "id": 1,
            "device_name": "Keysight_tech"
        }
    }
]

2.Using GET request and url http://127.0.0.1:8000/temp/   i.e the list in which temperature is greater than 100 F & current date
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "pub_date": "2020-06-16",
        "temp_reading": 102,
        "Employee_id": {
            "id": 1,
            "first_name": "Kalpesh",
            "last_name": "Jaiswal",
            "email": "kalpesh@gmail.com",
            "address": "Jaipur"
        },
        "Device_id": {
            "id": 1,
            "device_name": "Keysight_tech"
        }
    }
]



3. Using GET request and url http://127.0.0.1:8000/date/     i.e the list of current date 
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "pub_date": "2020-06-16",
        "temp_reading": 102,
        "Employee_id": {
            "id": 1,
            "first_name": "Kalpesh",
            "last_name": "Jaiswal",
            "email": "kalpesh@gmail.com",
            "address": "Jaipur"
        },
        "Device_id": {
            "id": 1,
            "device_name": "Keysight_tech"
        }
    },
    {
        "id": 2,
        "pub_date": "2020-06-16",
        "temp_reading": 96,
        "Employee_id": {
            "id": 2,
            "first_name": "shivam",
            "last_name": "tomar",
            "email": "tomar@gmail.com",
            "address": "Gwalior"
        },
        "Device_id": {
            "id": 2,
            "device_name": "IR_based"
        }
    },
    {
        "id": 3,
        "pub_date": "2020-06-16",
        "temp_reading": 92,
        "Employee_id": {
            "id": 3,
            "first_name": "gulati",
            "last_name": "singh",
            "email": "gulati@gmail.com",
            "address": "Delhi"
        },
        "Device_id": {
            "id": 1,
            "device_name": "Keysight_tech"
        }
    }
]