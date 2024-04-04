import os

#Функция для более удобного вызова файлов в папке и пути до него
#PathFor должен быть до ListFor

def PathFor(diName): #diName обязательно вводить в "кавычках" пример: ListFor('Rats')
    dName=str('/')+str(diName)
    a = os.getcwd()+str(dName)
    if os.path.exists(a)==True:
#        os.chdir(a)
        return a



#если что-то не будет работать хотя должно из дериктории 412Sel возможно дело в том что дериктория выбрана как основная в этой функции
def ListFor(diName): #diName обязательно вводить в "кавычках" пример: ListFor('Rats')
    dName=str('/')+str(diName)
    a = os.getcwd()+str(dName)
    save=os.getcwd()
    if os.path.exists(a)==True:
        os.chdir(a)
        r=os.listdir(os.getcwd())
        os.chdir(save)
        return(r)
