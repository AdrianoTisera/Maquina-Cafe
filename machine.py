class Machine():
    # Una máquina que da café solo, café doble, café con leche simple, café con leche doble, chocolate, capuccino, y té.
    def prepare_coffee(self, coins, quantity):
        if coins >= (quantity*2):
            return True
        else:
            return False
    
    def prepare_d_coffee(self, coins, quantity):
        if coins >= (quantity*3):
            return True
        else:
            return False
    
    def prepare_coffee_w_milk(self, coins, quantity):
        if coins >= (quantity*5):
            return True
        else:
            return False
    
    def prepare_d_coffee_w_milk(self, coins, quantity):
        if coins >= (quantity*2):
            return True
        else:
            return False
    
    def prepare_chocolate(self, coins, quantity):
        if coins >= (quantity*5):
            return True
        else:
            return False
    
    def prepare_capuccino(self, coins, quantity):
        if coins >= (quantity*7):
            return True
        else:
            return False
    
    def prepare_tea(self, coins, quantity):
        if coins >= (quantity):
            return True
        else:
            return False