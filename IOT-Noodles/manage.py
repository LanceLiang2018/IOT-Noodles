from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)

import config
from users import *
import mainpage
import drivers
import command

if __name__ == '__main__':
    sever_init()
    app.run(threaded=True, debug=False, host='0.0.0.0', port=8081)
