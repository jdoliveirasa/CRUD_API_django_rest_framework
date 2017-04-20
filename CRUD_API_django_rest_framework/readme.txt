
curl http://localhost:9000/api/tasks/
curl -X POST http://localhost:9000/api/tasks/ -d "title=hello world&description=a whole new world"
curl -X PUT http://localhost:9000/api/tasks/1 -d "title=hello world&description=be nice"
curl -X PUT http://localhost:9000/api/tasks/1 -d "title=hello world&description=be nice&completed=True"
curl -X DELETE http://localhost:9000/api/tasks/1

https://godjango.com/43-permissions-authentication-django-rest-framework-part-2/


QuickstartDjangoRestFramework
