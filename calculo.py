
from conversoes import Converter
from host import Host
endereço_ip = '10.20.12.45'
h = 26
#ip em binario
bin_ip =Converter.convert_bin(endereço_ip)
print(f'ip em binario: {bin_ip}')
#mascara em binario
msk_bin =  Converter.mask_for_bin(endereço_ip,h)
print(f' mascara sub rede em binario: {msk_bin}')
#mascara em decimal
msk =  Converter.return_mascara_sub__rede(msk_bin)
print(f'Mascara de subrede em decimal: {msk}')
#calculo hosts
n_hosts = Host.calc_hosts(endereço_ip,h)
print(f'quantidade de hosts: {n_hosts}')
