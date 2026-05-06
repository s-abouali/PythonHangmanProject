import random

hangman_art = {
    0: ["  +---+",
        "      |",
        "      |",
        "      |",
        "      |",
        "========="],

    1: ["  +---+",
        "      |",
        "      O",
        "      |",
        "      |",
        "========="],

    2: ["  +---+",
        "      |",
        "      O",
        "      |",
        "     / ",
        "========="],

    3: ["  +---+",
        "      |",
        "      O",
        "     /|",
        "     / ",
        "========="],

    4: ["  +---+",
        "      |",
        "      O",
        "     /|\\",
        "     / ",
        "========="],

    5: ["  +---+",
        "      |",
        "      O",
        "     /|\\",
        "     / \\",
        "========="],

    6: ["  +---+",
        "      |",
        "     \\O/",
        "     /|\\",
        "     / \\",
        "========="]
}

words = ("aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo",
         "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo",
         "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle",
         "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam",
         "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow",
         "curlew", "deer", "dinosaur", "dog", "dolphin", "donkey", "dormouse", "dotterel",
         "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel",
         "eland", "elephant", "elk", "emu", "falcon", "ferret", "finch", "fish",
         "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe",
         "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk",
         "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog",
         "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird",
         "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo",
         "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur",
         "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird",
         "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink",
         "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal",
         "newt", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter",
         "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl",
         "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony",
         "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon",
         "rail", "ram", "rat", "raven", "red-deer", "red-panda", "reindeer", "rhinoceros",
         "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion",
         "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake",
         "sparrow", "spider", "spoonbill", "squid", "squirrel", "starling", "stingray",
         "stoat", "stork", "swallow", "swan", "tapir", "tarsier", "termite", "tiger",
         "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus",
         "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock",
         "woodpecker", "worm", "wren", "yak", "zebra")


def display_man(wrong_guesses):
    print("\n" + " " * 10 + "HANGMAN")
    for line in hangman_art[wrong_guesses]:
        print(line.center(20))
    print()


def display_word(hint, wrong_guesses, guessed_letters):
    print("Word: " + " ".join(hint))
    if wrong_guesses > 0:
        print(
            f"Wrong guesses: {', '.join(sorted(list(set([chr(c) for c in guessed_letters if c not in ' '.join(hint)]))))}")
    print("-" * 30)


def main():
    answer = random.choice(words).lower()
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    max_wrong = len(hangman_art) - 1  # 6 wrong guesses

    print("Welcome to Hangman!")
    print(f"Word has {len(answer)} letters\n")

    while True:
        display_man(wrong_guesses)
        display_word(hint, wrong_guesses, guessed_letters)

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter exactly one letter!")
            continue

        if guess in guessed_letters:
            print("❌ You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            print("✅ Good guess!")
        else:
            wrong_guesses += 1
            print("❌ Wrong guess!")

        if "_" not in hint:
            display_man(wrong_guesses)
            print("🎉 YOU WIN!")
            print(f"The word was: {' '.join(answer)}")
            break

        if wrong_guesses >= max_wrong:
            display_man(wrong_guesses)
            print("💀 YOU LOSE!")
            print(f"The word was: {' '.join(answer)}")
            break

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == 'y':
        main()

if __name__ == "__main__":
    main()