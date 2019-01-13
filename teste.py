import platform, os, time

###############################################################constants#######################################################
delaySecond=time.sleep()
MenuText="""
            1)Registrar chamada
            2)Ler Ficheiro
            3)Listar Clientes
            4)Fatura
            5)Terminar
          """
allowPhoneChar=['1','2','3','4','5','6','7','8','9','0','+']
#################################################################################################################################
def isPhoneValid(string):
    for c in string:
        if(c not in allowPhoneChar):return false
    return true

def ClearScreen():
    if(platform.system()=="Windows"): os.system("cls")
    if(platform.system()=="Linux"): os.system("clear")

def safeFileOpen(mode,filePath):
    if mode not in ['r','w','x','a','t','b','r+','w+','x+','a+','t+','b+']:
        return "InvalidOpenMode"
    else:
        try:
            arq=open(mode,filePath)
            return arq
        except IOError as e:
            arq=e.strerror()
            return arq

def RegCall():
    arq=safeFileOpen("arq.txt","a")
    if(arq=="IOError"):
        print("Erro ao abrir o arquivo. Verifique o caminho do mesmo e/ou permissoes no local")
    else:
        
    

def menu():
    ClearScreen()
    op="InvalidOption"
    while(op=="InvalidOption" or op!=5):
        try:    
            op=int(input(MenuText))
            ClearScreen()
            if(op not in list(range(1,6))):
                print("Opcao invalida. Selecione as opcoes disponiveis (1-5)")
                delaySecond(3)
                op="InvalidOption"
            elif(op==1):
                
        except TypeError:
            print("Opcao invalida. Selecione as opcoes disponiveis (1-5)")
            delaySecond(3)
            op="InvalidOption"
    return op
#op=0
#while(op!=5):
 #   if(op==1)
