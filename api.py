from flask import Flask, render_template,request,jsonify,json
import requests
import hashlib
import ecdsa
import binascii




app=Flask(__name__)


headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

def hash_password(password):
	hash_object = hashlib.sha256(password)
	hash_password = hash_object.hexdigest()
	return (hash_password)


@app.route('/signup', methods=['POST'])
def homepage():
	if request.headers['Content-Type'] == 'application/json':
		response=request.json
		username=response["email"]
		password=response["password"]
		confirm_password=response["confirm_password"]
		if (password == confirm_password):
			#hash password
			finalpassword=hash_password(password)
			#Send request to storj api
			data = '{ "email":"'+ str(username)+'", "password": "'+ finalpassword+'" }'
			response1 = requests.post('https://api.storj.io/users', headers=headers, data=data).json()
			return jsonify(response1)


@app.route('/add-key', methods=['POST'])
def add_key():
	if request.headers['Content-Type'] == 'application/json':
		response=request.json
		username=response["email"]
		password=response["password"]
		key=response["ecdsakey"]
		#hash password
		finalpassword=hash_password(password)
		#send request to storj api to register keys
		data = '{ "key": "'+key+'" }'
		response1 = requests.post('https://api.storj.io/keys', headers=headers, data=data, auth=(username, finalpassword)).json()
		return jsonify(response1)

@app.route('/get-key',methods=['POST'])
def get_key():
	if request.headers['Content-Type'] == 'application/json':
		response=request.json
		username=response["email"]
		password=response["password"]
		#hash password
		finalpassword=hash_password(password)
		#send request to storj api to list keys
		response1 = requests.get('https://api.storj.io/keys', headers=headers, auth=(username, finalpassword)).json()
		return jsonify(response1)
		
		return render_template('get-key.html',keys=keys)


@app.route('/create-bucket',methods=['POST'])
def create_bucket():
	if request.headers['Content-Type'] == 'application/json':
		response=request.json
		username=response["email"]
		password=response["password"]
		key=response["ecdsakey"]
		bucketname=response['bucketname']
		#hash password
		finalpassword=hash_password(password)

		#Prepare data
		data='{"pubkeys":["'+key+'"],"name":"'+bucketname+'"}'
		#send response
		response1=requests.post('https://api.storj.io/buckets',headers=headers,data=data,auth=(username,finalpassword)).json()
		
		return jsonify(response1)
	

@app.route('/get-bucket',methods=['POST'])
def get_bucket():
	if request.headers['Content-Type'] == 'application/json':
		response=request.json
		username=response["email"]
		password=response["password"]
		#key=request.form.get('ecdsa-key')
		#hash password
		finalpassword=hash_password(password)

		response1 = requests.get('https://api.storj.io/buckets', headers=headers, auth=(username, finalpassword)).json()
		
		return jsonify(response1)

	

if __name__ == '__main__':
	app.run(debug=True)



