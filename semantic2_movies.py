import spacy

planet_hulk_description = '''Will he save their world or destroy it? 
                             When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle 
                             and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet 
                             Sakaar where he is sold into slavery and trained as a gladiator.'''

def preprocess_text(text):
# perform tokenizing
    nlp = spacy.load("en_core_web_md")
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

# load spacy and define filename as path to movies.txt
def find_similar_movie(planet_hulk_description, filename=".venv/movies.txt"):
    nlp = spacy.load('en_core_web_md')

    # read from text file
    with open(filename, 'r') as file:
        movie_descriptions = file.readlines()

    # preprocess input description
    input_doc = preprocess_text(planet_hulk_description)

    # calculate similarity for each movie description
    similarities = []
    for movie_description in movie_descriptions:
        similarity = nlp(" ".join(preprocess_text(movie_description))).similarity(nlp(" ".join(input_doc)))
        similarities.append(similarity)

    # find the index of most similar movie
    most_similar_index = similarities.index(max(similarities))

    # get the letter representing the most similar movie
    most_similar_movie_title = chr(65 + most_similar_index)

    return f"Next movie to watch: Movie {most_similar_movie_title}"

# print the most similar movie to the description of Planet Hulk

recommend = find_similar_movie(planet_hulk_description)
print(recommend)
