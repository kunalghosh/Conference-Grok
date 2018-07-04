from collections import namedtuple # later use py3.7 dataclasses
import urllib
import feedparser
import pdb

ArxivPaper = namedtuple("ArxivPaper", [
                                        "title", 
                                        "authors", 
                                        "abstract",
                                        "linktopdf",
                                        "linktoabs"
                                        ])

def arxiv_url_sanitizer(url):
    """
    as of now, just converts 
    arxiv.org/pdf/ to arxiv.org/abs
    """
    # if its an arxiv pdf url then
    if url.find("pdf") != -1:
        url = url.replace("/pdf","/abs")
        url = url.replace(".pdf","")
    return url

def get_paper_info(url):
    """
    Given an arxiv url returns
    a ArxivPaper object with fields
        title : str
        authors : str
        abstract : str
        linktopdf : str
        linktoabs : str
    """
    arxiv_id = url.split("/")[-1]
    arxiv_searchurl = "http://export.arxiv.org/api/query?id_list={}".format(arxiv_id)

    try:
        atom_feed = urllib.request.urlopen(arxiv_searchurl)
    except urllib.error.HTTPError as e:
        # print("Couldn't retrieve : {}".format(arxiv_searchurl))
        raise RuntimeError("Trouble fetching ArXiv Id : {}".format(arxiv_id))

    parsed_feed = feedparser.parse(atom_feed)
    paper = parsed_feed["entries"][0]
    
    title = paper["title"]
    authors = paper["authors"]
    abstract = paper["summary"]
    linktopdf = None
    linktoabs = None
    for link_dict in paper["links"]:
        if link_dict["type"].find("html") != -1:
            linktoabs = link_dict["href"]

        elif link_dict["type"].find("pdf")!= -1:
            linktopdf = link_dict["href"]

    # comment = paper["arxiv_comment"] # Not there in all arxiv pages.
    return ArxivPaper(title, authors, abstract, linktopdf, linktoabs) 
