### Validation  type  --> 1) Field Level, 2) Object Level, 3)  Validators




## Field Level Validation
```
// apply  validation on  single  attribute 
// example this put in serializers.py
 def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError('Seat Full!!')
        return value
    
```




## object Level Validation
```
// apply  validation on  multyple  attribute 
// example this put in serializers.py
    
def validate(self, data):
    nm =data.get('name')
    ct =data.get('city')

    if nm.lower() == 'ankush' and ct.lower() != 'bhopal':
        raise serializers.ValidationError('City must be Ranchi')
    return data
    
```


##  validator Validation
```
// defind validator at top

def start_with_r(value):
    if value[0].lower() !=  'r':
        raise serializers.ValidationError('Name shoud be start with R')


// 'validators=[start_with_r]'  give as a argument on atrribute value
// then name should be start with r otherwise not create student object

    name = serializers.CharField(max_length=100,validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


```




# serializer type  1) regular serializers 2) Model serializer
```

// regular serializers
this is not genrate automatic id

// Model serializers
this is  genrate automatic id  

```
