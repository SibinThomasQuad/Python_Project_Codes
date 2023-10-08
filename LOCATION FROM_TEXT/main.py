import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Text containing location information
text = "New York is a city in the United States. Paris is in France."

# Process the text with spaCy
doc = nlp(text)

# Iterate through the entities in the text and filter for locations
locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

# Print the identified locations
for location in locations:
    print("Location:", location)
