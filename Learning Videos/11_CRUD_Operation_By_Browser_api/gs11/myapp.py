import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


# // get data from database
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    
    
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url = URL,headers=headers ,data=json_data)
    data = r.json()
    print(data)
        
        
get_data()
# get_data(2)








# //  create data in database
def post_data():
    data = {
        'name':'rrankush',
        'roll':16,
        'city':'mp'
    }
    
    headers = {'content-Type':'application/json'}
    
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers , data=json_data)
    data = r.json()
    print(data)


# post_data()








# //  update data  of existing in  database

def update_data():
    
    # // below code for parttially updatae
    data = {
        'id':3,
        'name':'ankush GuptaGGA',
        'city':'Bhopal [MP]PPA'
    }
    
    # // below code for Fully updatae
    # data = {
    #     'id':4,
    #     'roll':111,
    #     'name':'gupta2',
    #     'city':'gkp2'
    # }
    
    json_data = json.dumps(data)
    
    headers = {'content-Type':'application/json'}
    
    r = requests.put(url = URL,headers=headers, data=json_data)
    data = r.json()
    print(data)


# update_data()








# //  Delete data of existing in  database

def delete_data():
    
    data = {
        'id':4
    }
    json_data = json.dumps(data)

    headers = {'content-Type':'application/json'}

    r = requests.delete(url = URL,headers=headers,data=json_data)
    data = r.json()
    print(data)


# delete_data()