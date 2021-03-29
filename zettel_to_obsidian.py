# This script converts vimwiki (zettel) files to markdown for Obsidian
# Author: Gabe kamalakis


# Open the file
# Count headers (convert to # ## and ###)
# Find Title/Date/filename
# Links should actually stay the same


import sys
import os


def main():

    # Creating a new folder called "obsidian"
    relative_directory = os.path.relpath('.','/')
    new_directory_name = "obsidian"

    path = os.path.join(relative_directory, new_directory_name)
    os.mkdir(path)


    command = sys.argv[1]


    zettelFile = open(command, mode='r')
    text = zettelFile.readlines()


    print("Creating File...")
    newFile = open("%s.md"%(command.rstrip(".wiki")), mode="w")

    for line in text:
        line = convert_headers(line)
        newFile.write(line)

    newFile.close()
    zettelFile.close()


def create_json():

    status = False
    return status



def convert_headers(line):

    """
    convert_headers(string)
    Takes single line of text
    Replaces VimWiki headers with Markdown headers
    returns converted header as string
    """

    header_strength = 0
    old_header = "="
    new_header = "#"

    for character in line:
        if character == old_header:
            header_strength += 1
        else:
            break

    new = line.replace(old_header, '')
    newline = new_header * header_strength + new

    return newline

def convert_title(text):
    # converting title to text breaks links...
    # Not sure how to convert all links into their perspective titles
    # Maybe use some kind of dictionary and convert all files at once?
    title_signifier = "%%title "
    date_signifier = "%%date "

    title = text[0].replace(title_signifier, '')
    date = text[1].replace(date_signifier, '')

    return title, date

# def convert_tag(text):

main()

