import math
import random
import os
import os.path
import argparse


def create_list(files_count, max_digits):
    list = []

    for i in range(1, files_count + 1):
        # Append file number
        # Use the same number of digits as
        # the number of files in local dir
        file_number = (max_digits - (int(math.log10(i))+1)) * str(0) + str(i)
        list.append(file_number)

    # Randomize file number order
    random.shuffle(list)

    return list


def rename_files(file_number_list, separator, new_order):
    for number, file_name in zip(file_number_list, os.listdir(".")):
        if(file_name != "media_shuffle.py"):

            file_name_without_number = " " + file_name

            if(not new_order):
                # Finds previous file ordering if it exists
                # Removes it so only the file's name remains
                if(file_name[0] == "["):
                    end = file_name.find(']')
                    file_name_without_number = file_name[end+1:]
                elif(file_name[0] == "("):
                    end = file_name.find(')')
                    file_name_without_number = file_name[end+1:]
                elif(file_name[0].isdecimal()):
                    end = 1
                    while file_name[end].isdecimal():
                        end = end + 1
                    file_name_without_number = file_name[end:]

            # Selects separator from args (default: no separator)
            if(separator == "pa"):
                separator_start = "("
                separator_end = ")"
            elif(separator == "br"):
                separator_start = "["
                separator_end = "]"
            else:
                separator_start = ""
                separator_end = ""

            # Rename the file with selected separator and order
            os.rename(file_name, separator_start + number +
                      separator_end + file_name_without_number)
    return


parser = argparse.ArgumentParser(
    description='Shuffles your media files in the current directory')
parser.add_argument('-n', dest='new_order',
                    default=False,
                    action='store_true',
                    help='adds ordering numbers without checking for preexisting ones')

parser.add_argument('-s', dest='separator',
                    default="",
                    help='separator for the file number (br for "[]", pa for "()") (default: none)')
args = parser.parse_args()

files_count = len([name for name in os.listdir('.') if os.path.isfile(name)])
max_digits = int(math.log10(files_count))+1
file_number_list = create_list(files_count, max_digits)
rename_files(file_number_list, args.separator, args.new_order)
