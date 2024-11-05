# Admin API Specs

## Admin Login
### Endpoint : POST /api/admin/login

### Request Body :

```json
{
    "username": "admin",
    "password": "admin123"
}
```

### Response Body (Success) 
```json
{
    "data": {
        "nama": "Admin",
        "role": "Admin",
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

## Edit Admin
### Endpoint : PUT /api/admin/edit

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
    "data": "Updated Successfully"
}
```

### Response Body (Failed) :
```json
{
    "data": "Failed to Update"
}
```

## Logout Admin
### Endpoint : DELETE /api/admin/logout

### Request Header : 
- X-API-TOKEN: Token (Mandatory)

### Response Body :
```json
{
  "data": "Logout Successfully"
}
```