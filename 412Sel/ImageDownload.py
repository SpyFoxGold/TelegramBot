import requests
import os
import DerictoryList




def ubrat(x):
    A=''
    for i in range(0,len(x)):
        if x[i]!='.':
            A+=x[i]
        else: return(A)

url='https://wdorogu.ru/images/wp-content/uploads/2020/04/s1200-30-1.jpg'
directory="Cats"
def DownloadImg(url,directory): #директория в кавычках
    name=0
    A=DerictoryList.ListFor(str(directory))
    for i in range(0,len(A)):
        A[i]=ubrat(A[i])

    while str(name) in A:
        name+=1

    name=str(name)


    diName=str(directory)
    dName=str('/')+str(diName)
    a = os.getcwd()+str(dName)
    save=os.getcwd()
    if os.path.exists(a)==True:
      os.chdir(a)



    img = requests.get(url)
    img_option=open(name + '.jpg', 'wb')
    img_option.write(img.content)
    img_option.close()

    os.chdir(save)
