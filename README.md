TwitApp
=======
# Development environment

### Required software
1. Python 2.7
2. Django
3. Pip (https://github.com/simpleservices/app_report-python/wiki/How-to-install-pip-on-Windows)

### Required applications
1. Python Social Auth: https://github.com/omab/python-social-auth (Install with pip: pip install python-social-auth)

### Settings
1. **DATABASES.default.NAME** has to be change to point absoulte sqlite db file in your system. If you want to use another DB, you also have to set other DATABASE settings.
2. **DEBUG** property in **settings.py** is set to **True** in development mode. Please note, that it disables catching exceptions by Social Auth app and rendering views after unseccessful log in.