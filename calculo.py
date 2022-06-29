
#ip teste:10.20.12.45
lista_ip = []

def agrupadora(ip):
    provisoria = []

    #repartir esse ip

    for x in ip:
        if x!= '.':
            provisoria.append(x)
        else:
            lista_ip.append(provisoria)
            provisoria=[]
    ii = [int((x+y)) for x,y in lista_ip] #lista com os valores separados
    return ii


#função para converter em binario
def convert_bin(ip):
    ip+='.00' #descobrir o porque desse problema
    binario = []
    tabela = [128, 64, 32, 16, 8, 4, 2, 1]
    ip = agrupadora(ip)
    print(f' agrupadora retorna o ip: {ip}')
    for x in ip:
       aux =0
       lista = []
       for num in tabela:

           if num < x:
               aux+=num
               if aux>x:
                   aux-=num
                   lista.append(0)
               else:
                   lista.append(1)
           if num>x:
               lista.append(0)

       binario.append(lista)

    print(binario)
    return binario

def subred_1(ip,rd):
    ip_bin =convert_bin(ip)
    listcomp = [x for x in ip_bin for x in x]
    print(listcomp)





#agrupadora('') #transforma minha string em uma lista das partes do ip do tipo int
#convert_bin('10.20.12.45') #transforma o ip em uma lista de lista onde cada parte do meu ip é convertido em binario

subred_1('10.20.12.45',26)