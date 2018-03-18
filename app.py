from flask import Flask, render_template, flash,request,url_for,redirect
import requests
import hashlib
import ecdsa
import binascii
import os




app=Flask(__name__)


headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}


@app.route('/', methods=['GET', 'POST'])
def homepage():
	if request.method == 'POST':
		username=request.form.get('email')
		password=request.form.get('password')
		confirm_password=request.form.get('confirmpassword')
		if (password == confirm_password):
			hash_object = hashlib.sha256(password)
			hash_password = hash_object.hexdigest()
			#Send request to storj api
			data = '{ "email":"'+ username+'", "password": "'+ hash_password+'" }'
			response = requests.post('https://api.storj.io/users', headers=headers, data=data).json()
			flash(response)
			return render_template('signup.html')
		else:
			flash("Invalid credentials Please try again")
			return render_template('signup.html')
	else:
		flash("hello World")
		return render_template('signup.html')


@app.route('/add-key/', methods=['GET','POST'])
def add_key():
	if request.method == 'POST':
		username=request.form.get('email')
		password=request.form.get('password')
		key=request.form.get('ecdsakey')
		#hash password
		hash_object = hashlib.sha256(password)
		hash_password = hash_object.hexdigest()
		#send request to storj api to register keys
		data = '{ "key": "'+key+'" }'
		response = requests.post('https://api.storj.io/keys', headers=headers, data=data, auth=(username, hash_password)).json()
		flash(response)
		return render_template('add-key.html')
	else:
		flash("Add key to do your transactions easily")
		return render_template('add-key.html')

@app.route('/get-key/',methods=['GET','POST'])
def get_key():
	if request.method == 'POST':
		username=request.form.get('email')
		password=request.form.get('password')
		key=request.form.get('ecdsa-key')
		#hash password
		hash_object = hashlib.sha256(password)
		hash_password = hash_object.hexdigest()
		response = requests.get('https://api.storj.io/keys', headers=headers, auth=(username, hash_password)).json()
		dict1=response[0]
		keys=dict1['key']
		flash(keys)
		
		return render_template('get-key.html',keys=keys)

	else:
		flash("Get Your Key pair")
		return render_template('get-key.html')

@app.route('/create-bucket/',methods=['GET','POST'])
def create_bucket():
	if request.method == 'POST':
		username=request.form.get('email')
		password=request.form.get('password')
		pubkey=request.form.get('pubkey')
		bucketname=request.form.get('bucketname')
		#hash password
		hash_object = hashlib.sha256(password)
		hash_password = hash_object.hexdigest()
		#Prepare data
		data='{"pubkeys":["'+pubkey+'"],"name":"'+bucketname+'"}'
		#send response
		response=requests.post('https://api.storj.io/buckets',headers=headers,data=data,auth=(username,hash_password)).json()
		flash(response)
		return render_template('create-bucket.html')
	else:
		flash("Create a new Bucket")
		return render_template('create-bucket.html')

@app.route('/get-bucket/',methods=['GET','POST'])
def get_bucket():
	if request.method == 'POST':
		username=request.form.get('email')
		password=request.form.get('password')
		#key=request.form.get('ecdsa-key')
		#hash password
		hash_object = hashlib.sha256(password)
		hash_password = hash_object.hexdigest()
		response = requests.get('https://api.storj.io/buckets', headers=headers, auth=(username, hash_password)).json()
		flash(response)
		
		return render_template('get-bucket.html')

	else:
		flash("Get Your List of Buckets")
		return render_template('get-bucket.html')


@app.route('/get-frame/',methods=['GET','POST'])
def get_frame():
	if request.method == 'POST':
		username=request.form.get('email')
		password=request.form.get('password')
		#key=request.form.get('ecdsa-key')
		#hash password
		hash_object = hashlib.sha256(password)
		hash_password = hash_object.hexdigest()
		response = requests.get('https://api.storj.io/frames', headers=headers, auth=(username, hash_password)).json()
		flash(response)
		
		return render_template('get-frames.html')

	else:
		flash("Get Your List of Buckets")
		return render_template('get-frames.html')

