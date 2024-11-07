import pyqrcode #pip install PyQRCode

url = input("Enter the URL to generate QR Code: \n ")

QR = pyqrcode.create(url)

QR.png("web.png", scale=8)