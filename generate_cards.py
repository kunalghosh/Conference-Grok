#!/usr/bin/env python3

import os
import sys
import pprint
from code.cards_template import CARDS_TEMPLATE
# from code import arxiv_url_sanitizer # converts /pdf/ urls to /abs/ urls
from code.get_paperinfo_fromurls import get_paperinfo_fromurls # takes in arxiv urls and returns details to render 

if __name__ == "__main__":
    data_path = "./data"
    template_path = "./html"
    template_file = "template.html"
    urls_file = sys.argv[1]
    assert urls_file.find(".txt") != -1, "Expecting a text file as input"
    output_htmlfile = urls_file.replace(".txt", ".html")

    card_template = CARDS_TEMPLATE(
                        path_to_template = template_path,
                        template_filename = template_file,
                                    )
    paper_details = get_paperinfo_fromurls(urls_filepath = os.path.join(data_path, urls_file))
    card_template.render(paper_details_iterator=paper_details)
    card_template.save_html(output_dir = template_path, output_htmlfile = output_htmlfile)



