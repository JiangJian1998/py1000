from PIL import Image
import os, imghdr
def photo_resize(path):
    pw,ph = (1136, 640)
    f_list = os.listdir(path)
    for each in f_list:
        f_path = path+'\\'+each
        if imghdr.what(f_path):
            img = Image.open(f_path)
            w,h = img.size
            if(w>pw):
                img = img.resize((int(pw), int(h*(pw/w))))
                w, h = img.size
            if(h>ph):
                img = img.resize((int(w*(ph/h)), int(ph)))
            img.save(f_path)
    del img

if __name__ == "__main__":
    photo_resize(".\dir")