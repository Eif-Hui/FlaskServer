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

@app.route('/api/v1.0/tasks', methods=['post','get'])
def get_tasks():
    """获取请求参数"""
    #dd = request.json.get('DDD')  # json
    #aa = request.form.get('dd')  #  from
    aw = request.get_json()
    ww = aw.get("dd")
    print(ww)
    data = {
        "dd":ww
    }
    return jsonify({'tasks': data})

@app.route('/db/testCase/insert',methods=['post'])
def insert_db():
    caseId = request.get_json('caseId')
    story = request.get_json('story')
    title = request.get_json('title')
    method = request.get_json('method')
    path = request.get_json('path')
    req_data = request.get_json('req_data')
    sql = request.get_json('sql')
    expect1 = request.get_json('expect1')
    expect2 = request.get_json('expect2')
    expect3 = request.get_json('expect3')




if __name__ == '__main__':
    app.run(debug=True)