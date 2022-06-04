import qrcode 
from flask import Flask, render_template, request
import os

QR_Generator = Flask(__name__)

picFolder = os.path.join('static','pics')

QR_Generator.config['UPLOAD_FOLDER'] = picFolder

@QR_Generator.route('/')
def index():
	return render_template('UserPage.html')

@QR_Generator.route('/', methods = ['POST'])
def getvalue():
	fileName = ""
	option = int(request.form['formselector'])
	if(option == 1):
		wNumber = request.form['Wnumber']
		cCode = request.form['cCode']
		url = "https://wa.me/"+cCode+wNumber+"?text=Hii"
		fileName = "w" + wNumber + ".jpg"
	elif(option == 2):
		cCode = request.form['cCode']
		phNumber = request.form['PHnumber']
		url = "tel:"+phNumber
		fileName = "p" + phNumber + ".jpg"
	elif(option == 3):
		email = request.form['email']
		url = "mailto:"+email
		fileName = "E"+email + ".jpg"
	qr_img = qrcode.make(url)
	path = "static/pics"
	qr_img.save(f"{path}/"+fileName)

	pic1 = os.path.join(QR_Generator.config['UPLOAD_FOLDER'], fileName)
	return render_template('OutputPage.html', user_image = pic1)


if(__name__ == '__main__'):
	QR_Generator.run(host="0.0.0.0", debug = True)