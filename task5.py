# class Soldier():
#     def __init__(self,name = 'Ryan'):
#         self.name = name
# class Guns():
#     def __init__(self,weapon):
#         self.weapon = weapon
# class Act_of_Shooting(Soldier,Guns):
#     def __init__(self, *args):
#         super().__init__(self,*args)
#         self.bullets = 10
#     def fire_bullets(self):
#         print('fire-fire')

#     def fill_bullets(self):
#         self_bullets += 1

#     def subtract_bullets(self):
#         self_bullets -= 1

# guns = Act_of_Shooting('Ak-47')
# guns.self_bullets(15)
# guns.fire_bullets()
# guns.fill_bullets()
# guns.subttract_bullets()





class Soldier:
    def __init__(self, name = 'Ryan'):
        self.name = name

class Gun:
    def __init__(self, make):
    # def __init__(self, make='AK47')
        self.make = make

class Act_of_Shooting(Soldier, Gun):
    def __init__(self, *args):
        Soldier.__init__(self, *args)
        self.bullets = 5

    def fill_bullets(self, num):
        self.bullets += num

    def gun_fire(self):
        if self.bullets:
            print('tigi-tigitishh')
            self.bullets -= 1
        else:
            print('no bullets')

soldier = Act_of_Shooting ('AK-47')
soldier.gun_fire()
soldier.gun_fire()
soldier.gun_fire()
soldier.gun_fire()
soldier.gun_fire()
soldier.gun_fire()
soldier.fill_bullets(10)
soldier.gun_fire()