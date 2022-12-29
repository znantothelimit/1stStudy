#필요한 모듈을 단계적으로 import
import os
from flask import Flask, request, render_template, redirect, url_for, jsonify
 
# static 기능 추가
app = Flask(__name__)
 
# 테스트 기능 1
@app.route('/hello') # app에서 hello라는 요청이들어오면 밑의 함수로 들어가서 실행
def hello_Flask():
    return 'Hello, Flask'

# 테스트 기능 2
@app.route('/hi')
def hi_Flask():
    return 'Hi, Flask'

# 만약에 온/습도일 때
#~~/data?temp=10&humi=20
@app.route('/data')
def data_Flask():
    return 'this is the data'

# 파이썬에서 메인함수
if __name__ == '__main__':
    app.run(  # app.run == 해당 app 실행해라
    host="0.0.0.0", # 호스트는 0.0.0.0 
    port=7777, # 7777포트 열기
    debug=True) # 디버그 메시지 출력해줘

#초기 테스트
a=10
b=20
c=a+b
print(c)
print("Hello Flask!!!")

