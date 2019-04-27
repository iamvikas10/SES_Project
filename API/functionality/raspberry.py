# -*- coding: utf-8 -*-

import base64,cv2

img = 'gg.jpg'
def encode_image(img):
    image = open(img,'rb')
    img = image.read()
    #encodedImg = image.encode();
    x= base64.b64encode(img);
    return str(x)
    #with open('demo.txt','w') as f:
        #f.write(x)

text = encode_image(img)
def decode_image(text):
    imageString = base64.encodestring(bytes(text,'utf8'))
    return imageString

img = decode_image(text)