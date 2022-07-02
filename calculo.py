
from conversoes import Converter
from host import Host
ip = Converter.convert_bin('192.164.125.10')
print(ip)
mascaraBin =  Converter.mask_for_bin('192.164.125.1',24)
print(mascaraBin)
