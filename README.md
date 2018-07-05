# About
A simple CSS card interface to sift through a list of ArXiv links.
It displays the title, authors, abstract and a link to access the pdf.

Usecase: When going through papers published at a conference, I open the arxiv url of each of the papers in a separate tab in the browser.
This results in a lot of open tabs in the browser. Instead of doing this, I keep a list of the arxiv urls in a text file. This script helps `convert the list of urls` to a `list of research paper details` (title, authors, abstracts, pdf link) which is much easy to refer to subsequently. 

# Demo
Converts list of [arxiv urls](https://github.com/kunalghosh/Conference-Grok/blob/master/data/icml.txt) to [deck of CSS Cards](https://htmlpreview.github.io/?https://github.com/kunalghosh/Conference-Grok/blob/master/html/icml.html)

![gif demo](https://media.giphy.com/media/7OWsu9E23HiViWZV8L/giphy.gif)

# Dependencies:
1. Python3  : This is a Python based project.
2. Jinja2   : For generating the HTML
3. FeedParser : parses Atom feed returned by arxiv.org
4. Web Browser

# How to use ?
1. Create a text file `data_file.txt` in ./data containing arxiv links.
2. Run `python3 generate_cards.py data_file.txt` which generates an html file in ./html with the same name as `data_file.txt`
3. Open ./html/`data_file.html` in your favourite web browser (needs CSS)
