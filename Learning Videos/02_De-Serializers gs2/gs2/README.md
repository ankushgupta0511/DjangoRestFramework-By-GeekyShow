
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





### 3) De-Serialization
```
// it convert json data into complex data  ( otherwords reverse concept of serialization)

// important concept and  this is De-serialization 

 Json Data           ----------------->     python Native dataType     --------------------->       complex DataType
                        Parse Data                                        De-Serialization
```

### 4) BytesIO()
```
// Defination :-

A Stream implemention using in-memory bytes buffer. It inherites  BufferedBase. The buffer is discared when the close() methd is called.

//  syntext
import io
stream = io.Bytes(json_data)
```


### 5) JSONParser()
```
// this is used to parse to json data to python native data type. 

// syntext
from rest_framework.parsers import JSONParser
parsed_data = JSONParser().parse(stream)
```


### 6) De-Serialization process
```
// Creating Serializer Object
serializer = StudentSerializer(data = parsed_data)

// check validated data
serializer.is_valid()

// if data valid then you get data
serializer.validated_data

// if not valid data then it show errors
serializer.errors


// this use to create data in footer of serializer.py

def create(self, validate_data):
    return Student.objects.create(**validate_data)


```





# serializer type  1) regular serializers 2) Model serializer
```

// regular serializers
this is not genrate automatic id

// Model serializers
this is  genrate automatic id  

```
