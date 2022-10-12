import qrcode

data='Hello World!'#data that you want to store in qrcode.
address='D:\python/projects/QR code generator/qrcode.png' #where do you want to save the  generated qrcode.

img= qrcode.make(data)
img.save(address)
