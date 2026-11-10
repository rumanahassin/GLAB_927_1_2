
# GLAB 927.1.2 — Hands-On Text Processing for Email Management with Python

## Project Description
This project explores how Python and the Natural Language Toolkit (NLTK) can be used to process business emails.

The assignment focuses on two natural language processing techniques: stemming and lemmatization. These techniques help normalize words so that email text can be analyzed, searched, and compared more effectively.

The project uses uv to manage Python dependencies and provides practical examples of text preprocessing.


## Key Concepts

### Natural Language Toolkit (NLTK)

NLTK is a Python library used for natural language processing (NLP). It provides tools for analyzing and processing human language, including tokenization, stemming, and lemmatization.

In this project, NLTK is used to process business email text and compare different methods of word normalization.


### Tokenization

Tokenization is the process of splitting text into smaller units called tokens, such as words and punctuation marks.

In this project, NLTK's word_tokenize function is used to break business emails into individual tokens before applying stemming and lemmatization.


### Stemming

Stemming is a natural language processing technique that reduces words to their root or base forms by removing or modifying word endings.

In this project, NLTK's PorterStemmer is used to process business email text.

For example, "working" becomes "work" and "studies" becomes "studi".

Stemming can help improve email searching and text matching by grouping words with similar roots. However, the resulting stems are not always valid dictionary words.


### Lemmatization

Lemmatization is a natural language processing technique that converts words into their dictionary forms, called lemmas.

In this project, NLTK's WordNetLemmatizer is used to normalize words in business emails.

For example, "children" becomes "child" and "studies" becomes "study".

Unlike stemming, lemmatization generally produces valid dictionary words. The results can depend on the part of speech assigned to a word.

Lemmatization can improve text analysis by helping identify different forms of the same word.


## Setup and Execution Instructions

This project uses Python, uv, and NLTK.

### Setup

Open a terminal in the GLAB_927_1_2 project directory.

Install the project dependencies:

```bash
uv sync
```

### Run the Application

Run the email-processing program:

```bash
uv run python src/glab_927_1_2/email_processing.py
```

Note: On a new computer, the program may need to download the required NLTK data resources: punkt, punkt_tab, wordnet, and omw-1.4.

## Task 4: Comparison and Reflection

### Comparison Results

The following table shows the results of applying stemming and lemmatization to five words.

| Original Word | Stemmed Word | Lemmatized Word |
|---|---|---|
| running | run | running |
| studies | studi | study |
| working | work | working |
| children | children | child |
| connections | connect | connection |

I noticed that stemming and lemmatization produced different results for several words. For example, "studies" became "studi" with stemming but "study" with lemmatization. Also, "children" stayed the same with stemming but changed to "child" with lemmatization.


### 1. What is the main difference between stemming and lemmatization?

Stemming and lemmatization both help reduce words to their base forms,
but they work differently. Stemming cuts off word endings and sometimes
creates words that are not real words. For example, "upcoming" became
"upcom." Lemmatization tries to find the correct dictionary form of a
word. For example, "members" became "member." I learned that stemming
is simpler, while lemmatization helps keep words meaningful.

### 2. Which technique is more likely to return dictionary forms? Give a concrete example?

Lemmatization is more likely to return real dictionary words because it considers the word's proper form. For example, stemming changed "studies" to "studi," which is not a real word, while lemmatization changed it to "study." This helped me understand why lemmatization can be more useful when we want words to keep their meaning.

### 3. How could stemming support search or matching in business emails?

Stemming can make it easier to search business emails by reducing similar words to the same root. For example, "working" and "worked" can both become "work." This can help find related emails even when different forms of a word are used.

### 4. What benefit might lemmatization offer in a text-analysis pipeline?

Lemmatization helps make text easier to analyze by changing different forms of words into their dictionary forms. For example, "children" becomes "child" and "studies" becomes "study." This can help a program recognize related words and understand the text more consistently.

### 5. How did the pos argument change a result?

The pos argument tells the lemmatizer what type of word it is processing. When I tested "running" without specifying pos, the word stayed the same. When I used pos="v" to identify it as a verb, "running" changed to "run." I learned that specifying the correct part of speech can help produce a more accurate result.

## Summary of Findings and What I Learned

In this assignment, I learned how to use Python and NLTK to process business emails using stemming and lemmatization. I noticed that stemming is simpler but sometimes produces words that are not real dictionary words, while lemmatization usually keeps words meaningful.

I also learned how the `pos` argument can change the results of lemmatization. Overall, this assignment helped me better understand how text processing can make searching and analyzing business emails easier.