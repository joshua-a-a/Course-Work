# Load SpaCy

import spacy 

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ''' London the Shard is tall look up,
The girl told the story cried,
Mary gave the child a Band-Aid,
That Jill is never here hurts,
The cotton clothing is made of grows in Mississippi
'''

doc = nlp(gardenpathSentences)

for ent in doc.ents:
    print(f"{ent.text:{8}} {ent.label_}")

print(spacy.explain("GPE"))
print(spacy.explain("FAC"))
print(spacy.explain("PRODUCT"))

# for the first sentence it returns London as GPE and the Shard as a product
# the second sentence returns the same results for the same reason
# the third sentence returns MARY defined as a person
# onto the fourth defines JILL as a person 
# finally the fith sentence defines Mississippi as GPE meaning its a "country, city, state"

# the Shard is a Skyscraper in London. This does not represent a product, instead FAC. However, in the context of the sentence it is easily read as an object. 
# Mississippi was ready as GPE which means Countries, cities, states, etc. This makes sense and matches as the context of the word is a city in USA

