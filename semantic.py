import spacy
nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
      for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

# 'en_core_web_md'
# 0.5929930274321619 - the similarity between "cat" and "monkey" is 0.59 possibly due to both being animals 
# 0.40415016164997786 - similiarity betwewn "mokey" and "banana" is 0.40, this will raise similiarities in less direct ways as it is a food that 
# monkeys eat, and a recognisable one at that. but does not directly match as is a species of monkey was named 
# 0.22358825939615987 # similiarity betwewn "banana" and "cat" - no real similarities resulting in the lower score of 0.22

# cat cat 1.0
# cat apple 0.2036806046962738
# cat monkey 0.5929930210113525
# cat banana 0.2235882580280304
# apple cat 0.2036806046962738
# apple apple 1.0
# apple monkey 0.2342509925365448
# apple banana 0.6646699905395508
# monkey cat 0.5929930210113525
# monkey apple 0.2342509925365448
# monkey monkey 1.0
# monkey banana 0.4041501581668854
# banana cat 0.2235882580280304
# banana apple 0.6646699905395508
# banana monkey 0.4041501581668854
# banana banana 1.0


# 'en_core_web_sm'
# [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  # print(word1.similarity(word2))
# 0.6770565478895127
# /Users/joshuapoulter/anaconda3/.venv/semantic.py:8: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  # print(word3.similarity(word2))
# 0.7276309976205778
# /Users/joshuapoulter/anaconda3/.venv/semantic.py:9: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  # print(word3.similarity(word1))
# 0.6806929391210822

# cat cat 1.0            
# cat apple 0.7018378973007202
# cat monkey 0.6455236077308655
# cat banana 0.2214718759059906
# apple cat 0.7018378973007202
# apple apple 1.0
# apple monkey 0.7389943599700928
# apple banana 0.36197030544281006
# monkey cat 0.6455236077308655
# monkey apple 0.7389943599700928
# monkey monkey 1.0
# monkey banana 0.4232020080089569
# banana cat 0.2214718759059906
# banana apple 0.36197030544281006
# banana monkey 0.4232020080089569
# banana banana 1.0

            
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(f"{sentence} - {similarity}")

# MD
# where did my dog go - 0.630065230699739
# Hello, there is my car - 0.8033180111627156
# I've lost my car in my car - 0.6787541571030323
# I'd like my boat back - 0.5624940517078084
# I will name my dog Diana - 0.6491444739190607
      
#SM
# 

# comparisons
# using SM rather than MD shows us that SM does not use word vectors therefor uses tagger, parser and NER to find similarity. it does provide higher scores 
# cases when comparing cat and monkey and monkey and banana due to NER, this is also the case when comparing cat and banana which increased by 0.46 which shows 
# less accuracy in the language model of recognising the similarity between unrelated words
            
# when 