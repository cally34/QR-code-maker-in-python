import qrcode
import image

def listen():
    user_input = input("Enter the URL: ")

if True:
    data = input("Enter the URL: ")
    filename = input("Enter Filename: ")

qr = qrcode.QRCode(
    version = 15,
    box_size = 10, 
    border = 5, 

)


qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

img.save(filename + ".png") 