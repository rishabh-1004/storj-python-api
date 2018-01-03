from flask import Flask, request, jsonify,json


app= Flask(__name__)

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}



@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'application/json':
		response=request.json
		return jsonify(response)


if __name__=='__main__':
	app.run(debug=True)