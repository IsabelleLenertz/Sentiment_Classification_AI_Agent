# https://www.kaggle.com/c/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from bagOfWordsModel.KaggleWord2VecUtility import KaggleWord2VecUtility
import pandas as pd
import numpy as np
import nltk
# nltk.download()
# import pandas as pd


def main():
    results = model()
    print(results)

def model():
    df_train = pd.read_csv("bagOfWordsModel.training.csv", header=0, delimiter="\t", quoting=3, names = ['sentiment', 'comment'])
    df_test = pd.read_csv("bagOfWordsModel.testdata.csv", header=0, delimiter="\t", quoting=3, names = ['comment'])
    df_test_label = pd.read_csv("bagOfWordsModel.l.csv")
    labels = np.array(df_test_label)
    clean_data = []
    for i in range( 0, len(df_train["comment"])):
        clean_data.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(df_train["comment"][i], True)))
    
        
    vectorizer = CountVectorizer(analyzer = "word",   \
                                tokenizer = None,    \
                                preprocessor = None, \
                                stop_words = None,   \
                                max_features = 5000)
    train_data_features = vectorizer.fit_transform(clean_data)
    np.asarray(train_data_features)
    
    # ******* Train a random forest using the bag of words
        #
    print("Training the random forest this may take a while \n")
    
    # Initialize a Random Forest classifier with 100 trees
    forest = RandomForestClassifier(n_estimators = 100)
    
    # Fit the forest to the training set, using the bag of words as
    # features and the sentiment labels as the response variable
    #
    # This may take a few minutes to run
    forest = forest.fit( train_data_features, df_train["sentiment"] )
    
    
    
    # Create an empty list and append the clean reviews one by one
    clean_test_reviews = []
    
    print("Cleaning and parsing the test set movie reviews...\n")
    for i in range(0,len(df_test["comment"])):
        clean_test_reviews.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(df_test["comment"][i], True)))
    
    # Get a bag of words for the test set, and convert to a numpy array
    test_data_features = vectorizer.transform(clean_test_reviews)
    np.asarray(test_data_features)
    
    # Use the random forest to make sentiment label predictions
    print("Predicting test labels...\n")
    result = forest.predict(test_data_features)
    
    # Copy the results to a pandas dataframe with an "id" column and
    # a "sentiment" column
    output = pd.DataFrame( data={"sentiment":result} )
    
    # Use pandas to write the comma-separated output file
    output.to_csv(os.path.join(os.path.dirname(__file__), '', 'bagOfWordsModel.Bag_of_Words_model.csv'), index=False, quoting=3)
    print("Wrote results to Bag_of_Words_model.csv")
    
    count_correct_class = 0
    for i in range(len(result)):
        if result[i] == labels[i]:
            count_correct_class +=1
    accuracy = (count_correct_class)/1000

    return accuracy
    
if __name__ == "__main__":
    main()
    
# train.shape
# train.columns.values 