import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


# // get data from database
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)
    r = requests.get(url = URL, data=json_data)
    data = r.json()
    print(data)
        
        
# get_data()
# get_data(2)







# //  create data in database
def post_data():
    data = {
        'name':'ankush',
        'roll':105,
        'city':'mp'
    }
    
    json_data = json.dumps(data)
    r = requests.post(url = URL, data=json_data)
    data = r.json()
    print(data)


# post_data()








# //  update data  of existing in  database

def update_data():
    
    # // below code for parttially updatae
    # data = {
    #     'id':3,
    #     'name':'ankush GuptaGG',
    #     'city':'Bhopal [MP]PP'
    # }
    
    # // below code for Fully updatae
    data = {
        'id':1,
        'roll':106,
        'name':'ankush GuptaGG',
        'city':'Bhopal [MP]PP'
    }
    
    json_data = json.dumps(data)
    r = requests.put(url = URL, data=json_data)
    data = r.json()
    print(data)


update_data()








# //  Delete data of existing in  database

def delete_data():
    
    data = {
        'id':2,
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data=json_data)
    data = r.json()
    print(data)


# delete_data()