@app.route('/get-frameshard/',methods=['GET','POST'])
def get_frameshard():
	if request.method == 'POST':
		username=request.form.get('email')
		password=request.form.get('password')
		#key=request.form.get('ecdsa-key')
		#hash password
		hash_object = hashlib.sha256(password)
		hash_password = hash_object.hexdigest()
		response = requests.get('https://api.storj.io/frames/5a4a46c39f02e60001d135d6', headers=headers, auth=(username, hash_password)).json()
		flash(response)
		
		return render_template('get-framesshard.html')

	else:
		flash("Get Your List of Buckets")
		return render_template('get-framesshard.html')

@app.route('/get-contract/',methods=['GET','POST'])
def get_contract():
	if request.method == 'POST':
		username=request.form.get('email')
		password=request.form.get('password')
		#key=request.form.get('ecdsa-key')
		#hash password
		hash_object = hashlib.sha256(password)
		hash_password = hash_object.hexdigest()
		challenge= os.urandom(32)
		'''data={
  			"hash": "c317e457ffe78d3cbcd624306674d0ac0777d3808b77b004681c8e6bb7e72ab6",
  			"size": 440677,
  			"index": 0,
 			"challenges": [
    "2128bc38ed5140bb9ba8ddac16183eecc4c9ef63b0cd46b30f49b578737a7a52"
  ],'''
		'''data={
			  "frame": "5a4a46c39f02e60001d135d6",
			  "mimetype": "image/png",
			  "filename": "image.png",
			  "hmac": {
			    "type": "sha256",
			    "value": "c317e457ffe78d3cbcd624306674d0ac0777d3808b77b004681c8e6bb7e72ab6"
			  }
			  buckets/1c9985eca672956f1ce7632e/files
			}'''		  
			
		response = requests.get('https://api.storj.io/frames/5a4a46c39f02e60001d135d6', headers=headers, auth=(username, hash_password)).json()
		flash(response)
		
		return render_template('get-contract.html')

	else:
		flash("Get Your List of Buckets")
		return render_template('get-contract.html')

@app.route('/get-files/',methods=['GET','POST'])
def get_files():
	if request.method == 'POST':
		username=request.form.get('email')
		password=request.form.get('password')
		#key=request.form.get('ecdsa-key')
		#hash password
		hash_object = hashlib.sha256(password)
		hash_password = hash_object.hexdigest() 
			
		response = requests.get('https://api.storj.io/buckets/b843c2c81af56f717558ae2d/files', headers=headers, auth=(username, hash_password)).json()
		flash(response)
		
		return render_template('get-contract.html')

	else:
		flash("Get Your List of files")
		return render_template('get-contract.html')

@app.route('/download-files/',methods=['GET','POST'])
def download_files():
	if request.method == 'POST':
		username=request.form.get('email')
		password=request.form.get('password')
		#key=request.form.get('ecdsa-key')
		#hash password
		hash_object = hashlib.sha256(password)
		hash_password = hash_object.hexdigest() 
			
		response = requests.get('https://api.storj.io/buckets/b843c2c81af56f717558ae2d/files/74cafc4907d9e81a53f1ae4c', headers=headers, auth=(username, hash_password)).json()
		flash(response)
		
		return render_template('get-contract.html')

	else:
		flash("Get Your List of files")
		return render_template('get-contract.html')

@app.route('/new/',methods=['GET','POST'])
def new():
	if request.method == 'POST':
		username=request.form.get('email')
		password=request.form.get('password')
		#key=request.form.get('ecdsa-key')
		#hash password
		hash_object = hashlib.sha256(password)
		hash_password = hash_object.hexdigest() 
			
		redirect('https://api.storj.io/b4d60d0cfc92b051c41f934be33a27cc39bd4b6a')
	
	else:
		flash("Get Your List of files")
		return render_template('get-contract.html')



if __name__ == '__main__':
	app.secret_key = 'some secret key'
	app.run(debug=True)




