from flask import Flask, render_template

app = Flask(
  __name__,
  static_folder="static",
  static_url_path=""
)

@app.route("/")
@app.route("/<name>")
def hello(name=None):
  return render_template("hello.html", name=name)

@app.route("/profile/<username>")
def profile(username):
  return "You are viewing {}'s profile".format(username)

@app.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1, num2):
  result = num1 * num2
  return str(result)

if __name__ == "__main__":
  app.run()