# Classification API Specs

## Upload Image
### Endpoint : POST /api/upload

### Request Header :
- X-API-TOKEN: Token (Mandatory)

### Request Body :
```json
{
    "waktu_upload": "TimeStamp",
    "file_path": "String",
}
```

### Response Body (Success):
```json
{
    "data": {
        "derajat_klasifikasi": "Int",
        "deskripsi": "String"
    }
}
```

### Response Body (Failed):
```json
{
    "data": "Failed to upload image"
}
```
