from flask import Flask, render_template
import pymysql
from db_connect import db
import json

app = Flask(__name__)

# db config 파일 불러오기
with open("./db_config.json", 'r') as f:
    dbConfig = json.load(f)

print(dbConfig['name'])

# db 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    dbConfig['name'], dbConfig['dbPassword'], dbConfig['address'], dbConfig['port'], dbConfig['dbName'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

# table 생성
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
