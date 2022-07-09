from flask import Flask
from service.robot.remote_access import remoteAccess

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

app.register_blueprint(remoteAccess)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000) # 내 컴퓨터가 5000포트를 못 써서 4000으로 했습니다
