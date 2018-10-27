from flask import Flask, session, redirect, url_for, escape, request, render_template
from manage import app
from actoken import token_check
import json

queue = []
tid_starter = 1


def find_task(tid):
    for t in queue:
        if t.tid == tid:
            return t
    return None


def find_tasks(did):
    for t in queue:
        if t.dest == did:
            return t
    return None


def replace_task(task):
    for i in range(len(queue)):
        if queue[i].did == task.did:
            queue[i] = task
            return


class Task:
    def __init__(self, did, dest, data=''):
        global tid_starter
        self.WAITING = 'WAITING'
        self.FINISH = 'FINISH'
        self.did = did
        self.dest = dest
        self.data = data
        self.tid = str(tid_starter)
        tid_starter = tid_starter + 1
        self.stat = self.WAITING

    def json(self):
        js = {'did': self.did,
              'dest': self.dest,
              'data': self.data,
              'tid': self.tid,
              }
        return json.dumps(js)


@app.route('/command_new', methods=['POST'])
def command_new():
    did = request.form['did']
    dest = request.form['dest']
    data = request.form['data']
    task = Task(did, dest, data)
    queue.append(task)
    tid = task.tid
    return str(tid)


@app.route('/command_task_stat', methods=['POST'])
def command_task_stat():
    tid = request.form['tid']
    task = find_task(tid)
    if task is None:
        return 'No task.'
    return task.stat


@app.route('/command_get_task', methods=['POST'])
def command_get_task():
    did = request.form['did']
    token = request.form['token']
    if not token_check(did, token):
        return 'Token Error.'
    task = find_tasks(did)
    if task is None:
        return 'No task.'
    return task.json()


@app.route('/command_fetch', methods=['POST'])
def command_fetch():
    did = request.form['did']
    token = request.form['token']
    if not token_check(did, token):
        return 'Token Error.'
    tid = request.form['tid']
    data = request.form['data']
    task = find_task(tid)
    if task is None:
        return 'No task.'
    task.data = data
    task.stat = task.FINISH
    replace_task(task)
    return 'Success'


@app.route('/command_finish', methods=['POST'])
def command_finish():
    did = request.form['did']
    token = request.form['token']
    if not token_check(did, token):
        return 'Token Error.'
    tid = request.form['tid']
    task = find_task(tid)
    if task is None:
        return 'No task.'
    data = task.data
    queue.remove(task)
    return data




