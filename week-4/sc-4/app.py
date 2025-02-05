from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        # Handle form submission here if needed
        name = request.form.get('Name')
        return f"Hello, {name}!"  # Example response after form submission
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
