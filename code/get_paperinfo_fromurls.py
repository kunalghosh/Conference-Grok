from code.arxiv_util import arxiv_url_sanitizer
from code.arxiv_util import get_paper_info

def get_paperinfo_fromurls(urls_filepath):
    """
    Returns a dictionary of url entered by user
    and corresponding paper info from arxiv.
    """

    url_paperinfo = {}
    with open(urls_filepath) as f:
        for original_url in f.readlines():
            url = arxiv_url_sanitizer(original_url.strip())
            # print("Sanitized url = {}".format(url))
            try:
                paper_info = get_paper_info(url)
            except RuntimeError as e:
                print("[SKIP] Error processing : {}, message : {}".format(url, e))
                pass
            url_paperinfo[original_url] = paper_info
            
    return url_paperinfo
