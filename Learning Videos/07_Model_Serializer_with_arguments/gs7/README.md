# Many argument which can be apply inside 'serializers.ModelSerializer'
```
//'read_only' :- this allow only create and read but we can not update data


1) 


// name can be read and create but can not be update  but other field can be update 
   name = serializers.CharField(read_only=True)  




2)
// below 'read_only' apply on multyple attribue 
    read_only_fields = ['name','roll']
    
        
        
3)    
// this is the other way to give argument on attributes
   extra_kwargs = {'name':{'read_only':True},'roll':{'read_only':True}}

```
