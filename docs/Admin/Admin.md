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
