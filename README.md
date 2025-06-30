# fly.io 


## 🔧 수정파일

- config/urls.py
- todo/urls.py
- header.html
- settings.py
- .evn 

## 수정내용

1. config/urls.py
```python
path("", lambda request: redirect("todo:todo_List")),
```
todo: 앱네임추가


2. todo/urls.py
```python
app_name ="todo"
```
앱이름 추가

3. header.html
```html
{% url 'todo:todo_List' %}
```
url에 todo: 앱이름 추가

4. 자신의 fly도메인으로 수정
```python
# Fly 배포용 ALLOWED_HOSTS 설정
APP_NAME = os.environ.get("FLY_APP_NAME")

ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev", "todolist-drf-snowy-cherry-4909.fly.dev,"]
# 본인의 fly 도메인으로 수정

CSRF_TRUSTED_ORIGINS = [
    f"https://{APP_NAME}.fly.dev",
    "https://todolist-drf-snowy-cherry-4909.fly.dev/",
    ]
# 본인의 fly 도메인으로 수정
```

5. settings.py에 있는 SECRET_KEY를 .env에 이동 
```python
SECRET_KEY = env("DJANGO_SECRET_KEY")
```

![config/urls.py](images/config_urls.png)
![todo/urls.py](images/todo_urls.png)
![header.html](images/header_html.png)
![settings.py](images/settings_py.png)

111