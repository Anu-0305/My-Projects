import random

subjects = ["monkey", "neha kakkar", "salman khan", "modi", "nirmala sitharaman", "auto driver from delhi"]
actions = ["eats", "beats", "launches", "declares", "cancels", "dances with", "sings with"]
places_or_things = ["banana", "kashmir", "erragadda", "mental hospital", "plate of samosa"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    print(f"\nBREAKING NEWS: {subject} {action} {place_or_thing}")

    user_input = input("Type yes to continue, no to stop: ").strip().lower()

    if user_input == "no":
        print("Stopping program...")
        break
