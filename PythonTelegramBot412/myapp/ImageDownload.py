import requests
import os
from myapp import DirectoryList




def ubrat(x):
    A=''
    for i in range(0,len(x)):
        if x[i]!='.':
            A+=x[i]
        else: return(A)

#url='https://avatars.dzeninfra.ru/get-zen_doc/4445366/pub_6143b06811c2f753fabe138b_6143b11325b27052c65d0731/scale_1200'
#directory="Cats"

def DownloadImg(url,directory):
    name = 0
    A=DirectoryList.ListFor(str(directory))
    for i in range(0,len(A)):
        A[i]=ubrat(A[i])
    while str(name) in A: #даём новое имя
        name+=1
    name=str(name)

    a = DirectoryList.PathFor(directory)
    save=os.getcwd()
    if os.path.exists(a)==True:
        os.chdir(a)
    img = requests.get(url)
    img_option=open(name + '.jpg', 'wb')
    img_option.write(img.content)
    img_option.close()

    os.chdir(save)
