pokemons = [int(x) for x in input().split(' ')]  # get user inputs
removed_pokemons = []

while len(pokemons) > 0:
    idx = int(input())  # get index to be removed

    # Case when index is less than zero
    if idx < 0:
        pokemon = pokemons.pop(0)  # get hold of first pokemon value
        pokemons.insert(0, pokemons[-1])  # insert copy of last pokemon in first position
    # Case when index is bigger than the list size
    elif idx >= len(pokemons):
        pokemon = pokemons.pop(len(pokemons) - 1)  # get hold of last pokemon value
        pokemons.insert(len(pokemons), pokemons[0])  # insert copy of first pokemon in the last position
    # any other case
    else:
        pokemon = pokemons.pop(idx)  # get hold of Pokemon value

    # add or subtract removed pokemon value from other pokemons
    pokemons = [x + pokemon if x <= pokemon else x - pokemon for x in pokemons]

    removed_pokemons.append(pokemon)  # append removed pokemon to list of removed pokemons

print(sum(removed_pokemons))  # print the final output
