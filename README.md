# stackcoin

Clone the repo and create a virtual env, then run:
```
cp .env.example .env
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata sample.json
python manage.py runserver
visit <http://localhost:8000/>
```
