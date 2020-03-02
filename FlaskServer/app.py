# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 下午5:06
# @Author  : Hui
# @File    : app.py

from flask import Flask,jsonify,request



app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': 'Buy groceries django',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python flask',
        'description': u'Need to find a good Python tutorial on the web',
        'done': True
    }
]

@app.route('/api/v1.0/tasks', methods=['post'])
def get_tasks():
    """获取请求参数"""
    #dd = request.json.get('DDD')  # json
    #aa = request.form.get('dd')  #  from
    aw = request.get_json()
    ww = aw.get("dd")
    data = {
        "dd":ww
    }
    return jsonify({'tasks': data})


if __name__ == '__main__':
    app.run(debug=True)