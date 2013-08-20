===================
 PHP to HTML
===================

A simple script to convert sites created in PHP using header and footer files to a more universal HTML format.

The script processes PHP files it fines and saves the output, so header and footer files are effectively processed. It also replaces .php files extensions with .html.

Script ignores any files that begin with .git, .svn, and .DS_Store as those were the most problematic.

Usage
===============
./php_to_html.py [source dir] [destination dir]


To Do
===============
Add a robust configuration for ignoring files.
