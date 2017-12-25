import random, string, PIL.Image, PIL.ImageDraw, PIL.ImageFont, PIL.ImageFilter
def create():
    width,height = size = (64*4,64)
    wenzi = [*string.ascii_uppercase, *string.ascii_lowercase, string.digits]#返回字母和数字
    img = PIL.Image.new('RGB', size, random_color(0))#RGB要大写
    font = PIL.ImageFont.truetype('arial.ttf', height-10)#创建font对象
    draw = PIL.ImageDraw.Draw(img)#创建draw对象
    for x in range(width):#全像素随机
        for y in range(height):
            draw.point((x,y),fill=random_color(1))
    for i in range(4):#四个字符
        draw.text((int(width/4)*i+15,0),random.choice(wenzi),random_color(0),font)
    img = img.filter(PIL.ImageFilter.BLUR)
    img.save("验证码.jpg")
    # print(wenzi)

def random_color(case):
    if case == 0:
        return (random.randint(1,225), random.randint(1,225), random.randint(1,225))
    else:
        return (random.randint(100,200), random.randint(100,200), random.randint(100,200))
    pass

if __name__ == '__main__':
    create()