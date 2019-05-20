import csv
import sys
sys.path.append('../')
from model import sentiment_analysis

def main():
    new_file = open("../../Data/feature_extracted_training.csv", 'w')
    writer = csv.writer(new_file, delimiter = ',')
    writer.writerow(('ClassLabel', 'Sentence', 'SentimentScore', 'SubjectivityScore'))
    with open("../../Data/training.csv", 'r') as file:
        lines = csv.reader(file, delimiter = ',')
        for line in lines:
            ClassLabel, Sentence = line
            features = sentiment_analysis.feature_extraction(Sentence)
            writer.writerow((ClassLabel, Sentence, features['Blob sentiment'], features['Blob subjectivity']))



if __name__ == "__main__":
    main()
