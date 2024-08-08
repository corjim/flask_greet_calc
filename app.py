# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_num():
    '''Sums a and b parameters'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f' <h1>calculated {a} + {b} = {a + b} </h1>'

@app.route('/sub')
def sub_num():
    '''Find the difference btw the parameter'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f' <h1>calculated {a} - {b} = {a - b} </h1>'


@app.route('/mult')
def sub_num():
    '''multiple the a and b parameter'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f'<h1> calculated {a} * {b} = {a * b} </h1>'

@app.route('/div')
def sub_num():
    '''Find the difference btw the parameter'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f'<h1> calculated {a}/{b} = {a / b} </h1>'

 #      **** From Operations file   ***


operators ={
    'sub': sub,
    'add': add,
    'div': div,
    'mult': mult
}


@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)