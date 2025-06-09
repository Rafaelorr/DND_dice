from random import randint

def roller(dice_faces: int, dice_count: int, modifier: int, adv: bool) -> int:
    """
    dice_faces: max number for every roll
    dice_count: the amount of dice
    modifier: the number added to the total sum
    adv: True = advantage, False = disadvantage, None = normal
    """

    total = 0

    if adv is True:
        # advantage
        for _ in range(dice_count):
            roll1 = randint(1, dice_faces)
            roll2 = randint(1, dice_faces)
            total += max(roll1, roll2)
    elif adv is None:
        # normaal
        for _ in range(dice_count):
            total += randint(1, dice_faces)
    elif adv is False:
        # disadvantage
        for _ in range(dice_count):
            roll1 = randint(1, dice_faces)
            roll2 = randint(1, dice_faces)
            total += min(roll1, roll2)
    else:
        raise Exception("Invalid value for 'adv'.")

    result = total + modifier
    return result

def ask_number(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid number.")

# Input with validation
dice_faces = ask_number("Amount of dice faces: ")
dice_count = ask_number("Number of dice: ")
modifier = ask_number("Modifier: ")

adv_input = input("adv, normaal or disadv: ").lower()
if adv_input == "adv":
    adv = True
elif adv_input == "disadv":
    adv = False
else:
    adv = None

resultaat = roller(dice_faces, dice_count, modifier, adv)
print(f"You rolled: {resultaat}")
