# Personal Account backend

### **Dev domain** - `wish.ginda.info`

## Documentation `API v1`

### Registration

**Request**

* Endpoint -  `/account/registration`
* Method - `POST`
* Headers - `browser: {browserName} {browserVersion} `

**Request:**

```py
{
    "login": str,  # [a-z0-9_]{4,32} 
    "password": str,  # ((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20})
    "email": str,  # ^(.+)@(.+)\.(.+)$
    "first_name": str,  # [А-Я]{1}[а-я ]{1,255} 
    "last_name": str,  # [А-Я]{1}[а-я ]{1,255} 
    "patronymic": Optional[str],  # [А-Я]{1}[а-я ]{1,255} 
}
```

**Response:** `Code 200`

```py
{
    "id": int,
    "login": str,
    "email":  str,
    "first_name":  str,
    "last_name":  str,
    "created_at": str,  # 2024-03-07 23:32:53.818302
    "description": str,
    "background_color": str,  # #005CC9
    "birthday": str,  # "2005-04-07" | ""
    "patronymic": str, # | ""
    "avatar": str,  # Url for static
    "groups": [],
    "roles": [],
    "permissions": [], # Permissions name
    "token": str
}
```

**Errors:**

`Code 400` - User form input error

`Code 403` - Request data is incorrect

`Code 500` - Server error
```py
{
    "errorMessage": str
}
```

### Login

**Request**

* Endpoint-  `/account/login`
* Method - `POST`
* Headers - `browser: browserName browserVersion `

**Request**

```py
{
    "password": str,
    # Must email or login
    "login": Optional[str],
    "email": Optional[str]
}
```

**Response**

```py
{
    "id": int,
    "login": str,
    "email":  str,
    "first_name":  str,
    "last_name":  str,
    "created_at": str,  # 2024-03-07 23:32:53.818302
    "description": str,
    "background_color": str,  # #005CC9
    "birthday": str,  # "2005-04-07" | ""
    "patronymic": str, # | ""
    "avatar": str,  # Url for static
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
    "permissions": [str], # Permissions name
    "token": str
}
```
**Errors:**

`Code 400` - User form input error

`Code 403` - Request data is incorrect

`Code 500` - Server error
```py
{
    "errorMessage": str
}
```

### Check login available

* Endpoint -  `/account/login/check`
* Method - `GET`

**Request params:**
```
login=str
```

**Response**
```py
{
    'message': str, 
    'is_login_available': bool
}
```
### Profile

* Endpoint -  `/account/me`
* Method - `GET`
* Headers - `Authorization: token`

**Response**

```py
{
    "id": int,
    "login": str,
    "email":  str,
    "first_name":  str,
    "last_name":  str,
    "created_at": str,  # 2024-03-07 23:32:53.818302
    "description": str,
    "background_color": str,  # #005CC9
    "birthday": str,  # "2005-04-07" | ""
    "patronymic": str, # | ""
    "avatar": str,  # Url for static
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
    "permissions": [str], # Permissions name
    "token": str
}
```

