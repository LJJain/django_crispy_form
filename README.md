# Django Crispy Form Practice

## 日誌

> 2022.11.07
- models.py: add Candidates Model

> 2022.11.08
- register admin.py

> 2022.11.09
- install boostrap5 crispy_forms
- VALIDATION (輸入驗證)
- Phone 
- Jquery & Jquery.mask
- Install Jazzmin
- Capitalize the first and last name (models.py)

> 2022.11.12
- Radio button
- Select (選單:two methods): 1. models.py(PERSONALITY) 2. forms.py(SALARY)
- Checkbox (experience)
- signal
- files
- django-cleanup (delete file when delete candidate)
- django-multiselectfield
- django-ckeditor


## 筆記

> install crispy-bootstrap5
- pip install crispy-bootstrap5
- INSTALLED_APPS=[
    "crispy_forms",
    "crispy_bootstrap5",
    ]
- settings.py:CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
- setting.py:CRISPY_TEMPLATE_PACK = "bootstrap5"

> VALIDATION
- forms.py:from django.core.validators import RegexValidator

> Install Jazzmin
- pip install -U django-jazzmin
- INSTALLED_APPS = [
    'jazzmin',
]

> files (upload)
- settings.py:

    import os

    MEDIA_URL = '/media/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

- urls.py(project):

    from . import settings

    from django.conf.urls.static import static

    +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  (urlpatterns)

> Django Custom Admin Panel using JET Theme
- not yet

> Django Cleanup
- pip install django-cleanup
- INSTALLED_APPS = [
    'django_cleanup',
]

> django-multiselectfield
- pip install django-multiselectfield
- INSTALLED_APPS = [
    'multiselectfield',
]

> django-ckeditor
- pip install django-ckeditor
- INSTALLED_APPS = [
    'ckeditor',
]

## 參考資料

> 教學網站
- https://www.youtube.com/watch?v=647j3b96aMs&list=PLEoCKCuqTqMh4WH-xXmDlQqIZmuDF09ya&index=1&ab_channel=DjangoMastery

> Templates
- https://drive.google.com/drive/folders/1bbgi3p00GzX8i8nlE9vJuKctfzlIR7ql

> JQuery CDN
- https://releases.jquery.com/

> jquery.mask CDN
- https://cdnjs.com/libraries/jquery.mask

> Django Custom Admin Panel using JET Theme
- https://www.youtube.com/watch?v=NKuhpkqg-H8&ab_channel=DjangoMastery 

> django-multiselectfield
- https://pypi.org/project/django-multiselectfield/