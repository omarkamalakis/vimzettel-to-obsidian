# Vim-Zettel to Obsidian Conversion script


Vim-Zettel creates vimwiki pages using vimwiki's wiki format. This script converts any directory which contains a Zettel-Wiki into an Obsidian folder.


## Goals:

- Convert all page filenames to titles
		- filenames are currently random numbers
		- associate random numbers with files

- Convert all links within each page to reflect new filenames
- Convert tags from vimwiki to markdown
- convert titles/dates to markdown

Everything else should be largely identical



## Methods

Create a database (or JSON) of filenames, titles, and dates.

Read through each file in directory and add entries to the database(top part of file has the important data).

Convert each file:
- change filename to title
- change links to associated title from database
- change formatting (headers/tags/etc.)

Write each file to markdown and export to a new folder (include JSON file in folder for metadata)
