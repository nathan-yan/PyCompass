from flask import Flask 
import compass.views.home as home

application = home.application

if __name__ == "__main__":
    application.run(host = '192.168.1.22', debug = True)
