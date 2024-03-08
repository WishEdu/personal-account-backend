# Documentation v1

### **Domain** - `wish.ginda.info`

### Registration
 * Route  -  `/account/registration`
 * Method - `POST`
 * Headers - `browser: ${browserName} ${browserVersion} `

**json:**
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
**Response:**
```py
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
    "token": str,  # 64 Authorization hash
}
```

### Login
 * Route  -  `/account/login`
 * Method - `POST`
 * Headers - `browser: ${browserName} ${browserVersion} `

**json:**
```py
body = {
    "password": str,  
    # Email | Login
    "login": Optional[str], 
    "email": Optional[str],  
}
```
**Response:**
```py
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
    "token": str,  # 64 Authorization hash
}
```

### Profile
 * Route  -  `/account/me`
 * Method - `GET`
 * Headers - `Authorization: ${token}`

**Response:**
```py
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

