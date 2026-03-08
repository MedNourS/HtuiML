import re

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

def minify_html(html: str) -> str:
    """
    Returns a string representing the minified version of an HTML file
    """
    
    return html.replace("\n", "").replace(" <", "<").replace("> ", ">").replace("< ", "<").replace(" >", ">").replace("  ", " ").strip()

def remove_unnecessary_html(html: str) -> str:
    """
    Returns a string representing only the content of the <body>, removing comments and whatnot
    """
    
    return re.sub("<!--(.*?)-->", "", re.sub("<head>(.*?)</head>", "", re.sub("<script>(.*?)</script>", "", html.split("<body>")[1].split("</body>")[0]))).strip()

def structure(html: str) -> str:
    """
    Returns a string representing the structure of the html's contents, using indents
    """
    
    return html.replace(">", ">\n  ").replace("</", "\n</")