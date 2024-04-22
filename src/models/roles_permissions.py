class Roles:
    permissions = {
        "admin": ["create", "read", "update", "delete"],
        "user": ["read", "update"],
        "guest": ["read"]
    }
