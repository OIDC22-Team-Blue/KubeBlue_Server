import paramiko
from flask import Blueprint

remoteAccess = Blueprint("remote access", __name__, url_prefix="/remoteAccess")


@remoteAccess.route('/runTestcase')
def run_testcase():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect("110.165.18.0", username="root", password="oidc001", timeout=5)  # 대상IP, User명, 패스워드, 타임아웃 입력
        print('ssh connected.')  # ssh 정상 접속 후 메시지 출력

        ssh.close()  # ssh 접속하여 모든 작업 후 ssh 접속 close 하기

        return "connection success"

    except Exception as err:
        print(err)  # ssh 접속 실패 시 ssh 관련 에러 메시지 출력
        return "connecting fail"
