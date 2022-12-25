import qrcode

"""This project will help a user to generate a QR code
for a given url and afterward this QR code can be used to invite the users to a specified link
"""

img = qrcode.make('https://youtu.be/8lrRrmy8SHw')
img.save('myqrcode.png')
img.show()
