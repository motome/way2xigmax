
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "「XIGMAXへの道へようこそ」"

# goodbye関数の追加
@app.route("/goodbye")
def goodbye():
    return "「ありがとうございました。またのお越しをお待ちしております。」"

# あいさつする関数を作成
@app.route("/user/<name>")
def hi(name):
    html = f"<html><body><h1>いらっしゃいませ！{name}さん</h1></body></html>"
    return html


# 挨拶する関数をHTMLに変更
@app.route("/profile/<name>")
def profile(name):
    html = f"<html><body><h1>{name}さんの登録情報です</h1></body></html>"
    return html

  # ログイン機能
@app.route("/login", methods=["GET", "POST"])
def login():
    # リクエストメソッドGETのときは以下の処理を行う
    if request.method == "GET":
        return '''
        <form action="/login" method="post">
            Password:<input type="text"><br>
            <input type='submit'>
        </from>
        '''
    # リクエストメソッドPOSTの時は以下の処理を行う
    return "Logged in"  
  
if __name__ == '__main__':
      app.run(port=8000, debug=True)



