from flask import Flask 
import compass.views.home as home

application = home.application

if __name__ == "__main__":
    application.run(host = '10.104.38.217', debug = True)
