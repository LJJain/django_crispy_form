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

## 參考資料

> 教學網站
- https://www.youtube.com/watch?v=647j3b96aMs&list=PLEoCKCuqTqMh4WH-xXmDlQqIZmuDF09ya&index=1&ab_channel=DjangoMastery

> Templates
- https://drive.google.com/drive/folders/1bbgi3p00GzX8i8nlE9vJuKctfzlIR7ql

> JQuery CDN
- https://releases.jquery.com/

> jquery.mask CDN
- https://cdnjs.com/libraries/jquery.mask