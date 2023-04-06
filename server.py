from flask import Flask, render_template

# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/play/<int:num>')
@app.route('/play')
@app.route('/play/<int:num>/<string:color>')
def play(num=3, color='blue'):
    return render_template("index.html", num=num, color=color)






if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
