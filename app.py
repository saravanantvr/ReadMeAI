from flask import Flask, redirect, session
import random
import string

app = Flask(__name__)
app.secret_key = "readme_ai_secret_key"


# -----------------------------
# Generate Random Token
# -----------------------------
def generate_token(length=50):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# -----------------------------
# HOME PAGE (WELCOME)
# -----------------------------
@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>

<head>
    <title>ReadMe AI</title>
</head>

<body style="
    margin:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
    url('/static/images/bg.jpg');
    background-size:cover;
    background-position:center;
">

<div style="
    width:520px;
    background:rgba(255,255,255,0.92);
    padding:40px;
    border-radius:20px;
    text-align:center;
">

    <h1 style="color:#0d6efd;">📘 ReadMe AI</h1>
    <p>Smart Classroom System</p>

    <hr>

    <a href="/login/admin" style="display:block;margin:10px;padding:15px;background:red;color:white;text-decoration:none;border-radius:10px;">👑 Main Admin</a>

    <a href="/login/staff" style="display:block;margin:10px;padding:15px;background:orange;color:white;text-decoration:none;border-radius:10px;">👨‍💼 Staff</a>

    <a href="/login/teacher" style="display:block;margin:10px;padding:15px;background:green;color:white;text-decoration:none;border-radius:10px;">👨‍🏫 Teacher</a>

    <a href="/login/student" style="display:block;margin:10px;padding:15px;background:blue;color:white;text-decoration:none;border-radius:10px;">🎓 Student</a>

</div>

</body>
</html>
"""


# -----------------------------
# LOGIN ROUTE (GENERATES RANDOM URL)
# -----------------------------
@app.route("/login/<role>")
def login(role):

    token = generate_token()

    session["token"] = token
    session["role"] = role

    return redirect(f"/dashboard/{token}")


# -----------------------------
# DASHBOARD (RANDOM URL)
# -----------------------------
@app.route("/dashboard/<token>")
def dashboard(token):

    if "token" not in session:
        return "<h3>Session Expired</h3>"

    if token != session["token"]:
        return "<h3>Access Denied</h3>"

    role = session.get("role", "user")

    return f"""
    <h1 style='text-align:center;margin-top:100px;'>
        Welcome {role.upper()} 👋<br><br>

        Your Secure URL:<br>
        <span style="color:green">{token}</span>
    </h1>
    """


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)