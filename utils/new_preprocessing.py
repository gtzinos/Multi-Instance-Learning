import re
import csv


def convert_labels_to_binary(input_file_path, most_frequent_index, output_file_path):
    fp = open(input_file_path, 'r')
    outfp = open(output_file_path, 'w')

    ln = fp.readline()
    outfp.write("reference,other\n")

    while True:
        ln = fp.readline()
        if len(ln) == 0:
            break

        columns = ln.split(',')

        for index, column in enumerate(columns):
            if index == most_frequent_index:
                if column == "1":
                    outfp.write("1,-1\n")
                else:
                    outfp.write("-1,1\n")
            
    outfp.close()
    fp.close()

convert_labels_to_binary("../data/train-label", 2, "./test-results")
