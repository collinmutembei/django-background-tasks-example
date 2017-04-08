django-background-tasks-example
===============================
This example shows how to set up and use [django-background-tasks](https://github.com/arteria/django-background-tasks/).

## Usage

Start the server.

```
python manage.py runserver
```

Register a task

```
curl -d message=hello http://localhost:8000/api/v1/tasks/
```

Process tasks

```
python manage.py process_tasks
```
