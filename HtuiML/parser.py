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
    
    return html.replace("\n", "").replace(" <", "<").replace("> ", ">").replace("< ", "<").replace(" >", ">").replace("  ", " ").replace("  ", " ")