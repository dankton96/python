import easygui
numList=['0','1','2','3','4','5','6','7','8','9']
letterList=['a','b','ç','c','d','e','f','g','i','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
FilePath=easygui.fileopenbox("Selecione o arquivo a ser manipulado:")
#print(FilePath)
file=open(FilePath,'r+')
sub=[]
for sc in file:
    sub.append(sc)
text=''
for i in sub:
    text+=str(i)
print(text)
set4=[text[i:i+4] for i in text[:-3]]
print(set4)
