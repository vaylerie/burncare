# User API Specs

## Register User 
### Endpoint : POST /api/users

### Request Body :
```json
{
    "username": "Jonathan Alz",
    "nama": "Jonathan Kamagi",
    "role": "General",
    "password": "rahasia",
    "token": "ajsepfqwuiewqdklxa"
}
```

### Response Body (Success)
```json
{
   "data": "User created successfully"
}
```

### Response Body (Failed)
```json
{
   "data": "Registered Failed"
}
```

## User Login
### Endpoint : POST /api/auth/login

### Request Body :

```json
{
    "username": "Jonathan Alz",
    "password": "rahasia"
}
```

### Response Body (Success) 
```json
{
    "data": {
        "nama": "Jonathan Kamagi",
        "role": "General",
        "token": "ajsepfqwuiewqdklxa"
    }
}
```

### Response Body (Failed)
```json
{
    "data": "Login Failed"
}
```

## Edit User
### Endpoint : PUT /api/auth/edit

### Request Header :
- X-API-TOKEN: Token (Mandatory)

### Request Body :
```json
{
    "username": "String",
    "nama": "String",
    "password": "String"
}
```

### Response Body (Success) :
```json
{
    "data": "User Updated Successfully"
}
```

### Response Body (Failed) :
```json
{
    "data": "Failed to Update User"
}
```

## Logout User 
### Endpoint : DELETE /api/auth/logout

### Request Header : 
- X-API-TOKEN: Token (Mandatory)

### Response Body :
```json
{
  "data": "Logout Successfully"
}
```