from flask import Flask, render_template, redirect, request, url_for, session
from flask_session import Session
from Otp import sendOTP
from Utils import *
from flask_restful import Api
from resources import routes
from database.models import User, seshion



app = Flask(__name__)

app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]
Session(app)

api=Api(app)
routes.initialize_routes(api)


# homePage route
@app.route("/")
def IndexPage():
    return render_template("index.html")


@app.route('/cards')
def cards():
    return render_template('cards.html')



# registeration code
@app.route('/register_seller', methods=["POST", "GET"])
def register_seller():
    if (request.method == "GET"):
        return render_template('register_seller.html')
    else:
        mail = request.form.get('email')
        otp = sendOTP(mail)
        session['otp'] = str(otp)
        addSellerInSession(request)
        return render_template("seller_otp.html")


@app.route('/seller_otp_verification', methods=["POST"])
def seller_otp_verification():
    otp = session.get('otp')
    formOtp = request.form.get('first')
    formOtp += request.form.get('second')
    formOtp += request.form.get('third')
    formOtp += request.form.get('fourth')
    formOtp += request.form.get('fifth')
    formOtp += request.form.get('sixth')
    if (otp == formOtp):
        addSellerFromSession2DB()
        first=session.get('firstname')
        last=session.get('lastname')
        userid=session.get('userid')
        session.clear()
        session['id'] = userid
        session['firstname']=first
        session['lastname']=last
        #
        return "seller registered"
    else:
        removeDirectory("./static/sellerData/" + session['userid'])
        session.clear()
        return render_template('index.html')


@app.route('/register_buyer', methods=["GET", "POST"])
def register_buyer():
    if (request.method == "GET"):
        return render_template('/register_buyer.html')
    else:
        mail = request.form.get("email")
        otp = sendOTP(mail)
        session['otp'] = str(otp)
        addBuyerInSession(request)
        return render_template('otp.html')


@app.route('/otp_verification', methods=["GET"])
def otp_verification():
    otp = session.get('otp')
    formOtp = request.args.get('first')
    formOtp += request.args.get('second')
    formOtp += request.args.get('third')
    formOtp += request.args.get('fourth')
    formOtp += request.args.get('fifth')
    formOtp += request.args.get('sixth')
    print("otp sent : ", otp)
    print("otp entered : ", formOtp)
    if (otp == formOtp):
        addBuyerFromSession2DB()
        userid=session.get('userid')
        session.clear()
        session['cart']=''
        session['id']=userid
        return render_template('index.html')
    else:
        session.clear()
        return render_template('index.html')



# @app.route('/login', methods=['GET',"POST"])
# def log_in():
#     if(method=='GET'):

#     res=seshion.query(User.user_id).filter(User.email==email, User.password==password).all()
#     if(len(res)==0):
#         raise Exception('invalid')
#     else:
#         id=res[0][0]
#         if(id[2]=='S'):
#             pass
#         elif (id[2]=='A'):
#             pass
#         else:
#             session['id']=id



# end registeration












@app.route("/login", methods=["GET", "POST"])
def buyer_login_page():
    if request.method == "GET":
        return render_template('login.html')
    else:
        email = request.form.get('login_email')
        password = request.form.get('password')
        res=seshion.query(User.user_id).filter(User.email==email, User.password==password).all()
        if(len(res)==0):
            return render_template('login.html', error="Invalid email or password")
        else:
            id=res[0][0]
            if(id[2]=='S'):
                pass
            elif (id[2]=='A'):
                pass
            else:
                session['id']=id
                session['cart']=''
                return render_template("index.html")

@app.route("/contact_us")
def Contact_us():
    return render_template("About_us_and_policies/contact.html")


@app.route("/about_us")
def About_us():
    return render_template("About_us_and_policies/AboutUs.html")
@app.route("/our_team")
def Our_Team():
    return render_template("Team_intro/ourTeam.html")

@app.route("/policies")
def Policies():
    return render_template("About_us_and_policies/Policies.html")

@app.route("/privacy_policies")
def Privacy_Policy():
    return render_template("About_us_and_policies/policies/PrivacyPolicy.html")
@app.route("/return_policies")
def Return_Policy():
    return render_template("About_us_and_policies/policies/ReturnPolicy.html")
@app.route("/exchange_policies")
def Exchange_Policy():
    return render_template("About_us_and_policies/policies/ExchangePolicy.html")
@app.route("/delivery_policies")
def Delivery_Policy():
    return render_template("About_us_and_policies/policies/DeliveryPolicy.html")
@app.route("/customer_care")
def Customer_Care():
    return render_template("About_us_and_policies/CustomerCare/customerCare.html")
@app.route("/FAQs")
def FAQs():
    return render_template("faq.html")

@app.route("/buyer_dashboard")
def Buyer_Dashboard():
    return render_template("buyer_dashboard.html")

@app.route("/wish")
def Wish():
    return render_template("wish.html")

if __name__ == "__main__":
    app.run(debug=True,port=9999)
