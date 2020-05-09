from flask import Flask, request, render_template, send_from_directory,jsonify
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/",methods=['POST','GET'])
def main() :
	return "Server is Active"

@app.route("/cin_kyc",methods=['POST','GET'])
def cin_kyc():
	
	data = request.get_json()
	print(data)
	data_type = data['data_type']
	selfie = data['selfie']
	cin_front = data['cin_front']
	cin_back = data['cin_back']

	
	return jsonify({"cin_verif_front":True,"cin_verif_back":False,"face_match":True,"cin_number":"43453345"})

	



@app.route("/passport_kyc",methods=['POST','GET'])
def passport_kyc():
			
	return "Passport not yet implemented"
	


if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port=80,threaded = True)	
