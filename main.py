from calculo_redes_ipv4 import CalculoIPV4
calculos =  CalculoIPV4('192.168.1.5',pre = 24)
print(f'\t Endereço ip: {calculos.ip}')
print(f'\t Mascara de SubRede: {calculos.mask}')
print(f'\t Ip da rede: {calculos.ip_da_rede()}')
print(f'\t Broadcast: {calculos.broadcast()} ')
print(f'\t Prefixo da rede: {calculos.pre}')
print(f'\t numeros de IPs da rede: {calculos.quantidade_host()}')

'''
amanha calcular o ip da rede e broadcast
'''
