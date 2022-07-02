
class Format:
    """ Classe Format
Esta classe é responsavel por receber o endereço ip e formatá-lo de forma que possa ser utilizado
para os calculos de redes IPv4
    """
    @staticmethod
    def format_ip(ip):
        """ format_ip
        Retorna o ip fornecido devidamente formatado para que calculos posteriores sejam realizados
        o valor retornadosera uma lista de inteiros onde cada elemento é um bloco do meu endereço ip
        :param: ip
        :type: string
        :return: list(int)
        """
        ip= ip+'.'
        parada=0
        inicio=0
        bloco = ''
        lista=[]
        for b in ip:
            parada+=1
            if b=='.':
                bloco=ip[inicio:parada-1]
                lista.append(int(bloco))
                inicio = parada
        return lista


if __name__=='__main__':
    c = Format.format_ip('10.20.12.40')
    print(c)

