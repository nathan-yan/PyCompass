from flask import Flask

application = Flask(__name__,
                    template_folder = "../templates",
                    static_folder = "../static")
