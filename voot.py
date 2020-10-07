#import pyautogui,time
import math
from PIL import Image
import PIL.ImageOps
from PIL import ImageFilter
def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)
from PIL import Image

import numpy as np
 #tttttttt
def dodgej(front,back):
    # The formula comes from http://www.adobe.com/devnet/pdf/pdfs/blend_modes.pdf
    result=back*256.0/(256.0-front) 
    result[result>255]=255
    result[front==255]=255
    return result.astype('uint8')
def dodge2(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')
def dodge(image, mask):
    # determine the shape of the input image
    width,height = image.shape[:2]

    # prepare output argument with same size as image
    blend = np.zeros((width,height), np.uint8)

    for col in range(width):
        for row in range(height):

            # shift image pixel value by 8 bits
            # divide by the inverse of the mask
            #print((255.-mask))
            tmp = (image[col,row] << 8) / (255.-mask[col,row])

            # make sure resulting value stays within bounds
            #print(tmp)
            if tmp > 255:
                tmp = 255
            blend[col,row] = tmp
    print (blend)
    return blend
#333333333
col = Image.open("44.jpg") # open colour image
gray = col.convert('L')
#gray.show()
#bw = gray.point(lambda x: 0 if x<128 else 255, '1')
#bw.save("result_bw.png")#it tell how much area is blank
#bw = col.convert('L')
#bw.save('new.png')
inverted_image = PIL.ImageOps.invert(gray)
#inverted_image.save('new_name.png')
blur=inverted_image.filter(ImageFilter.BLUR)
image2 = np.asarray(gray)
image1=np.asarray(blur)
print(image1)
#result=dodge(front=image1, back=image2)
result=dodge(image1, image2)

#result = Image.fromarray(result, 'RGB')
#result = Image.fromarray(result, 'RGB')
img = Image.new( 'RGB', (col.size[0],col.size[1]), "white")
pixels = img.load()
for i in range(col.size[0]):    # for every pixel:
    #variables
    for j in range(col.size[1]):
        pixels[i, j] = (result[j,i],result[j,i],result[j,i])
img = img.convert('L')
img = img.point(lambda x: 0 if x<250 else 255, '1')
img.save('bodder.png')
img.show()
input('yo')


img1 = Image.open('44.jpg')    
img = Image.new( 'RGB', (img1.size[0],img1.size[1]), "white") # create a new black image

pixels = img.load() # create the pixel map
for i in range(img.size[0]):    # for every pixel:
    #variables
    ThrushHold=5
    PresentColor=(0,0,0)
    
    for j in range(img.size[1]):
        NowColor=img1.getpixel((i,j))
        if tell_color_dis(NowColor,PresentColor,ThrushHold)!=True:
            pixels[i, j] = (0,0,0)
            PresentColor=NowColor

#img.show()   
img2 = Image.new( 'RGB', (img.size[0],img.size[1]), "white") # create a new black image            
pixels = img2.load()
for i in range(img.size[0]):    # for every pixel:
    #variables
    flag=0
    skip=''
    for j in range(img.size[1]):
        if skip!=j:
            skip=''
            NowColor=img.getpixel((i,j))
            if NowColor==(0,0,0):
                if flag==0:
                    pixels[i, j] = (0,0,0)
                    flag=1
                else:
                    if j!=img2.size[1]-1:
                        if img.getpixel((i,j+1))==(0,0,0):
                            pixels[i, j] = (0,0,0)
                            flag=0
                            skip=j+1
        else:
            pixels[i, j] = (0,0,0)



img2.show()

input('img2 done')
img3 = Image.new( 'RGB', (img2.size[0],img2.size[1]), "white") # create a new black image            
pixelss = img3.load()
for i in range(3,img2.size[0]-3):    # for every pixel:
    #variables
    for j in range(3,img2.size[1]-3):
        g=(i-1,j-1)
        blackcount=0
        for ii in range(3):
            for jj in range(3):
                if img2.getpixel((g[0]+ii,g[1]+jj))==(0,0,0):
                    blackcount+=1
        if blackcount>=4:
            pixelss[i, j] = (0,0,0)
            


img3.show()
#img.save("comp.png")
