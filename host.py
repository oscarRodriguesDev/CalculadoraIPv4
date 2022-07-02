from conversoes import Converter
from formatando_ips import Format
class Host:
    # resolução recebendo o /n
    @staticmethod
    def calc_hosts(ip, rd):
        ip_bin = Converter.convert_bin(ip)
        listcomp = [x for x in ip_bin for x in x]
        listtcomp2 = [1 for x in range(rd)]
        v1 = len(listcomp)
        v2 = len(listtcomp2)
        v3 = v1 - v2
        for i in range(v3):
            listtcomp2.append(0)
        return (2 ** v3) - 2

#retorna o ip broadcast da rede
    @staticmethod
    def calc_broadcast(ip,rd):
        lista =[128,64,32,16,8,4,2,1]
        listtcomp2 = [0 for x in range(rd)]
        index =len(listtcomp2)-32
        soma = 0
        for i,x in enumerate(lista,-8):
            if i>=index:
                soma+=x
        ip =  Format.format_ip(ip)
        ip[-1] =  soma
        ip =  str(ip)
        ip = ip.replace(',','.')
        ip =  ip.replace('[','')
        ip = ip.replace(']', '')
        ip =  ip.replace(' ','')
        return ip

#retorna o primeiro ip da rede:
    @staticmethod
    def firs_ip(ip,rd):
        lista = [128, 64, 32, 16, 8, 4, 2, 1]
        listtcomp2 = [0 for x in range(rd)]
        index = len(listtcomp2) - 32
        soma = 0
        for i, x in enumerate(lista, -8):
            if i >= index:
                soma += x
        soma = soma-(soma-1)
        ip = Format.format_ip(ip)
        ip[-1] = soma
        ip = str(ip)
        ip = ip.replace(',', '.')
        ip = ip.replace('[', '')
        ip = ip.replace(']', '')
        ip = ip.replace(' ', '')
        return ip



if __name__=='__main__':
    hosts = Host.calc_hosts('10.20.12.4',26)
    print(hosts)

    broad= Host.calc_broadcast('10.20.12.4',26)
    print(broad)

    first = Host.firs_ip('10.20.12.4',26)
    print(first)