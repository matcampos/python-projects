text_A= "''"
text_B="''"


from difflib import HtmlDiff

delta_html = HtmlDiff().make_file(text_A.splitlines(), text_B.splitlines())

with open ('diff.html', 'w') as f:
    f.write(delta_html)