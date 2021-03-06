import markovify

# obtention de la compilation de discours
with open("path-to-macron") as f:
    text = f.read()

# création du modèle
text_model = markovify.Text(text)

# on affiche 20 phrases (vous pouvez changer ce nombre comme bon vous semble)
for i in range(20):
    print(text_model.make_sentence())
