# IMPORTS
import wikipediaapi
import html2markdown
from datetime import datetime

# Info on wiki API https://wikipedia-api.readthedocs.io/en/latest/wikipediaapi/api.html
# Maybe need use of https://github.com/didix21/mdutils package?

wiki_page = 'WebSocket'
date_now = datetime.now()

wiki_wiki = wikipediaapi.Wikipedia(language='en',
                                   extract_format=wikipediaapi.ExtractFormat.WIKI)

p_wiki_wiki = wiki_wiki.page(wiki_page)
p_wiki_markdown = html2markdown.convert(p_wiki_wiki.text)

#print(type(p_wiki_wiki))
print(p_wiki_wiki.title)
print(p_wiki_wiki.summary)
#print(p_wiki_wiki.text)
#print('---------------')
#print(p_wiki_markdown)

#TODO
# 1. Add a function to get the text of a page
# 2. Add a function to get the text of a page in markdown format
# 3. Search for "&nbsp;" and replace by " "
# 4. Search for "<link href="mw-data:TemplateStyles:r1067248974" rel="mw-deduplicated-inline-style"/>" and remove

# for link in p_wiki_wiki.links:
#    print(link)

template = (f'---\n'
f'title: {p_wiki_wiki.title}\n'
f'author: Wikipedia\n'
f'tags: in-progress\n'
f'url:\n'
f'publish date:\n'
f'reviewed date: {date_now}\n'
f'aliases: []\n'
f'---\n'
f'\n'
f'# {p_wiki_wiki.title}\n')

print(template)

with open('test_md.md', 'w', encoding="utf-8") as f:
    f.write(template)
    f.write(p_wiki_markdown)

# with open('test_markdown.txt', 'w') as f:
#     f.write(p_wiki_markdown.text)

