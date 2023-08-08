from Website_code import create_app

app = create_app()

@app.route("/")
def index():
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=False, host = "0.0.0.0")
