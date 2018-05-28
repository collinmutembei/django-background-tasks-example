django-background-tasks-example
===============================
This example shows how to set up and use [django-background-tasks](https://github.com/arteria/django-background-tasks/).

## Usage

Install project dependencies
```shell
pip install -r requirements.txt
```

Prepare database
```shell
cd project
python manage.py migrate
```

Start the server.

```shell
python manage.py runserver
```

Register a task (on separate terminal)

```
curl -d message=hello http://localhost:8000/api/v1/tasks/
```

Process tasks

```
python manage.py process_tasks
```
