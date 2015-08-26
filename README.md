django-background-tasks-example
===============================

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

## Python 2: OK

Tasks are executed and moved from `backgroun_task` table to `background_task_completedtask` table.

```
$ cat logs/debug.log
DEBUG 2015-08-26 03:29:52,391 views 67989 4369776640 calling demo_task. message=hello
DEBUG 2015-08-26 03:30:53,588 tasks 68009 140735087371008 demo_task. message=hello

$ sqlite3 db.sqlite3
SQLite version 3.8.5 2014-08-15 22:37:57
Enter ".help" for usage hints.
sqlite> select * from background_task;
sqlite> select * from background_task_completedtask;
1|api.tasks.demo_task|[["hello"], {}]|c8f1363b9f690df3369658038248adb182707b2b|0|2015-08-26 03:30:53.588400|0|||68009|2015-08-26 03:30:53.585170
sqlite>
```

You can run this example with python 2 using git python2 branch.

## Python 3

You need django-background-tasks >= 1.0.7 for Python 3.

```
$ cat logs/debug.log
DEBUG 2015-08-26 12:49:28,769 views 1779 4477964288 calling demo_task. message=hello
DEBUG 2015-08-26 12:50:31,981 tasks 1954 140735194714880 demo_task. message=hello

$ sqlite3 project/db.sqlite3
SQLite version 3.8.5 2014-08-15 22:37:57
Enter ".help" for usage hints.
sqlite> select * from background_task;
sqlite> select * from background_task_completedtask;
1|api.tasks.demo_task|[["hello"], {}]|c8f1363b9f690df3369658038248adb182707b2b|0|2015-08-26 12:50:31.981568|0|||1954|2015-08-26 12:50:31.977507
```

You can run this example with python 3 using git master branch.
