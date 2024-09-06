
### 1)  python json
```
// it use to convert python objects into json string.
// Example :-

import json
python_data = {'name':'sonam','roll':101}
json_data = json.dumps(python_data)
print(json_data)


// output is :-
{"name":"sonam","roll":101}

```


### 2) loads() method
 
 ```
// loads(data) :-this is used to parse json string. ( in otherwords it use to convert json to python objects )

import json
json_data = {"name":"sonam","roll":101}
parsed_data = json.loads(json_data)

// output is :-
{'name':'sonam','roll':101}

 ```




### 3) NOTE :-Important
```
// each row in table is called 'model objects'
// 'model objects' and 'complex DataType' and 'model instace' all are same
```


 ### 4) Serializers

```
// Defination

 In Django REST Framework, serializers are responsible for converting complexdata such as querysets and model instances to native python datatypes(called serialization) that can then be easily rendered into JSON, XML or other content types which is understandable by Front End.


 // important concept and  this is serialization 

 complex DataType   ----------------->     python Native dataType    --------------------->      Json Data
                      serialization                                      render into json


// step to convert simple model instance into serialization

// step 1 :- Creating simple model instance stu
  stu = Student.objects.get(id=1)

// step 2 :- Converting model instance stu to Python Dict/Serializing Object
serializer = StudentSerializer(stu)




// step to convert queryset into serialization

// step 1 :- Creating queryset  instance stu
  stu = Student.objects.all()

// step 2 :- Converting queryset stu to Python Dict/Serializing Object
serializer = StudentSerializer(stu,many=True)




//  'serializer.data' this is the serialized data.


// NOTE :- in 'serializers.py' file we have to declare ID columns bcz it not genrate automatically
```





