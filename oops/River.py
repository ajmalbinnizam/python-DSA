class River:
    all_rivers = []
    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)

    def get_info(self):
        print("the river {0} is {1} in length".format(self.name, self.length))

volga = River("volga", 320)
yamuna = River("yamuna", 300)
ganges = River("ganges", 280)
# for i in River.all_rivers:
#     print(i.name)

volga.get_info()
print(yamuna.name)
