from formatando_ips import Format
from conversoes import Converter
from host import Host
class CalculoIPV4:
    def __init__(self,ip, pre=0,mask =0):
        self._ip = ip
        self._pre = pre
        self._mask =  mask
    @property    #será usado para retornar o ip
    def ip(self):
        return self._ip

    @property  # será usado para retornar o prefixo
    def pre(self):
        if not self._pre==0:
            return self._pre
        else:
             return Converter.return_prefixo(self.mask)
    @property
    def mask(self):
        if not self._mask==0:
            return self._mask

        else:
            return self.maskara()

    def maskara(self): #retorna a mascara de subrede
       mascara = Converter.return_mascara_sub__rede(Converter.mask_for_bin(self._ip,self._pre))
       return mascara

    def quantidade_host(self):
        return Host.calc_hosts(self._ip,self._pre)


