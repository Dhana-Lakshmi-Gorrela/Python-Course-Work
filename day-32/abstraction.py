from abc import ABC,abstractmethod

class Phonepay(ABC):
    def sendeeinfo(self):
        print("you can entre their mobile number or scanner")
    def amount(self):
        print("you can enter amount")
    def pin(self):
        print("you need to enter the pin")

    @abstractmethod
    def tansaction(self):
        pass

class HDFC(Phonepay):
    def tansaction(self):
        print("payment using hdfc bank")

class SBI(Phonepay):
    def transaction(self):
        print("payment using sbi bank")

class UNION(Phonepay):
    def tansaction(self):
        print("payment using union bank")

class AXIS(Phonepay):
    def tansaction(self):
        print("payment using axis bank")

class ICIC(Phonepay):
    def tansaction(self):
        print("payment using icic bank")


pavani = HDFC()
pavani.sender.info()
pavani.amount()
pavani.pin()
pavani.transaction()

lucky = SBI()
lucky.sender.info()
lucky.amount()
lucky.pin()
lucky.transaction()

sai = UNION()
sai.sender.info()
sai.amount()
sai.pin()
sai.transaction()

ammu= AXIS()
ammu.sender.info()
ammu.amount()
ammu.pin()
ammu.transaction()

divya = ICIC()
divya.sender.info()
divya.amount()
divya.pin()
divya.transaction()


