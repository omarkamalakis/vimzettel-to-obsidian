# This script converts vimwiki (zettel) files to markdown for Obsidian
# Author: Gabe kamalakis


# Open the file
# Count headers (convert to # ## and ###)
# Find Title/Date/filename
# Links should actually stay the same


import sys


def main():

    argument = sys.argv[1]


    zettelFile = open(argument, mode='r')
    text = zettelFile.readlines()


    print("Creating File...")
    newFile = open("%s.md"%(argument.rstrip(".wiki")), mode="w")

    for line in text:
        line = convert_headers(line)
        newFile.write(line)

    newFile.close()
    zettelFile.close()




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

