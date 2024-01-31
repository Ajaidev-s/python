class shop:
    def __init__(self,name=None,qty=0):
        self.name=name
        self.qty=qty
    def purchase(self,qty):
        self.qty=self.qty+qty
    def sales(self,qty):
        self.qty=self.qty-qty
    def __str__(self):
        return self.name+"\t"+str(self.qty)
print("name    quantity")
pen=shop("pen",10)
pencil=shop("pencil",15)
era=shop("Eraser",3)
print(pen)
print(pencil)
print(era)
print("after purchase of 3 eraser")
era.purchase(3)
print(pen)
print(pencil)
print(era)
print("after sales of 4 pen")
pen.sales(4)
print(pen)
print(pencil)
print(era)
