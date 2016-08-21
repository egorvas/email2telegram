
from flask import Flask, request

app = Flask(__name__)

@app.route('/email',methods=['POST'])
def email():

	'''

	'''
	print ("email")
	return 'ok'

@app.route('/telegram',methods=['POST'])
def telegram():

	'''
	
	'''
	print ("telegram")
	return 'ok'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)