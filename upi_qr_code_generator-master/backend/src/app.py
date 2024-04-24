from flask import Flask, render_template,request,jsonify,send_file
from utils.upi_qr_code_generator import generateUPIQR
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return "QR code generator app"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/upi-qr",methods=["POST"])
def getQR():
    amount = request.args.get("amount")
    upi_address = request.args.get("adr")
    user_name = request.args.get("name")
    overlay_img = request.files
    return generateUPIQR(upi_address,amount,overlay_img,user_name)

if __name__ == "__main__":
    app.run(debug=True)
