TwitApp
=======
# Development environment

### Required software
1. Python 2.7
2. Django

### Required applications
1. Python Social Auth: https://github.com/omab/python-social-auth
 Install with pip: pip install python-social-auth

### Settings
1. **DATABASES.default.NAME** has to be change to point absoulte sqlite db file in your system. If you want to use another DB, you also have to set other DATABASE settings.
2. **DEBUG** property in **settings.py** is set to **False** by default. This is because of the way Python Social Auth handles unsuccessful authentication. It is handled by middleware exceptions catching. You cab change **DEBUG** to **True** and it will just raise an error after unsuccessful login.
