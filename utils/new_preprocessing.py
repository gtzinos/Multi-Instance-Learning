import re
import csv


def convert_labels_to_binary(input_file_path, most_frequent_index, output_file_path):
    fp = open(input_file_path, 'r')
    outfp = open(output_file_path, 'w')

    while True:
        ln = fp.readline()
        if len(ln) == 0:
            break

        columns = ln.split(' ')

        for index, column in enumerate(columns):
            if index == (most_frequent_index + 1):
                if column == "1":
                    outfp.write("1 0\n")
                else:
                    outfp.write("0 1\n")

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
                        outfp.write("<1 0>")
                    else:
                        outfp.write("<0 1>")

        outfp.write("\n")

    outfp.close()
    fp.close()
