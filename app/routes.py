from app import application as app
from app import model
from flask import render_template, Response, redirect
USER="user"
PASS="pass"
#TODO: Change these
DEBUG = True
def dbg_print(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def restricted(function):
    def restrictor(username, password, *args, **kwargs):
        # global USER, PASS
        # dbg_print("Inside restrictor", args, kwargs)
        # if username == USER and password == PASS:
        return function(*args, **kwargs)
        #This is here if we want to implement a user system.
        # else:
        #     dbg_print("Authentication Error: USER: {}\tPASS:{}".format(username, password))
        #     return "<h1>AUTH ERROR</h1>"
            #TODO: put proper error screen
    return restrictor

def api(function):
    @app.route("/api/<username>/<password>/{}/<path:otherArgs>".format(function.__name__))
    @restricted
    def x(*args, **kwargs):
        otherArgs = kwargs["otherArgs"]
        otherArgs = otherArgs.split("/")
        dbg_print("Inside api" ,otherArgs)
        return function(*otherArgs)
    return x

#############################
#                           #
#                           #
#             API           #
#                           #
#                           #
#############################

#

@api
def predict(*args):
    try:
        result = app.model.model.predict(*args)
        return ("<h1>{}</h1>".format(result))
    except:
        print("PROBLEMS, PROBLEMS")
