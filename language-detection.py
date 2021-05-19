from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text_input = str(input("Please enter text: "))

def language_check(text):
    language = {} #Dictionary to store the number of times the language occured in the text
    word = [word.lower() for word in word_tokenize(text_input)] #Creating a list from the text
    for lang in stopwords.fileids(): #Itarating through stropwords
        stopWords = set(stopwords.words(lang))
        words = set(word)
        common_words = words.intersection(stopWords) #Creating a set of similar words in text and stopwords

        language[lang] = len(common_words) #Counting the number of occurrences
    return language #Dictionary - language: number of times the stopwords occurred

def language_detection(text):
    languages = language_check(text)
    most_frequent_language = max(languages, key=languages.get)
    print("Detected language: ", most_frequent_language, "\n\nOther detected languages: ")

    del languages[most_frequent_language] #Deleting the key to prevent appearing in "Other detected languages"

    s = sum(languages.values()) #sum of the values in the dictionary
    for k, v in languages.items(): #Iterating through keys and values in the dictionary
        perc = v * 100.0 / s #Calculating the percentage of occurrences of each language
        if perc > 0: #Ignoring the languages that had 0 occurences
            print(k, format(perc, '.2f'))

language_detection(text_input)

