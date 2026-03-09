from bs4 import BeautifulSoup
import re

default_soup_parser: str = "lxml"

def get_html_content(abs_path: str) -> str:
    """
    Returns a string representing the contents of an HTML file
    """
    
    try:
        with open(abs_path, 'r', encoding='utf-8') as html_file:
            html_content: str = html_file.read()
            return html_content
    except Exception:
        return ""

def get_html_info(abs_path: str) -> dict:
    """
    Returns a dictionary representing info about an HTML file
    """
    
    try:
        with open(abs_path, 'r', encoding='utf-8') as html_file:
            html_content: str = html_file.read()
    except Exception:
        return {}
    
    soup = BeautifulSoup(html_content, default_soup_parser)
    
    return {
        "title": soup.title.get_text(),
        "language": soup.html["lang"],
        "css_links": [link_element["href"] for link_element in soup.find_all("link")]
    }

def structure(html: str, minify: bool = False) -> str:
    """
    Returns a string representing the structure of the html's contents, using indents
    """
    
    soup = BeautifulSoup(html, default_soup_parser)
    
    if minify:
        return re.sub("\n", "", str(soup))
    else:
        return str(soup)

def get_body(html: str) -> str:
    """
    Returns a string representing the <body>
    """
    
    soup = BeautifulSoup(html, default_soup_parser)

    return re.sub("<!--(.*?)-->", "", str(soup.find("body"))).replace("\n\n", "\n")

def get_content(html: str, tag: str = "body") -> str:
    """
    Returns a string representing the content of the chosen html tag, which is "body" by default, and removes comments
    """
    
    return re.sub("<!--(.*?)-->\n", "", html.split(f"<{tag}>")[1].split(f"</{tag}>")[0].strip())