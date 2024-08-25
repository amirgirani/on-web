from flask import Blueprint, render_template, request, redirect, session, abort
from config import admin_login_password, admin_login_username

app = Blueprint("admin", __name__)


@app.route('/admin/login', methods=["POST", "GET"])
def login():
    if request.method == ["POST"]:
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        if username == admin_login_username and password == admin_login_password:
            session['admin_login'] = username
            print(session['admin_login'])
            print(username)
            return redirect("/admin/dashboard")
        else:
            return redirect("/admin/login")
    else:
        return render_template('/admin/login.html')


@app.route('/logins', methods=["post"])
def logins():
    if request.method == "POST":
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        if username == admin_login_username and password == admin_login_password:
            session['admin_login'] = username
            return redirect("/admin/dashboard")
        else:
            return redirect("/admin/login")
    else:
        return render_template('/admin/login.html')


@app.route('/admin/dashboard', methods=["GET"])
def dashboard():
    try:
        x = session["admin_login"]
        return "dash"
    except:
        abort(403)

    if session["admin_login"]:

        return "dash"
    else:
        abort(403)
