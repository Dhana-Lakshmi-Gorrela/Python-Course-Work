'''
class whatsappv1:
    def messaging(self):
        print("You can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("you can audio and video")

a = whatsappv1()
a.messaging()

b = whatsappv2()
b.calls()
'''
'''
class whatsappv1:
    def messaging(self):
        print("You can message")

class whatsappv2:
    def extramessaging(self):
        print("you can add emojis, stickers and gifs")
    

class whatsappv3(whatsappv1,whatsappv2):
    def calls(self):
        print("you can audio and video")

class whatsappv4(whatsappv3):
    def status(self):
        print("you can add the status for 24 hours")

a = whatsappv1()
a.messaging()

b = whatsappv2()
b.extramessaging()

c = whatsappv3()
c.calls()

d = whatsappv4()
d.messaging()
d.extramessaging()
d.calls()
d.status()
'''
'''
class whatsappv1:
    def status(self):
        print("You can add images and videos")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("you can add music and stickers")
    

class whatsappv3(whatsappv2):
    def status(self):
        super().status()
        print("you can like and you can add reaction")


a = whatsappv3()
a.status()
'''
class whatsappv1:
    def status(self):
        print("You can add images and videos")

class whatsappv2:
    def status(self):
        print("you can add music and stickers")
    

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("you can like and you can add reaction")


a = whatsappv3()
a.status()

