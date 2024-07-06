from spellchecker import SpellChecker

# Crear una instancia del corrector ortográfico para el idioma español
spell = SpellChecker(language='es')

# Lista de palabras a corregir
words = ["escribir", "corrector", "ortografía", "programasion", "licicitacion"]

# Encontrar las palabras mal escritas
misspelled = spell.unknown(words)

for word in misspelled:
    # Obtener la palabra corregida
    corrected = spell.correction(word)
    print(f'{word} -> {corrected}')