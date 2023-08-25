pokemons = {
    "Bulbasaur": {"tipo": "Grass"},
    "Ivysaur": {"tipo": "Grass"},
    "Charmander": {"tipo": "Fire"},
    "Charmeleon": {"tipo": "Fire"},
    "Squirtle": {"tipo": "Water"},
    "Wartortle": {"tipo": "Water"},
    "Pikachu": {"tipo": "Electric"},
    "Raichu": {"tipo": "Electric"},
    "Vulpix": {"tipo": "Fire"},
    "Growlithe": {"tipo": "Fire"},
}

tipo = input('digite um tipo de pokemon').lower()

lista_pokemon = []

for key in pokemons:
    if pokemons[key]['tipo'].lower() == tipo:
        lista_pokemon.append(key)

print(f"Os pokemons do tipo selecionado foram : {lista_pokemon} e há {len(lista_pokemon)} pokemons")
