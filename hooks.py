import random

HOOKS = {
    "Clutch": [
        "They never saw this coming...",
        "This shouldn't have worked.",
        "I had ONE chance.",
        "Watch till the end.",
        "I almost lost everything.",
        "1 HP. 4 enemies.",
        "This changed the entire match.",
        "Impossible comeback.",
        "I can't believe I survived.",
        "Luck or skill?"
    ],

    "Funny": [
        "This went horribly wrong 😂",
        "Skill issue.",
        "I regret everything.",
        "What was I thinking?",
        "This is embarrassing.",
        "Mission failed successfully.",
        "Nobody saw this coming.",
        "Instant regret.",
        "I wasn't ready for that.",
        "Peak comedy."
    ],

    "Epic": [
        "This was INSANE!",
        "One of my best plays ever.",
        "You have to see this.",
        "That ending though...",
        "Absolute domination.",
        "This is why I love this game.",
        "The perfect play.",
        "Things escalated quickly.",
        "This clip deserves more views.",
        "Unreal moment."
    ]
}

def generate(category):
    return random.sample(HOOKS[category], 5)