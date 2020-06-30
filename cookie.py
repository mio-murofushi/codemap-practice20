from flask import Flask, request, render_template
from flask import make_response
from flask import session
import datetime

app = Flask(__name__)
app.secret_key = 'hogehoge'

@app.route("/cookie", methods=["POST","GET"])
def sample_cookie():
    first_mes=""
    re_mes=""
    lastlogin=""
    nowlogin=""
    mes = ""

    # リクエストを送信する回数をカウント
    # リクエストを送信した時間を受け取る
    count = request.cookies.get('count')
    lastlogin = request.cookies.get("nowlogin", "")
    nowlogin = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    # delボタンが押されたかどうかを判断
    if "del" in request.form.keys():
        mes = "削除ボタンが押されました"
    else:
        # カウント確認
        if count is None:
            count = 1
            first_mes = "初めてのアクセスです。"
            print(first_mes)
        else:
            count = int(count) + 1
            re_mes = "カウントを追加しました！"
            print(re_mes)

    params = {
        "mes":mes,
        "first_mes":first_mes,
        "re_mes":re_mes,
        "count":count,
        "lastlogin":lastlogin,
        "nowlogin":nowlogin
    }
    
    response = make_response(render_template("cookie.html", **params))

    if "del" in request.form.keys():
        response.set_cookie('count', str(count), expires=0)
        response.set_cookie('lastlogin', lastlogin, expires=0)
        response.set_cookie('nowlogin', nowlogin, expires=0)
        print("cookie削除")

    else:
        response.set_cookie('count', str(count))
        response.set_cookie('lastlogin', lastlogin)
        response.set_cookie('nowlogin', nowlogin)
    
    #return render_template("cookie.html", **params)
    return response

@app.route("/session")
def sample_session():
    count = session.get('count')
    if count is None:
        count = 1
    else:
        count = int(count) + 1
    session["count"] = count

    return "{}回目の訪問です。".format(count)