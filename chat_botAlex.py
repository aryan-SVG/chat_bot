

from nltk.chat.util import Chat, reflections


pairs = (
    (
        r"(.*)NLP(.*)",
        (
            "Natural language processing (NLP) refers to the branch of computer science—and more specifically, the branch of artificial intelligence or AI—concerned with giving computers the ability to understand text and spoken",
        ),
    ),
    (
        r"(.*)NLTK(.*)",
        (
            "The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language.",
        ),
    ),
    (
        r"(.*)Penn Tree Bank(.*)",
        (
            "The Penn Treebank (PTB) project selected 2,499 stories from a three year Wall Street Journal (WSJ) collection of 98,732 stories for syntactic annotation.",
        ),
    ),
    (
        r"(.*)k-means (.*)",
        (
            "k-means is linear to the number of instances and clusters; instead, the original partitional clustering problem is NP-hard.",
            
        ),
    ),
    (
        r"(.*)stop words(.*)",
        (
            "Stop words are said to be useless data for a search engine. Words such as articles, prepositions, etc. are considered as stop words. There are stop words such as was, were, is, am, the, a, an, how, why, and many more",
        ),
    ),
    (
        r"(.*)Syntactic Analysis(.*)",
        (
            "Syntactic Analysis:Syntactic analysis is a technique of analyzing sentences to extract meaning from it. Using syntactic analysis, a machine can analyze and understand the order of words arranged in a sentence. NLP employs grammar rules of a language that helps in the syntactic analysis of the combination and order of words in documents.",
            
        ),
    ),
    (
        r"(.*)Regular Expressions(.*)",
        (
            "A regular expression is used to match and tag words. It consists of a series of characters for matching strings.",
        ),
    ),
    (
        r"(.*)Regular Grammar(.*)",
        (
            "Regular grammar is used to represent a regular language.",
        ),
    ),(
        r"(.*)best first search (.*)",
        (
            "a numerical function to keep the queue of states sorted",
        ),
    ),

    (
        r"(.*)Parsing(.*)",
        (
            "Parsing in NLP refers to the understanding of a sentence and its grammatical structure by a machine. Parsing allows the machine to understand the meaning of a word in a sentence and the grouping of words, phrases, nouns, subjects, and objects in a sentence. ",
            
        ),
    ),
    (
        r"(.*)tokenization(.*)",
        (
            "It will split a text into separate words and sentences.",
        ),
    ),
    (
        r"(.*)tagger(.*)",
        (
            "It will label each word with a part of speech",
        ),
    ),
    (
        r"(.*)Pragmatic Analysis(.*)",
        (
            "Pragmatic analysis is an important task in NLP for interpreting knowledge that is lying outside a given document. The aim of implementing pragmatic analysis is to focus on exploring a different aspect of the document or text in a language. ",
        ),
    ),
    (
        r"(.*) Naive Bayes algorithm(.*)",
        (
            "Naive Bayes algorithm is a collection of classifiers which works on the principles of the Bayes’ theorem. This series of NLP model forms a family of algorithms that can be used for a wide range of classification tasks including sentiment prediction, filtering of spam, classifying documents and more. ",
        ),
    ),
    (
        r"(.*)text Summarization(.*)",
        (
            "Text summarization is the process of shortening a long piece of text with its meaning and effect intact. Text summarization intends to create a summary of any given piece of text and outlines the main points of the document. This technique has improved in recent times and is capable of summarizing volumes of text successfully.",
        ),
    ),
    (
        r"(.*)information extraction(.*)",
        (
            " Information extraction in the context of Natural Language Processing refers to the technique of extracting structured information automatically from unstructured sources to ascribe meaning to it. ",
        ),
    ),

    (
        r"Hi(.*)",
        (
            "Hi, Let us learn nlp...",
        ),
    ),
    (
        r"(.*)Bag of Words(.*)",
        (
            " Bag of Words is a commonly used model that depends on word frequencies or occurrences to train a classifier. This model creates an occurrence matrix for documents or sentences irrespective of its grammatical structure or word order. ",
        ),
    ),
    (
        r"(.*)NLP Tools(.*)",
        (
            "SpaCy,TextBlob,Textacy,Natural language Toolkit (NLTK),Stanford NLP,CogcompNL",
        ),
    ),
    (
        r"(.*)POS tagging(.*)",
        (
            "Parts of speech tagging better known as POS tagging refer to the process of identifying specific words in a document and grouping them as part of speech, based on its context.",

        ),
    ),
 

    (
        r"(.*)\?",
        (
            "can you say that again?",
            "Say what huh?",
            "I am sorry can you repeat that?",
        ),
    ),
    (
        r"quit",
        (
            "Bye Bye ",
            "Have a good day.",
            "I hope the guy who made me get extra credits Lol",
        ),
    ),
    (
        r"(.*)",
        (
            
            "Let's change the topic a bit ...",
            "Can you say that again  on that?",
           
            "Ohh Okay.",
            "Very Good .",
            
            "what does that tell you?",
            
            
        ),
    ),
)

Alex_chatbot = Chat(pairs, reflections)


def Alex_chat():
    
    print("Chat with ALEX ")
    print(' You can Enter "quit" when done.')
    print("=" * 80)
    print("Hello.  How can I help you today?")

    Alex_chatbot.converse()



def demo():
    Alex_chat()



if __name__ == "__main__":
    demo()