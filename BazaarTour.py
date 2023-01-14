from flask import Flask,render_template,redirect,request,url_for

app=Flask(__name__)


# homePage route
@app.route("/")
def IndexPage():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)