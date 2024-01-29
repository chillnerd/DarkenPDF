#!pip install tkinter,PyMuPDF,Pillow
import os, shutil , fitz
from PIL import Image, ImageEnhance
from tkinter.filedialog import askopenfilename

current=os.getcwd()
path1 = str(current)+'/old'
path2 = str(current)+'/new'
file=askopenfilename()
os.mkdir(path1)
os.mkdir(path2)
doc = fitz.open(file)
count=0
for page in doc:  
    pix = page.get_pixmap(dpi=300)
    if count // 10 == 0:
        dir = path1+"/"+"0"+str(count)+".png"
    else:
        dir = path1+"/"+str(count)+".png"
    pix.save(dir)
    count+=1

a=path1
arr = os.listdir(a)
new=path2
for i in range(len(arr)):
    b=a+'/'+arr[i]
    img = Image.open(b)
    img = img.convert("L")
    img = ImageEnhance.Contrast(img).enhance(3)
    img = ImageEnhance.Brightness(img).enhance(0.5)
    newfr=new+'/'+arr[i]
    img.save(newfr)


arr = os.listdir(new)
lst=[]
for i in range(len(arr)):
    a='img_'+str(i)
    b=new+'/'+arr[i]
    temp=Image.open(b)
    a=temp.convert('RGB')
    if i == 0:
        first=a
    else:
        lst.append(a)
dir=current+'/all.pdf'
first.save(dir,save_all=True, append_images=lst)


shutil.rmtree(path1)
shutil.rmtree(path2)