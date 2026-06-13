import spacy
nlp = spacy.load("en_core_web_lg")
text = """
 Built an AI REsume analyzer using embeddings and NlP techniques """
doc = nlp(text)
for token in doc:
    if not token.is_stop and token.is_alpha:
        print(token.text, "|", token.pos_)