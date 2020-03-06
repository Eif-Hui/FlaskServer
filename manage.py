# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 上午9:31
# @Author  : Hui
# @File    : manage.py

from flask import Flask

app = Flask(__name__)
app.register_blueprint()
app.register_blueprint()

def app_start():
	sched.start()
	http_server = WSGIServer(('127.0.0.1', 5000), app)
	http_server.serve_forever()
if __name__ == '__main__':
	#app_start()
	app.run(debug=True)