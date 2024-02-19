# We have to define the songs
first_song = ["brr", "fiu", "cric-cric", "brrah"]
second_song = ["pep", "birip", "trri-trri", "croac"]
third_song = ["bri-bri", "plop", "cric-cric", "brrah"]

# We have to define the animal sounds
frog_sounds = ["brr", "birip", "brrah", "croac"]
dragonfly_sounds = ["fiu", "plop", "pep"]
cricket_sounds = ["cric-cric", "trri-trri", "bri-bri"]


# we have to define the function to play the sound
def play_song(sound: str) -> list[str]:
    """
    This function will play the sound that is passed as a parameter
    :param sound: str
    :return: []
    """

    # We have to check in which sound the sound is
    if sound in first_song:
        index = first_song.index(sound)
        return first_song[index + 1:]
    elif sound in second_song:
        index = second_song.index(sound)
        return second_song[index + 1:]
    elif sound in third_song:
        index = third_song.index(sound)
        return third_song[index + 1:]

    # If the sound does not match any sound, do not play anything
    return []


def verify_sound(sound: str) -> bool:
    """
    This function will verify if the sound is in the list of sounds
    :param sound: str
    :return: bool
    """
    return sound in frog_sounds or sound in dragonfly_sounds or sound in cricket_sounds


# We have to show the sounds that the user can enter
print("The musical lake has three songs:")
print(f"Song 1: {','.join(first_song)}")
print(f"Song 2: {','.join(second_song)}")
print(f"Song 3: {','.join(third_song)}")

# We have to show the user the sounds that can be entered
print(
    "You can only enter a sound from any of the sounds emitted by the animals in the musical lake. \nIf you enter a sound that is not in the list, the program will not play anything. \n\n")

# We have to show the sounds that the user can enter
print("The sounds you can enter are:\n")
print(f"Frog sounds: {','.join(frog_sounds)}")
print(f"Dragonfly sounds: {','.join(dragonfly_sounds)}")
print(f"Cricket sounds: {','.join(cricket_sounds)}")

# We have to ask the user for the sound
sound_input = input("\n\n Please enter a sound: ")

# We have to verify if the sound is in the list of sounds
if verify_sound(sound_input):
    # We have to play the sound
    results = play_song(sound_input)
    if len(results) > 0:
        print("\nPlaying:", ", ".join(results))
    else:
        print("\nNothing is played for the given sound.")
