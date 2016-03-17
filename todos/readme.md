#说明文档

## API接口说明
<table>
	<tr>
		<td>API(路由)</td>
		<td>接收</td>
		<td>返回</td>
	</tr>
	<tr>
		<td>"/"(首页)</td>
		<td></td>
		<td>show.html</td>
	<tr>
		<td>"/todos/api/logup/todos"（注册）</td>
		<td>{"username": username,"password":password}</td>
		<td>{'logup':fs} (fs = {"done":bool,"message":message})
	</tr>
	<tr>
		<td>"/todos/api/login/todos"(登录)</td>
		<td>{"username":username,"password":"password"}</td>
		<td>{'Todo':ps} (ps={"done":True,"message":message,"title":title,"body":body})
	</tr>
	<tr>
		<td>"/todos/api/update/todos"(添加文章)</td>
		<td>{"title":title,"body":body,"done":True}</td>
		<td>{'update':results} (results={'done':bool})</td>
	<tr>
		<td>"/todos/api/change/todos"(改变文章)</td>
		<td>{"'title':title,
            'change_title':change_title,
            'change_body':chang_body,
            'done':True,
            'which':choose"}</td>
		<td>{'change':results} (results={'done':bool})</td>
	<tr>
		<td>"todos/api/delete/todos"(删除文章)</td>
		<td>{"done":True}</td>
		<td>{'delete':results} {results = {'done':bool}}</td>
	<tr>
		<td>"todos/api/logout/todos" (登出)</td>
		<td>{'done':True}</td></td>
		<td>{'logout':result} {result = {'done':bool}}</td>
		</tr>
## method of application usage
Install
========
```
$ python manage.py createall
```

Running
========
```bash
$ python manage.py runserver
```
Remove
========
```bash
$ python manage.py dropall
```
