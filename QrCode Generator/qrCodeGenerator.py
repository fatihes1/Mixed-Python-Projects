######################################
#### QR- CODE GENERATOR WITH PYTHON
#### 
#### First install 2 modules in CMD
#### -> qrcode -> pip install qrcode
#### -> image -> pip install image
####
######################################

import qrcode
import image

qr = qrcode.QRCode(
    version= 15, # means the version of the qr code high the number bigger the code image and complicated pictuıre
    box_size= 10, # size of the box where qe code will be displayed
    border= 5 # it is the white part of the image -- border in all 4 sides with white color
)

data = "https://fatihes1.github.io/"
# as I have given the path of my resume website 
# if you do not want to redirect and create for normal text that write text in the quotes

qr.add_data(data)
qr.make(fit = True)

#  The following lines of code will create your qr-code and save it in the same directory as your '.py' file 
image = qr.make_image(fill = 'black', back_color = 'white')
image.save("youtube_qr.png")