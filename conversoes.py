"""
Modulo Conversões:
reune diversas funçoes que possibilitam o calculo das redes ipv4

"""
from formatando_ips import Format
class Converter:
    """Classe Converter:
    Esta classe é responsavel por fazer a conversão de valores de decimal para binario e de binario para
    decimal quando necessário, todos as funções desta classe são estaticas
    """

    @staticmethod
    def convert_bin(ip):
        """Função convert_bin
        esta função converte o numero ip recebido como paramentro em formato binario, para que as operações necessárias
        necessarias para o calculo de redes ipv4 sejam realizados sem dificuldade por qualquer outra classe:
        :param: ip
        :type: String
        :return:lista
        :type: int
        """
        binario = []
        tabela = [128, 64, 32, 16, 8, 4, 2, 1]
        ip = Format.format_ip(ip)
        for x in ip:
            aux = 0
            lista = []
            for num in tabela:
                if num <= x:
                    aux += num
                    if aux > x:
                        aux -= num
                        lista.append(0)
                    else:
                        lista.append(1)
                if num > x:
                    lista.append(0)
            binario.append(lista)
        return binario



    @staticmethod
    def mask_for_bin(ip, pre):
        """ Função mask_for_bin
        Esta função tem a finalidade de calcular a mascara de subrede em numeros binarios
        :param pre:
        :type: int
        :param ip
        :type:int
        :return: lista
        :type: int
        """
        lista = []
        lista_2 = []
        contador = 0
        ip_bin = Converter.convert_bin(ip)
        for x_list in ip_bin:
            lista_2 = []
            for y_list in x_list:
                contador += 1
                if contador <=pre:
                    lista_2.append(1)
                else:
                    lista_2.append(0)

            lista.append(lista_2)
            if len(lista[-1])==7:
                lista[-1].append(0)

        return lista


    @staticmethod
    def return_mascara_sub_rede(masc_bin):
        """Função return_mascara_sub_red
        Esta função retorna a mascara de subrede em valores decimais em uma lista de inteiros
        :param: masc_bin
        :type: list
        :return: lista
        :type: list(int)
        """
        conv = [128, 64, 32, 16, 8, 4, 2, 1]
        lista = []
        soma = 0
        for v in masc_bin:
            soma = 0
            for x in v:
                soma += x
            if soma == 8:
                lista.append(255)

            elif soma < 8:
                soma = 0
                for i in range(7):
                    if v[i] == 1:
                        soma += conv[i]
                lista.append(soma)
        return lista



    @staticmethod
    def return_prefixo(mask):
        """Função return_prefixo
        Esta função retorna o prefixo da rede, atraves da mascara passada como paramentro
        :param: mask
        :type: list(int)
        :return: soma
        :type: int
        """
        soma=0
        var = 0
        lista = [128,64,32,16,8,4,2,1]
        mask =Format.format_ip(mask)
        for x in mask:
            if x==255:
                soma+=8
            else:
                for y in lista:
                    var+=y
                    if var<=x:
                        soma+=1
                    else:
                        return soma





if __name__ == '__main__':
    c = Converter.convert_bin('10.20.12.45')
    print(c)
    c1 = Converter.convert_bin('10.20.12.4')
    print(c1)

    m = Converter.mask_for_bin('123.123.123.6',26)
    print(m)

    g = Converter.return_prefixo('255.255.255.192')
    print(g)
