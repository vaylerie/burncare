# User Data API Specs

## Data
### Endpoint : GET /api/admin/userdata

### Request Header :
- X-API-TOKEN: Token (Mandatory)

### Response Body (Success) :
```json
{
    "data": {
        "username": "String",
        "nama": "String"
    }
}
```