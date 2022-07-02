# função para converter em binario
from formatando_ips import Format


class Converter:

    @staticmethod
    def convert_bin(ip):
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


# retorna a mascara de subrede convertida em binario
    @staticmethod
    def mask_for_bin(ip, rd):
        lista = []
        lista_2 = []
        contador = 0
        ip_bin = Converter.convert_bin(ip)
        for x_list in ip_bin:
            lista_2 = []
            for y_list in x_list:
                contador += 1
                if contador <= rd:
                    lista_2.append(1)
                else:
                    lista_2.append(0)

            lista.append(lista_2)
            if len(lista[-1])==7:
                lista[-1].append(0)

        return lista

    # convert a mascara binaria em mascara decimal
    @staticmethod
    def return_mascara_sub__rede(masc_bin):
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

#retorna o prefixo da rede

    @staticmethod
    def return_prefixo(mask):
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
