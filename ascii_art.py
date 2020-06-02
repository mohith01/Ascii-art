from PIL import Image
import numpy as np
from colorama import  init,Fore,Back
init(convert=True)
np.set_printoptions(threshold=np.inf)
im = Image.open(r'C:\Users\mohit\Desktop\ascii.jpg')#ENTER YOUR FILENAME
im = im.resize((im.size[0]//4,im.size[1]//4))
print(im.size)
pix_mat=np.asarray(im)
print(pix_mat.shape)
bright_mat=[]
for i in range(pix_mat.shape[0]):#175
	t=[]
	for j in range(pix_mat.shape[1]):#116
              #  for m in pix_mat[i][j]:
               #        if m>=200 or m<=135:
                #                m=255-m
                t.append(0.21*pix_mat[i][j][0]+0.72*pix_mat[i][j][1]+0.07*pix_mat[i][j][2])
	bright_mat.append(t)
bright_mat=np.asarray(bright_mat)
print(bright_mat.shape)
ascii_mat ="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
fin_mat=[]
bright_mat_trans=bright_mat//4
for i in range(bright_mat.shape[0]):
	t=[]
	for j in range(bright_mat.shape[1]):
		t.append(ascii_mat[int(bright_mat_trans[i][j])])
	fin_mat.append(t)
a=bright_mat.shape
print(a)
temp1=''
for k in range(a[0]):
    temp1=''.join(str(l) for l in fin_mat[k])
    
    print(Fore.GREEN+temp1)

