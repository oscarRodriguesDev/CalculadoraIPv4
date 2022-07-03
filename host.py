from conversoes import Converter
from formatando_ips import Format

"""Modulo host.py:
Este modulo fornece as ferramentas necessarioas para calcular os host, ip primarios, e ip broadcast de uma rede 
ipv4
"""
class Host:
    """Classe Host:
    Esta classe comporta funçõe estaticas destinadas ao calculo de hosts, ip broadcast e ip primario de redes ipv4
    """
    @staticmethod
    def calc_hosts(ip, pre):
        """Função calc_hosts
        Esta função retorna a quantidade de hosts disponiveis para configurar novos dispositivos na rede
        :param: ip
        :type: string
        :param: pre
        :type: int
        :return: qtd_hosts
        :type: int
        """
        ip_bin = Converter.convert_bin(ip)
        listcomp = [x for x in ip_bin for x in x]
        listtcomp2 = [1 for x in range(pre)]
        v1 = len(listcomp)
        v2 = len(listtcomp2)
        v3 = v1 - v2
        for i in range(v3):
            listtcomp2.append(0)
        qtd_hosts= (2 ** v3) - 2
        return qtd_hosts

#retorna o ip broadcast da rede
    @staticmethod
    def calc_broadcast(ip, pre):
        """ função calc_broadcast:
        Esta funçao retorna o ip broadcast da rede que estamos calculando
        :param: ip
        :type: string
        :param: pre
        :type: int
        :return:ip: o ip retornado é resultado do calculo do ip recebido como parametro, modificado
        atraves de metodo de string
        :type: string

        """
        lista =[128,64,32,16,8,4,2,1]
        listtcomp2 = [0 for x in range(pre)]
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


    @staticmethod
    def firs_ip(ip, pre):
        """ função first_ip:
        Esta funçao retorna o primeiro ip da rede que estamos calculando
        :param: ip
        :type: string
        :param: pre
        :type: int
        :return:ip: o ip retornado é resultado do calculo do ip recebido como parametro, modificado
        atraves de metodo de string
        :type: string

        """
        lista = [128, 64, 32, 16, 8, 4, 2, 1]
        listtcomp2 = [0 for x in range(pre)]
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