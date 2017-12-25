from PIL import Image, ImageDraw, ImageFont
def addNum(num,filename='1.jpg'):
    img = Image.open(filename)
    w,h = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf',50)
    draw.text((w-55,0),num,fill='red',font=font)#fill可以用rgb模式
    del draw
    img.save("edit.jpg")
    img.show()

if __name__ == '__main__':
    filename = '1.jpg'
    addNum('99',filename)