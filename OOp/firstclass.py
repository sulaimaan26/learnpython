class SystemInfo:
    power = "220v"

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        self.feat = self.feature

    def getconfig(self):
        print(self.cpu, self.ram)

    @classmethod
    def checkclass(cls):
        return cls.power

    @staticmethod
    def staticclass():
        print("This is static method")

    class feature:
        def __init__(self, camtype, reliable):
            self.camtype = camtype
            self.reliable = reliable


print(__name__)
computer1 = SystemInfo("I5", 4)
computer2 = SystemInfo("I7", 9)
computer1.getconfig()
computer2.getconfig()
print(computer1.power)
SystemInfo.power = "440v"
print(computer2.power)
print(SystemInfo.checkclass())
computer1.staticclass()
computer1.checkclass()
computer1.feat("aa", "a")
print(computer1.feat.camtype)
