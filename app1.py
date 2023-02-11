# from flask import Flask, render_template, request, session
# from flask_session import Session
# from Otp import sendOTP
# from Utils import *


# app = Flask(__name__)
# app.config.from_object("config")
# app.secret_key = app.config["SECRET_KEY"]
# Session(app)


# @app.route('/')
# def index():
#     return render_template("buyer_login.html")


# @app.route('/register_seller', methods=["POST", "GET"])
# def register_seller():
#     if (request.method == "GET"):
#         return render_template('register_seller.html')
#     else:
#         mail = request.form.get('email')
#         otp = sendOTP(mail)
#         session['otp'] = str(otp)
#         addSellerInSession(request)
#         return render_template("seller_otp.html")


# @app.route('/seller_otp_verification', methods=["POST"])
# def seller_otp_verification():
#     otp = session.get('otp')
#     formOtp = request.form.get('first')
#     formOtp += request.form.get('second')
#     formOtp += request.form.get('third')
#     formOtp += request.form.get('fourth')
#     formOtp += request.form.get('fifth')
#     formOtp += request.form.get('sixth')
#     if (otp == formOtp):
#         addSellerFromSession2DB()
#         session.clear()
#         return "seller registered"
#     else:
#         removeDirectory("./static/sellerData/" + session['userid'])
#         session.clear()
#         return "seller not registered"


# @app.route('/register_buyer', methods=["GET", "POST"])
# def register_buyer():
#     if (request.method == "GET"):
#         return render_template('/register_buyer.html')
#     else:
#         mail = request.form.get("email")
#         otp = sendOTP(mail)
#         session['otp'] = str(otp)
#         addBuyerInSession(request)
#         return render_template('otp.html')


# @app.route('/otp_verification', methods=["GET"])
# def otp_verification():
#     otp = session.get('otp')
#     formOtp = request.args.get('first')
#     formOtp += request.args.get('second')
#     formOtp += request.args.get('third')
#     formOtp += request.args.get('fourth')
#     formOtp += request.args.get('fifth')
#     formOtp += request.args.get('sixth')
#     print("otp sent : ", otp)
#     print("otp entered : ", formOtp)
#     if (otp == formOtp):
#         addBuyerFromSession2DB()
#         session.clear()
#         return "buyer registered"
#     else:
#         session.clear()
#         return "buyer not registered"


# @app.route('/login_seller', methods=["POST", "GET"])
# def login_seller():
#     if (request.method == "GET"):
#         return render_template("seller_login.html")
#     else:
#         return render_template('register_seller.html')


# app.run(debug=True)
