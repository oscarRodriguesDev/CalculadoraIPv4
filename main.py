from calculo_redes_ipv4 import CalculoIPV4
calculos =  CalculoIPV4('192.168.125.10',pre = 26)
print(f'\t Endereço ip: {calculos.ip}')
print(f'\t Mascara de SubRede: {calculos.mask}')
print(f'\t Ip da rede: ')
print(f'\t Broadcast: ')
print(f'\t Prefixo da rede: {calculos.pre}')
print(f'\t numeros de IPs da rede: {calculos.quantidade_host()}')

'''
amanha calcular o ip da rede e broadcast
'''
