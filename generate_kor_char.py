# #-*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import random
from datetime import datetime
import os



def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

red = (0, 0, 255)
black = (0, 0, 0)

for e in range(300):
    img = cv2.imread('/home/psj/Desktop/license_bg.jpg', cv2.IMREAD_COLOR)
    overlay = img.copy()
    height, width, p = img.shape
    aspect_ratio = 640 /float(width)
    dsize = (int(width*aspect_ratio), int(img.shape[0] * aspect_ratio))
    img = cv2.resize(img, dsize)


    font_filepath = "./data/fonts_kor/batang.ttc" #license 때
    # font_filepath = "./data/fonts_kor/NanumGothic.ttf" # 면허증
    # font_filepath = "./data/fonts_kor/malgunsl.ttf"  # A, B,C,D,E,F,G,H..
    # font_filepath = "./data/fonts_kor/malgunbd.ttf"


    # font_size = 20
    font_size = random.randint(11,16)

    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype(font_filepath, font_size)

    # xy = (40, 20)
    text = "DriversLicense"
    seed_x = random.randint(1, dsize[0]-int(font.getsize(text)[0])) #dsize[0] is width
    # seed_x = random.randint(310, dsize[0] - int(font.getsize(text)[0]))  # dsize[0] is width
    seed_y = random.randint(1, dsize[1]-int(font.getsize(text)[1])) # dsize[0] is height
    xy = (seed_x,seed_y)

    draw.text(xy, text, font=font, fill=black)

    save_path = "./generated_img/"
    save_name = (datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f'))
    save_img_name = save_path+'images/'+save_name+'.jpg'
    img_pil.save(save_img_name)

    i = 0
    for i, char in enumerate(text):
        right, bottom = font.getsize(text[:i + 1])
        width, height = font.getmask(char).size
        right += xy[0]
        bottom += xy[1]
        top = bottom - height
        left = right - width

        # draw.rectangle((left, top, right, bottom), None, "#f00")

        crop_img = img_pil.crop((left-1, top-2, right+1, bottom+2))  # for char
        # crop_img = img_pil.crop((left - 1, top - font_size, right + 1, bottom + font_size)) # for background

        print(save_path+save_name+str(i)+'_'+char+'.jpg')
        if char != " ":
            crop_img.save(save_path+'characters/'+save_name+str(i)+'_'+char+'.jpg')
            ch_label_bbx_file = save_path+'labels/'+save_name+'.txt'

            if os.path.isfile(ch_label_bbx_file):
                f1 = open(ch_label_bbx_file, 'a')
                f1.write(
                    char + "\t" + str(left-1) + "," + str(top-2) + "," + str(right+1) + "," + str(bottom+2) + "\n")
                f1.close()

            else:
                f1 = open(ch_label_bbx_file, 'w')
                f1.write(
                    char + "\t" + str(left-1) + "," + str(top-2) + "," + str(right+1) + "," + str(bottom+2)+ "\n")
                f1.close()

            ########### for yolo format
            ch_label_bbx_file_yolo = save_path + 'ch_labels_yolo/' + save_name + '.txt'
            if os.path.isfile(ch_label_bbx_file_yolo):
                char = str(0)
                f1 = open(ch_label_bbx_file_yolo, 'a')
                b = (left-1, right+1, top-2, bottom+2)
                bb = convert((dsize[0], dsize[1]), b)
                f1.write(char + "\t" + str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + "\n")
                f1.close()
            else:
                char = str(0)
                f1 = open(ch_label_bbx_file_yolo, 'w')
                b = (left - 1, right + 1, top - 2, bottom + 2)
                bb = convert((dsize[0], dsize[1]), b)
                f1.write(char + "\t" + str(bb[0]) + " " + str(bb[1]) + " " + str(bb[2]) + " " + str(bb[3]) + "\n")
                f1.close()
        else:
            crop_img.save(save_path + 'characters/' + save_name + str(i) + '.jpg')
            ch_label_bbx_file = save_path + 'labels/' + save_name + '.txt'

            if os.path.isfile(ch_label_bbx_file):
                f1 = open(ch_label_bbx_file, 'a')
                f1.write(
                    char + "\t" + str(left - 1) + "," + str(top - 2) + "," + str(right + 1) + "," + str(
                        bottom + 2) + "\n")
                f1.close()

            else:
                f1 = open(ch_label_bbx_file, 'w')
                f1.write(
                    char + "\t" + str(left - 1) + "," + str(top - 2) + "," + str(right + 1) + "," + str(
                        bottom + 2) + "\n")
                f1.close()

    # img = np.array(img_pil)
    # # show
    # cv2.imshow('dst', img)
    # # Destroy
    # cv2.waitKey()
    # cv2.destroyAllWindows()
