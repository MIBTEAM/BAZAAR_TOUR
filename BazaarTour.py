from flask import Flask,render_template,redirect,request,url_for

app=Flask(__name__)


# homePage route
@app.route("/")
def IndexPage():
    return render_template("index.html")

@app.route("/buyer-login", methods=["GET","POST"])
def buyer_login_page():
    if request.method == "POST":
        print("login buyer here")
        return render_template("buyer-login.html")
    else:
        return render_template("buyer-login.html")

@app.route("/register-buyer",methods=["POST"])
def register_buyer_account():
    if request.method == "POST":
        print("register buyer here")
        return render_template("testingfile.html")
    else:
        return render_template("testingfile.html")

@app.route("/seller-login")
def seller_login_page():
    return render_template("Seller-login.html")

@app.route("/register-seller",methods=["POST"])
def register_seller_account():
    print("Method----",request.method)
    if request.method == "POST":
        print("Into Post Methos")
        return render_template("testingfile.html")

@app.route("/register-sellers",methods=["GET"])
def register_seller_accounts():
    print("Method----",request.method)
    return render_template("seller-requirements-form.html")

if __name__=="__main__":
    app.run(debug=True)