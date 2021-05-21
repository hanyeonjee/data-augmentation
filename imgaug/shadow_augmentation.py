import cv2
import numpy as np
import random
from scipy.stats import norm
import random
import os


PREFIX_BG = "/home/work/trainsets/v01_multi_bottom_origin/"
SAVE_PREFIX ="/home/work/trainsets/v03_multi_bottom_shadow/"

bg_files = os.listdir(PREFIX_BG)

### shadow vertical #####
# for idx, val in enumerate(bg_files):
#     print("vertical  >> ",idx,"/", len(bg_files))
#     try:
#         img = cv2.imread(PREFIX_BG+val)
#         img2 = cv2.imread(PREFIX_BG+val)
#         blk = np.zeros(img2.shape, np.uint8)

#         start_x = random.randint(0,img.shape[1])
#         width = random.randint(8,15)

#         # Draw rectangles
#         # rectangle (x1,y1), (x2,y2)
#         black = cv2.rectangle(img2, (start_x, 0), (start_x+width, img.shape[0]), (0, 0, 0), cv2.FILLED)

#         out = cv2.addWeighted(img, 0.5, black, 0.5, 0)

#         saved_name = SAVE_PREFIX+val[:-4]+"_shadow1.jpg"
#         cv2.imwrite(saved_name, out)
        
#     except:    
#         print('except.')
#         continue
    

# #### shadow horizen - top ###
# for idx, val in enumerate(bg_files):
#     print("horizen  >> ",idx,"/", len(bg_files))
#     try:
#         img = cv2.imread(PREFIX_BG+val)
#         img3 = cv2.imread(PREFIX_BG+val)
#         horizen_blk = np.zeros(img3.shape, np.uint8)

#         # start_x = random.randint(0,img.shape[1])
# #         height = random.randint(13,17) #single 
#         height = random.randint(5,7) #multi 
#         alpha = random.uniform(0.5,0.9)

#         # Draw rectangles
#         # rectangle (x1,y1), (x2,y2)
#         horizen_black = cv2.rectangle(img3, (0, 0), (img3.shape[1], height), (0, 0, 0), cv2.FILLED)
    
#         out = cv2.addWeighted(img, 0.4, horizen_black, alpha, 0)

          
#         saved_name = SAVE_PREFIX+val[:-4]+"_shadow.jpg"
#         print("saved_name :", saved_name)
#         cv2.imwrite(saved_name, out)
        
#     except:    
#         print('except.')
#         continue

#### shadow horizen - bottom ###
for idx, val in enumerate(bg_files):
    print("horizen  >> ",idx,"/", len(bg_files))
    try:
        img = cv2.imread(PREFIX_BG+val)
        img3 = cv2.imread(PREFIX_BG+val)
        horizen_blk = np.zeros(img3.shape, np.uint8)

        # start_x = random.randint(0,img.shape[1])
#         height = random.randint(13,17) #single 
        height = random.randint(5,7) #multi 
        alpha = random.uniform(0.5,0.9)

        # Draw rectangles
        # rectangle (x1,y1), (x2,y2)
        horizen_black = cv2.rectangle(img3, (0, img3.shape[0]), (img3.shape[1], img3.shape[0]-height), (0, 0, 0), cv2.FILLED)
    
        out = cv2.addWeighted(img, 0.4, horizen_black, alpha, 0)

          
        saved_name = SAVE_PREFIX+val[:-4]+"_shadow.jpg"
        print("saved_name :", saved_name)
        cv2.imwrite(saved_name, out)
        
    except:    
        print('except.')
        continue
