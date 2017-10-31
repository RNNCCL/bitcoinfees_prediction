#!/usr/bin/env python
# -*- conding: utf-8 -*-

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from get_info import Fee

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def show():
    fee = Fee()
    fee_info = {}
    fee_info['fastest_fee'] = fee.fastest_fee()
    fee_info['half_hour_fee'] = fee.half_hour_fee()
    fee_info['hour_fee'] = fee.hour_fee()

    return render_template('index.html', fee_info=fee_info)


if __name__ == '__main__':
    app.run (debug=True)
