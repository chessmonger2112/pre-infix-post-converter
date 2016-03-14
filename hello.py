from flask import Flask,redirect, url_for, render_template, request
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    monger = "MONGERTRON!!"
    return render_template('index.html',monger=monger)

@app.route("/calculate",methods=["POST"])
def calculate():
    conversionFrom = request.form["conversionType"]
    conversionTo = request.form["conversionType2"]
    expression = request.form["expression"]
    monger = [conversionFrom,conversionTo]

    import re
    def isOperator(candidate,plus):
            return (candidate == "+" and plus) or (candidate == "*" and not plus)
    def isNumber(candidate):
        return candidate != "*" and candidate != "+"

    def convert(command,plus):
        index = 1
        length = len(command)
        while (index < length -1):
            first = command[index - 1]
            second = command[index]
            third = command[index + 1]
            if isNumber(first) and isOperator(second,plus) and isNumber(third):
                for x in range(3):
                    command.pop(index-1) #remove as seperate elements in array
                command.insert(index-1,first+third+second) #put them back in postfix notation
                return convert(command,plus)
            index +=1
        return command

    def reorganize(command,operator):
        length = len(command)
        for index in range(1,length - 1):
            first = command[index - 1]
            second = command[index]
            third = command[index + 1]
            if first == third and second.isdigit() and  first == operator:
                organized = command[:index - 1] + second + first + third  + command[index + 2:]
                return reorganize(organized,operator)
        return command



    def answer(str):
        arr = list(str)
        arr2 = convert(arr,False) #runs conversion first for only multiplication to preserve order of operationss
        arr3 = convert(arr2,True) #now converts for addition
        unorganized = "".join(arr3)
        organized1 = reorganize(unorganized,"+") #step1 of lexographic sort
        organized2 = reorganize(organized1,"*")
        return organized2






    new_format = answer(expression)
    return render_template("index.html",result=new_format)





#messing around
@app.route('/nutsack')
def hello_nuts():
    return redirect(url_for("boner"))
@app.route("/random")
def random():
    char = os.urandom(1)
    return "random bro %s" %char

@app.route("/boner")
def boner():
    return "<button>My butt itches</button>"


@app.route('/<username>')
def hello_user(username):
    return 'Hello %s' %username


if __name__ == '__main__':
    app.run(debug=True)
