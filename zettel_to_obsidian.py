# This script converts vimwiki (zettel) files to markdown for Obsidian
# Author: Gabe kamalakis


# Open the file
# Count headers (convert to # ## and ###)
# Find Title/Date/filename
# Links should actually stay the same


import sys
import os
import json
import argparse
import lib

def main():

    # Creating a new folder called "obsidian"

    # command = sys.argv[1]
    # target = sys.argv[1]
    # option = sys.argv[3]

    # new_directory_name = "obsidian"
    # os.mkdir(new_directory_name)

    tmp = traverse_files()
    print(tmp)


def traverse_files() -> dict:
    """
    Reads all .wiki files and extracts
    titles, ID numbers, and dates. Returns
    a dictionary to be used as reference
    for links

    dictionary structure:
    {ID: {"Title", "Date"},..}
    """

    pages = {}

    for page in os.scandir():

        if (page.path.endswith(".wiki")):

            id_number = page.path.lstrip('./').rstrip('.wiki')
            zettelFile = open(page.path, mode='r')
            text = zettelFile.readlines()
            title, date = lib.find_title_date(text)

            pages[id_number] = [title, date]

    return pages



main()

