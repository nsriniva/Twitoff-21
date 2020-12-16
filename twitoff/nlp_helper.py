

import spacy

SPACY_MODEL_NAME = "en_core_web_sm"

if not spacy.util.is_package(SPACY_MODEL_NAME):
	spacy.cli.download(SPACY_MODEL_NAME)

nlp = spacy.load(SPACY_MODEL_NAME)

def vectorize_tweet(tweet_text):
    return nlp(tweet_text).vector


if __name__ == "__main__":

    print("IF YOU ARE SEEING THIS, THE SPACY NLP MODEL HAS BEEN DOWNLOADED!")
    print(nlp)

    for example_tweet in ["Hello world", "We love #DataScience"]:
        print("-----------")
        print(example_tweet)
        vect = vectorize_tweet(example_tweet)
        print(vect)
