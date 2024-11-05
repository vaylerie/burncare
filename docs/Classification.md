# Classification API Specs

## Upload Image
### Endpoint : POST /api/upload

### Request Header :
- X-API-TOKEN: Token (Mandatory)

### Request Body :
```json
{
    image: img_file
}
```

### Response Body (Success):
```json
{
    "data": {
        "derajat_klasifikasi": "Int",
        "confidence_score" : "Float",
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
