# lib module (for vimzettel_to_obsidian)

"""
Support functions for vimzettel_to_obsidian

Functions:
traverse_files
convert_text
create_file
convert_headers(string)
find_title_date(string)
"""



def convert_text(text):
    return False

def create_file(text: str, title: str, date: int) -> bool:

    newFile = open("%s.md"%(title), mode="w")
    return False

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


def find_title_date(text: list) -> tuple:
    title_signifier = "%title "
    date_signifier = "%date "

    title = text[0].replace(title_signifier, '').replace("\n",'')
    date = text[1].replace(date_signifier, '').replace("\n",'')

    return title, date

