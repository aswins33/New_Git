class Phone:
    def call(self):
        print("calling...")

class Camera:
    def take_photo(self):
        print("photo captured!..")

class smartPhone(Phone,Camera):
    def browse(self):
        print("browsing..")


sp = smartPhone()
sp.call()
sp.take_photo()
sp.browse()