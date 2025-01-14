#!/usr/bin/env python3

import os
import yaml
from flask import Flask

app = Flask(__name__)


@app.route(
    "/",
    methods=["GET", "POST", "PUT", "DELETE"],
)
def index():
    return "Hello world\n"


if __name__ == "__main__":
    if os.path.isfile("config.yml"):
        with open(os.path.join(os.getcwd(), "config.yml"), "r", encoding="utf-8") as f:
            config = yaml.load(f, Loader=yaml.SafeLoader)

        host = config["server"]["listen"]["address"]
        port = config["server"]["listen"]["port"]
    else:
        host = "0.0.0.0"
        port = 8080

    app.run(debug=True, host=host, port=port)
