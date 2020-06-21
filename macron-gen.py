import markovify

# Get raw text as string.
with open("path-to-macron") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(20):
    print(text_model.make_sentence())