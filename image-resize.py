import os
import PIL
from PIL import Image
from datetime import datetime

i=6801
for image_file_name in os.listdir('C:\\Users\\SUJAN HASAN\\Desktop\\Demo\\'):
    s=str(i)
    if image_file_name.endswith(".jpg"):
        now = "img_9_"+s
        im = Image.open('C:\\Users\\SUJAN HASAN\\Desktop\\Demo\\'+image_file_name)
        new_width  = 32
        new_height = 32
        im = im.resize((new_width, new_height), Image.ANTIALIAS)
        im.save('C:\\Users\\SUJAN HASAN\\Desktop\\resize\\' + now + '.jpg')
        i = i + 1

print("Done")