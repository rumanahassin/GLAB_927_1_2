import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

print(nltk.__version__)

nltk.download("punkt")

nltk.download("punkt_tab")

nltk.download("wordnet")

nltk.download("omw-1.4")

stemmer = PorterStemmer()


email_content = (
    "Our team will be working on the upcoming "
    "project deadlines. Please ensure that all "
    "deliverables are submitted before the end "
    "of the week."
)

email_lowercase = email_content.lower()

tokens = nltk.word_tokenize(email_lowercase)

stemmed_tokens = [stemmer.stem(token) for token in tokens]

stemmed_email = " ".join(stemmed_tokens)


print("\nTASK 2: STEMMING")
print("Original Email:", email_content)
print("Stemmed Email:", stemmed_email)

lemmatizer = WordNetLemmatizer()



lemma_email_content = (
    "The team members are working on their "
    "tasks diligently. Please ensure that "
    "every report is submitted promptly."
)



lemma_tokens = nltk.word_tokenize(lemma_email_content.lower())


lemmatized_tokens = [lemmatizer.lemmatize(token) for token in lemma_tokens]

lemmatized_email = " ".join(lemmatized_tokens)


print("\nTASK 3: LEMMATIZATION")

print("Original Email:", lemma_email_content)

print("Lemmatized Email:", lemmatized_email)


words = ["running", "studies", "working", "children", "connections"]

print("\nTASK 4: STEMMING VS LEMMATIZATION")
print("Original | Stemmed | Lemmatized")


for word in words:
    stemmed = stemmer.stem(word)
    lemmatized = lemmatizer.lemmatize(word)
    print(f"{word} | {stemmed} | {lemmatized}")


print("\nVERB LEMMATIZATION TEST")
print("Default:", lemmatizer.lemmatize("running"))
print("With pos='v':", lemmatizer.lemmatize("running", pos="v"))

