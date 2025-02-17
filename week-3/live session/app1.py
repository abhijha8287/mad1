from flask import Flask, render_template
app1=Flask(__name__)

@app1.route("/")
def home():
    fruits=["Mango", "Banana","orange", "Papaya"]
    return render_template("home1.html", name="Abhishek",fruits=fruits)

if __name__=="__main__":
    app1.run(debug=True)
