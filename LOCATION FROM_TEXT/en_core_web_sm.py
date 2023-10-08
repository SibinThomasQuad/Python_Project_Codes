#language processing
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Function for Tokenization
def tokenize_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return tokens

# Function for Part-of-Speech Tagging
def pos_tagging(text):
    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags

# Function for Named Entity Recognition (NER)
def named_entity_recognition(text):
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

# Function for Dependency Parsing
def dependency_parsing(text):
    doc = nlp(text)
    dependencies = [(token.text, token.dep_) for token in doc]
    return dependencies

# Example text
text = "Apple Inc. is an American multinational technology company headquartered in Cupertino, California. It was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976."

# Tokenization Example
print("Tokenization:")
tokens = tokenize_text(text)
print(tokens)

# Part-of-Speech Tagging Example
print("\nPart-of-Speech Tagging:")
pos_tags = pos_tagging(text)
print(pos_tags)

# Named Entity Recognition Example
print("\nNamed Entity Recognition:")
entities = named_entity_recognition(text)
print(entities)

# Dependency Parsing Example
print("\nDependency Parsing:")
dependencies = dependency_parsing(text)
print(dependencies)
