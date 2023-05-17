from enum import Enum

import arcade

class AttackType(Enum):
    ROCHE = 0
    PAPIER = 1
    CISEAUX = 2



class AttackAnimation(arcade.Sprite):
   ATTACK_SCALE = 0.50
   ANIMATION_SPEED = 5.0


    def __init__(self, attack_type):
       super().__init__()

       self.attack_type = attack_type
       if self.attack_type == AttackType.ROCK:
           self.textures = [
               arcade.load_texture("assets/srock.png"),
               arcade.load_texture("assets/srock-attack.png"),
           ]
       elif self.attack_type == AttackType.PAPER:
           self.textures = [
               arcade.load_texture("assets/spaper.png"),
               arcade.load_texture("assets/spaper-attack.png"),
           ]
       else:
           self.textures = [
