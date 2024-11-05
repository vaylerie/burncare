# History Admin API Specs

## History
### Endpoint : GET /api/admin/history

### Request Header :
- X-API-TOKEN: Token (Mandatory)

### Response Body (Success) :
```json
{
    "data": {
        "waktu_upload": "TimeStamp",
        "file_path": "String",
        "derajat_klasifikasi": "Int",
        "confidence_score": "Float",
        "deskripsi": "String"
    }
}
```