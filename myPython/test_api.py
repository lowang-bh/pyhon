#!/usr/local/env python
# -*- coding:UTF-8 -*-

import requests, json


"""
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'X-CSRFToken: NhXYZrvg80gWbLuRWY5AfTDoFimUvRJs' -d '{ \ 
 "sn": "testAPI", \ 
 "device_type":"MySQL", \ 
 "machine_type":"虚拟机", \ 
 "cpu_cores":4, \ 
 "memory_size":4, \ 
 "disk_size":20, \ 
 "disk_num":1, \ 
 "hostname":"test" \ 
 }' 'http://127.0.0.1:8000/cmdb/hosts/'
"""
"""
User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Mobile Safari/537.36
"""

DATA= {
        "sn": "UUID112",
        "device_type":"MySQL",
        "machine_type":"虚拟机",
        "cpu_cores":4,
        "memory_size":4,
        "disk_size":20,
        "disk_num":1,
        "hostname":"create by SESSION api:2"
        }
login_data = {
        'username':"wang",
        'password':"wang"
        }

header = {'X-CSRFToken': 'FPgdqniZ3NlHCn4nX6o6WZDIRJH1Vqwj',
          'Content-Type': 'application/json',
          'Accept': 'application/json'}

URL='http://127.0.0.1:8000/cmdb/hosts/'
LOGURL="http://127.0.0.1:8000/user/logincheck"

def create_host_record(url, data=None):
    session = requests.Session()
    session.post(LOGURL, data=login_data)
    login_res = session.post(LOGURL, data=login_data)
    print login_res.status_code
    print login_res.content
    content = json.loads(login_res.content)
    print type(content), content
    print 'status' in  content
    print type(content['status']), content['status']
    print content['message']
    if content['status'] == 1:
        print "login with %s success " %login_data['username']
    else:
        print "login failed, exiting"
        exit(1)

    response = session.post(URL, data=DATA)
    print response.status_code, response.status_code == requests.codes.ok
    # print response.headers
    print response.content
    res_content= json.loads(response.content)
    print res_content['msg']
    print res_content['data']
    print response.url

if __name__ == "__main__":
    create_host_record(url=URL, data=DATA)
