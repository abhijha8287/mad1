from flask import Flask, render_template, request # flask is class and Flask is object
app=Flask(__name__)  # app is variable which have all the fun which Flask have __name__ consider this page as server code.

@app.route("/") # binds url with the given below function
# get : is used to get the data from server (default) 
# post : is used to send the data to server
def home():
    return render_template("index.html")


    
@app.route("/one", methods=["GET", "POST"]) # binds url with the given below function
def index():
    if request.method == "GET":
        return render_template("form.html")

    if request.method == "POST":
        course = request.form["c_name"]
        id_name = request.form.get("id")
        return render_template("course.html", j1=course, j2=id_name)
    
app.run(debug=True)