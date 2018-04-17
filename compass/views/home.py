from . import application

@application.route("/")
def index():
    return "hello world!"