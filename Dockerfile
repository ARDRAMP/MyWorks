from python:3.10.7
env PYTHONDDNTMRITEBYTECODE 1
env PYTHONUNBUFFERED 1
workdir /app
copy requirements.txt /app/
run pip install --upgrade pip
run pip install -r requirements.txt
copy . /app/
run python manage.py collectstatic --noinput  