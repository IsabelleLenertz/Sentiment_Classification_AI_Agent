#
#author : Jisha Pillai (jisha.pillai@sjsu.edu)
#
# Instruction to run the code:
#
# python normality_search.py -n <filename>
# Example = python normality_search.py -n new_training.csv
#

import math
from decimal import *
import pandas as pd
import numpy as np
import argparse
import itertools
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from scipy.stats.mstats import normaltest

__FIG_SIZE__ = (8, 10)
__ITERATIONS__ = 3
__TRAIN_DF_ = []
__TEST_DF = []


def main():
    initial_index = 0
    final_index = 0
    normality_value = 0
    parser = argparse.ArgumentParser(description = "argument parser")
    parser.add_argument('-n', type=argparse.FileType('r'))
    args = parser.parse_args()

    # Read the csv file from the argument
    data_frame = pd.read_csv(args.n)

    columns = ['SentimentScore', 'SubjectivityScore']

    i = 0
    cutoff_value = 2000
    initial = 0
    final = 0
    while i < __ITERATIONS__:
        i = i + 1
        final = final + cutoff_value

        df = data_frame[columns]
        df = df[initial:final]
        #initial = initial + cutoff_value

        # Generate Histograms
        similarity_value, new_df = generate_histogram(df, columns, normality_value)

        if similarity_value > normality_value:
            print(normality_value)
            normality_value = similarity_value
            normal_dist_df = new_df
            initial_index = initial
            final_index = final
            print(df.head())
            print(final_index)
    initial = initial + cutoff_value
    data_frame[initial_index:final_index].to_csv(r'../../Data/norm_dist_training.csv')

def generate_histogram(df, columns, normality_value):
    print(df.head())

    #Column reduction
    df_col_reduction = df
    df_col_reduction['red_col'] = df_col_reduction.apply(column_reduction, axis = 1)

    print(df_col_reduction['red_col'])

    #Perform normality test
    normality_result = normaltest(df_col_reduction['red_col'])

    similarity_value = normality_result[0]
    pvalue = normality_result[1]

    print("Histogram for the data set.")

    histogram_df = df_col_reduction['red_col']

    fig = plt.figure(figsize = __FIG_SIZE__)
    plt.gcf().clear()

    histogram_df.hist(normed = True)
    histogram_df.plot(kind = 'kde', linewidth = 2, \
                            color = 'r', label = 'Distribution Of Dataset')


    norm_fit = stats.norm.pdf(np.linspace(-3, 3, len(histogram_df)), np.mean(histogram_df), np.std(histogram_df))
    plt.plot(np.linspace(-3, 3, len(histogram_df)), norm_fit, label="Normal Distribution", color = 'k', linewidth = 2) # plot it

    plt.xlabel("Dataset Distribution")
    plt.ylabel("Frequency")

    plt.title("Similarity to normal distribution: " +str(similarity_value)+
    ", pvalue: " + str(pvalue))

    plt.legend()
    plt.show()

    return similarity_value, df_col_reduction

    # print("Histogram for the test data set.")
    #
    # histogram_test_df = df_test_col_reduction['red_col']
    #
    # fig = plt.figure(figsize = __FIG_SIZE__)
    # plt.gcf().clear()
    #
    # histogram_test_df.hist(normed = True)
    # histogram_test_df.plot(kind = 'kde', linewidth = 2, \
    #                         color = 'r', label = 'Distribution Of Dataset')
    #
    #
    # norm_fit = stats.norm.pdf(np.linspace(-3, 3, len(histogram_test_df)), np.mean(histogram_test_df), np.std(histogram_test_df))
    # plt.plot(np.linspace(-3, 3, len(histogram_test_df)), norm_fit, label="Normal Distribution", color = 'k', linewidth = 2) # plot it
    #
    # plt.xlabel("Dataset Distribution")
    # plt.ylabel("Frequency")
    #
    # plt.title("Similarity to normal distribution: " +str(similarity_value_test)+
    # ", pvalue: " + str(pvalue_test))
    #
    # plt.legend()
    # plt.show()



def column_reduction(row):
    reduced_column = np.sqrt(np.sum([i*i for i in row]))
    return reduced_column


if __name__ == "__main__":
    main()
