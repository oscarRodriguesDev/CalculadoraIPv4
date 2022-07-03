from formatando_ips import Format
from conversoes import Converter
from host import Host
""" modulo calculo_redes_ipv4.py:
Este modulo preve as ferramentas necessarias para que possamos realizar todos os calculo de nossa rede ipv4
"""
class CalculoIPV4:
    """Classe CalculoIPV4:
    esta classe prevê as funcionalidades necessarias para o calculo de redes ipv4, necessario dizer que poderemos tanto
    usar o prefixo da rede quanto poderemos usar a propria mascara de subrede, não alterando em nada o funcionamento
    interno da classe
    """
    def __init__(self,ip, pre=0,mask =0):
        """ Metodo Init:
        :param: ip
        :type: string
        :param: pre
        :type: int
        :param:mask
        :type: string
        O parametro pre e mask são opcionais, mas em um deles sempre deverá ser usado,caso contrario
        teremos um erro
        """
        self._ip = ip
        self._pre = pre
        self._mask =  mask
    @property    #será usado para retornar o ip
    def ip(self):
        """get do parametro ip
        :return:ip
        :type: string
        """
        return self._ip

    @property  # será usado para retornar o prefixo
    def pre(self):
        """ get do parametro pre
        :return pre
        :type: int
        Caso tenhamos informado o valor do prefixo, essa função apenas retorna o informado, mas caso contrario
        a função retorna o calculo do prefixo atraves do modulo de conversões
        """
        if not self._pre==0:
            return self._pre
        else:
             return Converter.return_prefixo(self.mask)
    @property
    def mask(self):
        """ get do parametro mask;
        :return: mask
        :type: string
        Caso o parametro de mascara não tenha sido informado este get retorna o valor do calculo da mascara
        que é realizado nessa mesma classe
        """
        if not self._mask==0:
            return self._mask

        else:
            return self.maskara()

    def quantidade_host(self):
        """ Função quantidade_host:
        retorna a quantidade de hosts possiveis para determinada rede
        """
        return Host.calc_hosts(self._ip,self._pre)

    def broadcast(self):
        """ função broadcast:
        retorna o endereço broadcast da rede
        """
        return Host.calc_broadcast(self._ip,self._pre)

    def ip_da_rede(self):
        """ função ip_da_rede
        retorna o primeiro ip da rede
        """
        return Host.firs_ip(self._ip,self._pre)

    def maskara(self):
       mascara = Converter.return_mascara_sub_rede(Converter.mask_for_bin(self._ip, self._pre))
       """ Retorna o a mascara de subred da rede que estamos realizando o calculo sobre ela"""
       return mascara[0:4]


