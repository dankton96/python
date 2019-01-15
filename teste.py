import platform, os, time

###############################################################constants#######################################################
MenuText="""
            1)Registrar chamada
            2)Ler Ficheiro
            3)Listar Clientes
            4)Fatura
            5)Terminar
          """
allowPhoneChar=['1','2','3','4','5','6','7','8','9','0','+']
#################################################################################################################################
def ClearScreen():
    if(platform.system()=="Windows"): os.system("cls")
    if(platform.system()=="Linux"): os.system("clear")

def isPhoneValid(string):
    if(string[0]=='+'):
        if(len(string)<4):return False
    else:
        if(len(string)<3):return False
    if(string[0] not in allowPhoneChar):return False
    for c in string[1:]:
        if(c not in allowPhoneChar[:-1]):return False
    return True

def safeFileOpen(filePath,mode):
    if mode not in ['r','w','x','a','t','b','r+','w+','x+','a+','t+','b+']:
        return "InvalidOpenMode"
    else:
        try:
            arq=open(mode,filePath)
            return arq
        except IOError as e:
            arq="IOError"
            return arq

def inputPhone(message):
    var=input(message)
    if(isPhoneValid(var)): return var
    else: return "InvalidPhone"

def RegCall():
    arq=safeFileOpen("arq.txt","a")
    if(arq=="IOError"):
        print("Erro ao abrir o arquivo. Verifique o caminho do mesmo e/ou permissoes no local")
    else:
        while(True):
            ClearScreen()
            while(True):
                if(SourcePhone=="InvalidPhone"):
                    SourcePhone=inputPhone("Telefone de origem invalido. Insira um numero valido:")
                else:
                    SourcePhone=inputPhone("Telefone de origem: ")
                if(SourcePhone!="InvalidPhone"):break
            while(True):
                if(DestPhone=="InvalidPhone"):
                    DestPhone=inputPhone("Telefone de destino invalido. Insira um numero valido:")
                else:
                    DestPhone=inputPhone("Telefone de destino: ")
                if(DestPhone!="InvalidPhone"):break
            try:
                while(True):
                    if(CallTime=="TypeError"):
                        CallTime=int(input("Duracao da chamada invalida. Informe um tempo em segundos e maior do que 0:"))
                    else:                    
                        CallTime=int(input("Duracao da chamada em segundos: "))
                    if(CallTime<=0):CallTime="TypeError"
                    if(CallTime!="TypeError"):
                        arq.write(SourcePhone,"\t",DestPhone,"\t",CallTime)
                        arq.close()
                        break
            except TypeError:
                CallTime="TypeError"

def ReadCallReg(fileName):
	arq=safeFileOpen(fileName,'r')
	if(arq=="IOError"): 
        print("Erro ao abrir o arquivo. Verifique o caminho e nome do mesmo e/ou permissoes no local")
        return "IOError"
	else:
		reg=[]
		for line in arq:
			lineData=line.split()
			reg.append(lineData)
		arq.close()
		return reg

def listClients(r):
    clientsList=dict()
    for t in r:
        if(t[0] not in clientList.keys()): clientList[t[0]]=0
    return clientList.keys()


def menu():
    ClearScreen()
    op="InvalidOption"
    while(op=="InvalidOption" or op!=5):
        try:    
            op=int(input(MenuText))
            ClearScreen()
            if(op not in list(range(1,6))):
                print("Opcao invalida. Selecione as opcoes disponiveis (1-5)")
                time.sleep(3)
                op="InvalidOption"
            elif(op==1):
                RegCall()
            elif(op==2):
                FileStr=input("Informe o nome do arquivo a ser lido:")
                Reg=ReadCallReg(FileStr)
            elif(op==3):
                if(len(Reg)==0):print("Nenhum cliente cadastrado")
                else:
                    print(listClients(Reg))
            elif(op==4):
                
            return op
                    
        except TypeError:
            print("Opcao invalida. Selecione as opcoes disponiveis (1-5)")
            time.sleep(3)
            op="InvalidOption"
while(True):
    sel=menu()
    if(sel==5):break
