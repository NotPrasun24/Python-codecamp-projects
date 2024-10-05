print("-"*20)
print("Welcome to Mad Libs")
print("-"*20)

name = input("Enter any name you would like to add to the story: ")
verb = input("Enter any name you would like to add to the verb: ")
city = input("Enter any name you would like to add to the city: ")
food = input("Enter any name you would like to add to the food: ")
planet = input("Enter any name you would like to add to the planet: ")
body_part = input("Enter any name you would like to add to the body part: ")

print("\nHere is your Mad Libs story: \n")



story = f"One day, {name} decided to {verb} all the way to {city}. On the way, they found a mysterious piece of {food} lying on the ground. Curious, they picked it up with their {body_part} and suddenly felt a strange sensation. \
Before they knew it, {name} was transported to the planet {planet}! There, they met a group of aliens who loved to {verb} just like {name} did. The aliens offered {name} a special dish made of {food}, and even though it looked a little odd, {name} decided to try it. Surprisingly, it tasted just like something from {city}. After spending the day exploring {planet}, {name} finally found a way to return to Earth. But they would never forget their incredible adventure—and the taste of that delicious {food} from another world."

print(story)