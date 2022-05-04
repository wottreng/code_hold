import ipaddress

class CIDRtools:

    def __init__(self):
        self.testCIDRs: list = ["10.42.0.1/24", "192.168.1.1/24"]

    def getAllIPaddrFromCIDR(self, CIDR: str):
        # ipCIDR = '185.117.73.0/24'
        allIPaddressesInCIDR: list = []
        set1 = ipaddress.ip_network(CIDR)
        ip_list = [str(ip) for ip in set1]
        for ipv4 in ip_list:
            allIPaddressesInCIDR.append(ipv4)
        return allIPaddressesInCIDR

    def getSubCIDRlist(self, allIPaddresses: list):
        subCIDRlist: list = []
        for ipaddress in allIPaddresses:
            if ".0" in ipaddress[-2:]:
                subCIDRlist.append(f"{ipaddress}/24")
        return subCIDRlist

    def buildSubCIDRlist(self, CIDRlist: list):
        # CIDRlist = ["1.1.1.0/19","etc..."]
        allSubCIDRs: list = []
        for CIDR in CIDRlist:
            allIPaddresses = self.getAllIPaddrFromCIDR(CIDR)
            subCIDRlist = self.getSubCIDRlist(allIPaddresses)
            for CIDR in subCIDRlist:
                allSubCIDRs.append(CIDR)
        return allSubCIDRs


if __name__ == '__main__':
    f = CIDRtools()
    allSubCIDRs = f.buildSubCIDRlist(f.testCIDRs)
    print(allSubCIDRs)



