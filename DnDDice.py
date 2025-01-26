from random import randint

def roller (dice_faces:int, dice_count:int, modifier:int, adv:bool) -> int:
    """
    dice_faces: max number for every roll
    dice_count: the amount of dice
    modifier: the number add to the sum of all the rolls
    adv: True = advantage, None = normal, disadvantage = False
    """

    roll :int = 0
    temp_resulat: list[int] = [0,0]

    if adv:
        for _ in range(dice_count+1):
          temp_resulat = [randint(1,dice_faces),randint(1,dice_faces)]
          if temp_resulat[0] > temp_resulat[1]:
              roll += temp_resulat[0]
          else:
              roll += temp_resulat[1]
    elif adv == None:
        for _ in range(dice_count+1):
            roll += randint(1,dice_faces)
    elif adv == False:
        for _ in range(dice_count+1):
          temp_resulat = [randint(1,dice_faces),randint(1,dice_faces)]
          if temp_resulat[0] < temp_resulat[1]:
              roll += temp_resulat[0]
          else:
              roll += temp_resulat[1]
    else:
        raise Exception("Function failed")
    
    resulat = roll + modifier

    return resulat

try:
    dice_faces :int = int(input("Amount of faces on the dice: "))
except int:
    print("Enter a number.")
    dice_faces :int = int(input("Amount of faces on the dice: "))

try:
    dice_count :int = int(input("Amount of dice: "))
except int:
    print("Enter a number.")
    dice_count :int = int(input("Amount of dice: "))

try:
    modifier :int = int(input("Roll modifier: "))
except int:
    print("Enter a number")
    modifier :int = int(input("Roll modifier: "))

adv = input("adv,normal or disadv: ")
if adv == "adv":
    adv :bool = True
elif adv == "disadv":
    adv :bool = False
else:
    adv :bool = None


resulat = roller(dice_faces,dice_count,modifier,adv)
print("You rolled "+resulat)