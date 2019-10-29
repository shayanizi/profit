#!/usr/bin/python
class Manage:
    def __init__(self,pip,lot):
        self.pip=pip
        self.lot=lot
    def profit(self):
        return (10*self.pip*self.lot)
man=Manage(int(input("how pip?!")),
           float(input("how lotage?!")))
management=Manage.profit(man)
print(management)