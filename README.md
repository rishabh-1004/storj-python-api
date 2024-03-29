Storj Api Documentation

The required packages are given in requirement.txt do install those before running

to run the api use python api.py

1. Signup

To call signup we need to send POST request with the following data:

	*email(text)
	*password(palin text)
	*confirm-password(plain text)

Curl command for the same- 

curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/signup -d '{"email":"gokow@muimail.com","password":"qwertyhjkl","confirm_password":"qwertyhjkl"}'

This will return a json response:-

{
  "activated": false, 
  "created": "2018-01-02T14:31:41.503Z", 
  "email": "gokow@muimail.com", 
  "id": "gokow@muimail.com", 
  "isFreeTier": true, 
  "preferences": {
    "dnt": false
  }, 
  "referralPartner": null, 
  "uuid": "dcf59ab1-6cb5-4a56-a4a8-5d089bfcf7e5"
}

and also send an activation email to the user.

2.Add Key

To add a key we need to send POST request with the following data:
	
	*email
	*password
	*new public key

Curl command for the same-

curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/add-key -d '{"email":"gokow@muimail.com","password":"qwertyhjkl","ecdsakey":"04c94e783080619d1d1d3cb091ac38409ee99ed5ccc1c9b761caf31fab48dcf0273cb209b619ef2e69b4271bf8e6d97ea3e7984a08d3f3f71b5d42f3ce3e75b260"}'

This will return a json respose-

{
  "key": "031a259ee122414f57a63bbd6887ee17960e9106b0adcf89a298cdad2108adf4d9",
  "user": "gordon@storj.io"
}

3. GET all public keys

To get display all the keys we need to send authentication details via post

	*email
	*password

Curl command for the same-

curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/get-key -d '{"email":"rishabhrajshrm00@gmail.com","password":"password"}'

this will return a json response-

[
  {
    "id": "04c94e783080619d1d1d3cb091ac38409ee99ed5ccc1c9b761caf31fab48dcf0273cb209b619ef2e69b4271bf8e6d97ea3e7984a08d3f3f71b5d42f3ce3e75b260", 
    "key": "yourkey", 
    "label": "", 
    "user": "rishabhrajshrm00@gmail.com"
  }
]

4. Create Bucket

To create a new bucket we need to send the following via POST request

	*email
	*password
	*ecdsakey
	*bucketname

curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/create-bucket -d '{"email":"rishabhrajshrm00@gmail.com","password":"password","ecdsakey":"key","bucketname":"Test3"}'

and response comes in json form:

{
  "created": "2018-01-02T16:22:31.470Z", 
  "encryptionKey": "", 
  "id": "b843c2c81af56f717558ae2d", 
  "name": "Test3", 
  "pubkeys": [
    "yourkey"
  ], 
  "publicPermissions": [], 
  "status": "Active", 
  "storage": 0, 
  "transfer": 0, 
  "user": "rishabhrajshrm00@gmail.com"
}

5 Get list of bucket

To get the list of bucket you onluy need to send the authentication via post

	*email
	*password

Curl command for this :

curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/get-bucket -d '{"email":"rishabhrajshrm00@gmail.com","password":"password"}'

And response of the following:

	[
	  {
	    "created": "2018-01-01T07:59:18.207Z", 
	    "encryptionKey": "", 
	    "id": "1c9985eca672956f1ce7632e", 
	    "name": "Test Bucket", 
	    "pubkeys": [
	      "your key"
	    ], 
	    "publicPermissions": [], 
	    "status": "Active", 
	    "storage": 0, 
	    "transfer": 0, 
	    "user": "rishabhrajshrm00@gmail.com"
	  }, 
	  {
	    "created": "2018-01-01T08:14:55.284Z", 
	    "encryptionKey": "", 
	    "id": "ded7270c4daef33feeae297e", 
	    "name": "TestBucket2", 
	    "pubkeys": [
	      "your key"
	    ], 
	    "publicPermissions": [], 
	    "status": "Active", 
	    "storage": 0, 
	    "transfer": 0, 
	    "user": "rishabhrajshrm00@gmail.com"
	  }, 
	  {
	    "created": "2018-01-02T16:22:31.470Z", 
	    "encryptionKey": "", 
	    "id": "b843c2c81af56f717558ae2d", 
	    "name": "Test3", 
	    "pubkeys": [
	      "your key"
	    ], 
	    "publicPermissions": [], 
	    "status": "Active", 
	    "storage": 0, 
	    "transfer": 0, 
	    "user": "rishabhrajshrm00@gmail.com"
	  }
	]






