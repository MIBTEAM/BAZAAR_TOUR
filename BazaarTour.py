from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


# homePage route
@app.route("/")
def IndexPage():
    return render_template("index.html")


@app.route("/buyer-login", methods=["GET", "POST"])
def buyer_login_page():
    if request.method == "POST":
        print("login buyer here")
        return render_template("buyer-login.html")
    else:
        return render_template("buyer-login.html")

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

if __name__ == "__main__":
    app.run(debug=True,port=9999)
