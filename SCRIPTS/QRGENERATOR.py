import qrcode
from PIL import Image
import qrcode.constants

data = input("Enter anything to generate QR code for it:")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="white"
)

img.save("QRcode.png")
img.show()