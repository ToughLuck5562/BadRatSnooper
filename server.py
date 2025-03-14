from flask import Flask, render_template, request

app = Flask(__name__, template_folder="client/templates", static_folder="client/static")

@app.route("/"):
def default():
  return 404

@app.route("/dsh")
def dashboard():
  pass

@app.route("/cnts", methods=["POST", "GET"])
  Device = request.args.get('ip')
  NewData = reuqest.args.get('data')

  if request.method == "POST":
    # upload to mongodb
    
    return render_template("cnts.html", ip=Device)
