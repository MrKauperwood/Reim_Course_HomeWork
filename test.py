class A:
    def __init__(self):
        self.ip1_fields = [1, 2, 3, 4]
        self.ip2_fields = [2, 3, 4, 5]

    ip1 = IPAddress("ip1_fields")
    ip2 = IPAddress("ip2_fields")

a = A()
a.ip1
a.ip1 = "192.168.0.1"
a.ip2