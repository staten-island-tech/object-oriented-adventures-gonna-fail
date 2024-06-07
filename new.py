class monster():

    def attack(self, user):
        user.health = 10 - 5
        print ("user.health")
        




    def __str__(self):
        return f"{self.name}, {self.age}, {self.artist}"