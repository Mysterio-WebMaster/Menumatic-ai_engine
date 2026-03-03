from flask import Flask
from controllers import recommend_blueprints

app = Flask(__name__)

for bp in recommend_blueprints:
    app.register_blueprint(bp, url_prefix="/v1")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
