name = str(input("Enter your name: "))
age = int(input("how old are you?"))
favourite_items = str(input("what is your favourite item?"))
what_is_your_favourite_color = str(input("what is your favourite color?"))
favourite_food = str(input("what is your absolutely favourite food?"))
when_is_your_birthday = str(input("when is your birthday?"))
def candle_count(ag):
    for i in range(ag):
        candles = i
        print(candles)
print(f"Hello, {name}!Thank you for inviting me to your birthday party!")
print(f"here is your present, I hope you like it!Its a {favourite_items}")
print(f"Yes I got it in your favourite colour{what_is_your_favourite_color}!")
print(f"Come you must eat I know you like {favourite_food}!")
print(f"blow out your candles and make a wish!I will count them for you!")
candle_count(age)