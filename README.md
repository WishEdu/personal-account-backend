
# Personal Account backend

## Documentation `API v1` 

### **Domain** - `wish.ginda.info`

### Registration
**Request**
 * Endpoint  -  `/account/registration`
 * Method - `POST`
 * Headers - `browser: {browserName} {browserVersion} `

**Response**
```py
body = {
    "login": str,  # [a-z0-9_]{4,32} 
    "password": str,  # ((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,20})
    "email": str,  # ^(.+)@(.+)\.(.+)$
    "first_name": str,  # [А-Я]{1}[а-я ]{1,255} 
    "last_name": str,  # [А-Я]{1}[а-я ]{1,255} 
    "patronymic": str,  # [А-Я]{1}[а-я ]{1,255} 
    "birthday": str  # (19|20)\d\d-((0[1-9]|1[012])-(0[1-9]|[12]\d)|(0[13-9]|1[012])-30|(0[13578]|1[02])-31)
}
```
**Response**
```json
{
    "id": int,
    "login": str,
    "email": str,
    "first_name": str,
    "last_name": str,
    "created_at": str,  # 2024-03-09 01:01:30.572922
    "background_color": str,  # #005CC9
    "patronymic": Optional[str],  # Иванович | null
    "birthday": Optional[str],  # 2004-04-14 | null
    "token": str,  # 64 Authorization hash
}
```

### Login
**Request**
 * Endpoint-  `/account/login`
 * Method - `POST`
 * Headers - `browser: browserName browserVersion `

**Request**
```json
{
    "password": str,  
    # Must email or login
    "login": Optional[str], 
    "email": Optional[str],  
}
```
**Response**
```json
{
    "id": int,
    "login": str,
    "email": str,
    "first_name": str,
    "last_name": str,
    "created_at": str,  # 2024-03-09 01:01:30.572922
    "background_color": str,  # #005CC9
    "patronymic": Optional[str],  # Иванович | null
    "birthday": Optional[str],  # 2004-04-14 | null
    "token": str,  # 64 Authorization hash
}
```

### Profile
 * Endpoint -  `/account/me`
 * Method - `GET`
 * Headers - `Authorization: token`

**Response**
```json
response = {
    "id": int,
    "login": str,
    "email": str,
    "first_name": str,
    "last_name": str,
    "created_at": str,  # 2024-03-09 01:01:30.572922
    "background_color": str,  # #005CC9
    "patronymic": Optional[str],  # Иванович | null
    "birthday": Optional[str],  # 2004-04-14 | null
    "groups": [
        {
            "id": int,
            "name": str
        }
    ],
    "roles": [
        {
            "id": int,
            "name": str
        }
    ],
    "permissions": [str]
}
```

