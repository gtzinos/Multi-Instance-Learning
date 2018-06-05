import re
import csv


def convert_labels_to_binary(input_file_path, most_frequent_index, output_file_path):
    fp = open(input_file_path, 'r')
    outfp = open(output_file_path, 'w')

    outfp.write("reference,other\n")

    while True:
        ln = fp.readline()
        if len(ln) == 0:
            break

        columns = ln.split(' ')

        for index, column in enumerate(columns):
            if index == (most_frequent_index + 1):
                if column == "1":
                    outfp.write("1 -1\n")
                else:
                    outfp.write("-1 1\n")

    outfp.close()
    fp.close()


def convert_sentences_to_binary(input_file_path, most_frequent_index, output_file_path):
    fp = open(input_file_path, 'r')
    outfp = open(output_file_path, 'w')

    while True:
        ln = fp.readline()
        if len(ln) == 0:
            break

        parts = re.findall('<[^>]+>', ln)

        for part in parts:
            part = part.replace("<", "")
            part = part.replace(">", "")
            columns = part.split(' ')

            for index, column in enumerate(columns):
                # print(part)
                if index == (most_frequent_index + 1):
                    if column == "1":
                        outfp.write("<1 -1>")
                    else:
                        outfp.write("<-1 1>")

        outfp.write("\n")

    outfp.close()
    fp.close()


convert_labels_to_binary("../data/train-label.dat", 2,
                         "../data/new_train-label.dat")
convert_labels_to_binary("../data/test-label.dat", 2,
                         "../data/new_test-label.dat")

#convert_sentences_to_binary("../data/train-sentlabel.dat", 2, "../data/new_train-sentlabel.dat")
convert_sentences_to_binary(
    "../data/test-sentlabel.dat", 2, "../data/new_test-sentlabel.dat")
