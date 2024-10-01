# user can have some privileges like
```
a) Staff status  :- this can access json api but admin panel can not be access
b) Superuser status :- can access both
```


# Authentication in DRF
```
1) Basic Authentication
2) Session Authentication
3) Remote Authentication
4) Custom Authentication
```


# Basic Authentication
```
// it use only Basic authentication like Singnup page and Login page
// it is genrally use only for testing

// Note :- successfully authenticated provides credentials like
1) request.urser will be a Django Instance
2) request.auth will be None
```

# Permission Classess
```
1) AllowAny
2) IsAuthenticated
3) IsAdminUser
4) IsAuthenticatedOrReadOnly
5) DjangoModePermissions
6) DjangoModePermissionsOrAnonReadOnly
6) Custom Permissioin
```


# IsAuthenticated
```
// only admin user can access json api and admin user can change api  but other  local user can only read and can not perform operation with json api
```



# below authentication for locally for this f() put in views.py f() 
    
```
 //   # this line you have to write always for using authentication
    authentication_classes = [BasicAuthentication]

 //  # IsAuthenticated means only admin user opeation perform karenga and No one can perform operation on api 
    permission_classes = [IsAuthenticated]

```


# authentication for globaly we have to write in setting.py 
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.BasicAuthentication']
}

```
