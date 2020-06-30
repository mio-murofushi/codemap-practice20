from flask import Flask, request, render_template
from flask import make_response
from flask import session
import datetime

app = Flask(__name__)
app.secret_key = 'hogehoge'

lastlogin=""
nowlogin=""


@app.route("/cookie", methods=["POST","GET"])
def sample_cookie():
    first_mes=""
    re_mes=""

    # リクエストを送信する回数をカウント
    # リクエストを送信した時間を受け取る
    count = request.cookies.get('count')
    lastlogin = request.cookies.get("lastlogin", "")
    nowlogin = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    # カウント確認
    if count is None:
        count = 1
        first_mes = "初めてのアクセスです。"
        print(first_mes)
    else:
        count = int(count) + 1
        re_mes = "カウントを追加しました！"
        print(re_mes)
    
    response = make_response()

    if "del" in request.form.keys():
        response.set_cookie('count', str(count), expires=0)
        response.set_cookie('lastlogin', lastlogin, expires=0)
        response.set_cookie('nowlogin', nowlogin, expires=0)
        print("cookie削除しました")

    else:
        # count 
        # last_access 日時情報
        response.set_cookie('count', str(count))
        response.set_cookie('lastlogin', lastlogin)
        response.set_cookie('nowlogin', nowlogin)
    
    params = {
        "first_mes":first_mes,
        "re_mes":re_mes,
        "count":count,
        "lastlogin":lastlogin,
        "nowlogin":nowlogin
    }
    
    return render_template("cookie.html", **params)

@app.route("/session")
def sample_session():
    count = session.get('count')
    if count is None:
        count = 1
    else:
        count = int(count) + 1
    session["count"] = count

    return "{}回目の訪問です。".format(count)