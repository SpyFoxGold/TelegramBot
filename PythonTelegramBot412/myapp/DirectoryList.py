import os


def AnimalList(): #ВЫДАЁТ СПИСОК ПАПОК В ДИРЕКТИРИИ ANIMALS в которых есть хотя бы лодин файл
    Result=[]
    start= os.getcwd()

    path = os.getcwd() +'/Animals'
    link = os.chdir(path)
    list = os.listdir(link)
    for i in range(0,len(list)):
        check = path+ '/' + list[i]
        if os.listdir(check) != []:
            Result.append(list[i])
    os.chdir(start)
    return Result




def PathFor(diName):#ВЫДАЁТ ПУТь ДО ПАПКИ diName В ПАПКЕ Animal // diNAme писать 'в кавычках'
#    os.chdir("../")
    link = os.getcwd() + '/Animals/' + str(diName)
    return (link)

def ListFor(diName): #ВЫВОДИТ diName обязательно вводить в "кавычках" пример: ListFor('Rats')
    #os.chdir("../")
    a = PathFor(diName)

    save=os.getcwd()
    if os.path.exists(a)==True:
        os.chdir(a)
        r=os.listdir(os.getcwd())
        os.chdir(save)
        return(r)

#print(ListFor('Cats'))

def CreateFolder(Foldername): #Создаёт папку в Animals
    save=os.getcwd()
    link = os.getcwd() + '/Animals/'
    os.chdir(link)
    link += '/' + str(Foldername)
    os.mkdir(link)
    os.chdir(save)
