class IPAddress:
    def __init__(self, ip):
        self.ip = ip

    def __get__(self, instance, owner):
        ip_all = ".".join(str(i) for i in a.__dict__[self.ip])
        print(ip_all)

    def __set__(self, instance, value):
        self.value = str(value).split(".")
        self.field = []
        for i in self.value:
            self.field.append(i)
        a.ip1_fields = self.field


class A:
    def __init__(self):
        self.ip1_fields = [1, 2, 3, 4]
а
    ip1 = IPAddress("ip1_fields")
    ip2 = IPAddress("ip2_fields")


a = A()
a.ip1
a.ip1 = "123.121.124.126"
a.ip1
print()
a.ip1 = "222.121.124.126"
a.ip1
print()



#a.ip1 = "192.168.0.1"
