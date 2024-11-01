# History API Specs

## History
### Endpoint : GET /api/history

### Request Header :
- X-API-TOKEN: Token (Mandatory)

### Request Body :
```json
{
    "username": "Jonathan Alz"
}
```

### Response Body (Success) :
```json
{
    "data": {
        "waktu_upload": "TimeStamp",
        "file_path": "String",
        "derajat_klasifikasi": "Int",
        "deskripsi": "String"
    }
}
```