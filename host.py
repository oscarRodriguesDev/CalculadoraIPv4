from conversoes import Converter
class Host:
    # resolução recebendo o /n
    @staticmethod
    def calc_hosts(ip, rd):
        ip_bin = Converter.convert_bin(ip)
        listcomp = [x for x in ip_bin for x in x]
        listtcomp2 = [1 for x in range(rd)]
        v1 = len(listcomp)
        v2 = len(listtcomp2)
        v3 = v1 - v2
        for i in range(v3):
            listtcomp2.append(0)
        return (2 ** v3) - 2

if __name__=='__main__':
    hosts = Host.calc_hosts('125.165.12.3',26)
    print(hosts)