# Trying to make a simple program to filter out words from messages.
messages = [
    "You swing wide and miss.",
    "The enemy laughs at you.",
    "That was a damn close call.",
    "You regain your stance.",
    "You land a clean hit.",
    "The goblin snarls.",
    "Damn, your blade got stuck for a second.",
    "You yank your weapon free.",
    "The enemy blocks with a shield.",
    "You circle to the right.",
    "A glancing hit connects.",
    "The target staggers.",
    "You take a breath.",
    "The enemy charges.",
    "You dodge left.",
    "You dodge right.",
    "You get clipped on the shoulder.",
    "Damn that hurt.",
    "You shake it off.",
    "You raise your guard.",
    "The enemy swings high.",
    "You parry at the last moment.",
    "Your counterattack lands.",
    "The enemy grunts.",
    "You hear metal clash.",
    "You step back.",
    "You lunge forward.",
    "The enemy retreats.",
    "You keep pressure on them.",
    "The enemy slips on loose gravel.",
    "You capitalize immediately.",
    "Damn, that was lucky.",
    "You strike again.",
    "The enemy's armor dents.",
    "They try to grapple you.",
    "You break free.",
    "You shove them away.",
    "The enemy throws sand.",
    "You blink rapidly.",
    "You swing blindly.",
    "You hear a yelp.",
    "The enemy is wounded.",
    "You focus your aim.",
    "You thrust forward.",
    "Direct hit.",
    "The enemy backs off.",
    "You advance carefully.",
    "The enemy feints.",
    "Damn, you almost fell for it.",
    "You recover fast.",
    "You slam your shield forward.",
    "The enemy stumbles.",
    "You go for a heavy strike.",
    "It lands with force.",
    "The enemy roars.",
    "You hear a damn loud crack in the distance.",
    "You glance around quickly.",
    "You refocus on the fight.",
    "The enemy tries a low sweep.",
    "You jump over it.",
    "You land awkwardly.",
    "Damn, your ankle twists slightly.",
    "You push through the pain.",
    "The enemy presses the attack."
]


def filter_messages(messages):
    damn_counter = 0
    filtered_messages = []  # Empty List

    # We need to check each messages
    for message in messages:
        filtered_word = []
        current_message = message
        print(f"Current Message: {current_message}")

        # Now we're splitting the words
        for word in message.split():
            print(f"Word: {word}")
            if word == "Dang":
                damn_counter += 1
                filtered_word.append(word)

        filtered_messages.append(" ".join(filtered_word))
        print(f"Damn Counter: {damn_counter}")

    for message in filtered_messages:
        print(message)


filter_messages(messages)
