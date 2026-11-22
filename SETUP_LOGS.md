## Setup

### Init & start the virtual environment

```bash
make init_venv
source ./bin/activate
```

### Install Django in the VM

```python
(django-training) django-training % pip3 install django
Collecting django
  Downloading django-6.1.3-py3-none-any.whl.metadata (3.9 kB)
Collecting asgiref>=3.9.1 (from django)
  Downloading asgiref-3.13.0-py3-none-any.whl.metadata (12 kB)
Collecting sqlparse>=0.5.0 (from django)
  Downloading sqlparse-0.6.1-py3-none-any.whl.metadata (6.9 kB)
Downloading django-6.1.3-py3-none-any.whl (8.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.4/8.4 MB 3.2 MB/s  0:00:02
Downloading asgiref-3.13.0-py3-none-any.whl (27 kB)
Downloading sqlparse-0.6.1-py3-none-any.whl (51 kB)
Installing collected packages: sqlparse, asgiref, django
Successfully installed asgiref-3.13.0 django-6.1.3 sqlparse-0.6.1

[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
(django-training) django-training % 
```

### Confirm what libraries are installed

```python
(django-training) django-training % pip3 freeze
asgiref==3.13.0
Django==6.1.3
sqlparse==0.6.1
(django-training) django-training % 
```

## Compose a base project

### `startproject`

Run `django-admin startproject {Project Name}`

```python
(django-training) django-training % django-admin startproject djangotrainingproject 
(django-training) django-training % 
```

```bash
(django-training) django-training % ls -la
total 40
drwxr-xr-x@ 12 su3-hokkaido  staff   384 Nov 22 12:11 .
drwxr-xr-x  16 su3-hokkaido  staff   512 Nov 11 17:26 ..
drwxr-xr-x@ 14 su3-hokkaido  staff   448 Oct 15 14:45 .git
-rw-r--r--@  1 su3-hokkaido  staff    69 Nov 22 12:03 .gitignore
-rw-r--r--@  1 su3-hokkaido  staff   681 Oct 15 14:44 Makefile
-rw-r--r--@  1 su3-hokkaido  staff  1842 Nov 22 12:11 README.md
drwxr-xr-x@ 14 su3-hokkaido  staff   448 Nov 22 12:06 bin
drwxr-xr-x@  4 su3-hokkaido  staff   128 Nov 22 12:09 djangotrainingproject # New directory
drwxr-xr-x@  2 su3-hokkaido  staff    64 Oct 15 13:55 include
drwxr-xr-x@  3 su3-hokkaido  staff    96 Oct 15 13:55 lib
-rw-r--r--@  1 su3-hokkaido  staff   384 Nov 22 12:03 pyvenv.cfg
-rw-r--r--@  1 su3-hokkaido  staff   236 Oct 15 14:24 pyvenv.cfg.sample
(django-training) django-training % 
```

```bash
(django-training) djangotrainingproject % ls -la
total 8
drwxr-xr-x@  4 su3-hokkaido  staff  128 Nov 22 12:09 .
drwxr-xr-x@ 12 su3-hokkaido  staff  384 Nov 22 12:11 ..
drwxr-xr-x@  7 su3-hokkaido  staff  224 Nov 22 12:09 djangotrainingproject
-rwxr-xr-x@  1 su3-hokkaido  staff  677 Nov 22 12:09 manage.py
(django-training) djangotrainingproject % 
```

### `startapp`

```python
(django-training) djangotrainingproject % python3 manage.py startapp djangotrainingapp    
(django-training) djangotrainingproject % 
```

### `runserver` (Run a local server)

```python
(django-training) djangotrainingproject % python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 22, 2026 - 03:17:25
Django version 6.1.3, using settings 'djangotrainingproject.settings'
Starting WSGI development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.1/howto/deployment/
```

## Initial configurations

Modify `djangotrainingproject/settings.py`

```python
INSTALLED_APPS = [
    ...
    'djangotrainingapp', # Added by @su3-hokkaido on Nov 22nd 2026
    ...
]
```

## Setup DB

### Create a model

`app/models.py`

```python
from django.db import models
from django.contrib.auth.models import User # Default user model

# A Model
class Task(models.Model):
  # Items
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # CASCADE: 親が消されたら子も消える
  title = models.CharField(max_length=255)
  description = models.TextField(null=True, blank=True)
  completed = models.BooleanField(default=False)
  createdDate = models.DateTimeField(auto_now_add=True)

  # Return value
  def __str__(self):
    return self.title

  # Sort Key
  class Meta:
    ordering = ["completed"]
```

### Migration

```python
(django-training) django-training % cd ./djangotrainingproject 
(django-training) djangotrainingproject % python3 manage.py makemigrations
Migrations for 'djangotrainingapp':
  djangotrainingapp/migrations/0001_initial.py
    + Create model Task
(django-training) djangotrainingproject % 
```

```python
(django-training) django-training % make migrate
cd ./djangotrainingproject && python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, djangotrainingapp, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying djangotrainingapp.0001_initial... OK
  Applying sessions.0001_initial... OK
(django-training) django-training % 
```

### Create super user

```python
(django-training) django-training % make makesu
cd ./djangotrainingproject && python3 manage.py createsuperuser
ユーザー名 (leave blank to use 'su3-hokkaido'): admin
メールアドレス: admin@django.com
Password: 
Password (again): 
このパスワードは ユーザー名 と似すぎています。
このパスワードは短すぎます。最低 8 文字以上必要です。
このパスワードは一般的すぎます。
Bypass password validation and create user anyway? [y/N]: y    
Superuser created successfully.
(django-training) django-training % 
```
