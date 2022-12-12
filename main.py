"""IMPORT"""
from datetime import datetime
import requests
import json
import mwparserfromhell
import re
import itertools
import textScan

"""INPUT"""
wiki_page = 'WebSocket'

"""REQUEST"""
# action=query, format=json, and title=Bla_Bla_Bla are all standard MediaWiki API parameters
# prop=extracts makes us use the TextExtracts extension
# exintro limits the response to content before the first section heading
# explaintext makes the extract in the response be plain text instead of HTML
# Then parse the JSON response and extract the extract:

# response = requests.get(
#     'https://en.wikipedia.org/w/api.php',
#     params={
#         'action': 'query',
#         'format': 'json',
#         'titles': 'Python_(programming_language)',
#         'prop': 'extracts',
#         'exintro': True,
#         'explaintext': True,
#     }).json()
#
# for item in response['query']['pages'].values():
#     print(item)
response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
        'action': 'query',
        'format': 'json',
        'titles': wiki_page,
        'prop': 'revisions',
        'rvprop': 'content'
    }).json()

# CALC
#date_now = datetime.now()

"""RESPONSE"""
page = response['query']['pages']
page_title = page[list(page)[0]]["title"]
contentFormat = page[list(page)[0]]['revisions'][0]['contentformat']
contentModel = page[list(page)[0]]['revisions'][0]['contentmodel']
#print(json.dumps(page[list(page)[0]]['revisions'][0]['*'], indent=4))
wiki_content = mwparserfromhell.parse(page[list(page)[0]]['revisions'][0]['*'])
wiki_content_str = str(wiki_content)
wiki_content_original = wiki_content_str

"""ADJUST REFERENCES"""
references = []
references_str = ""
# FIND REFERENCE SECTION
reference_section_title = re.search(pattern='[=]*?[ ]{0,1}References[ ]{0,1}[=]*',
                              string=wiki_content_str)

# FIND ALL REFERENCES
reference_segments = re.finditer(pattern='(<ref name=.*?>.*?</ref>)|(<ref name=.*?[ ]{0,1}/>)|(<ref name=.*?>)|(<ref.*?>.*?</ref>)',
                                 string=wiki_content_str,
                                 flags=re.DOTALL)

# REPLACE AND SAVE REFERENCES
for index, reference in enumerate(reference_segments):
    if reference.end() < reference_section_title.start():
        wiki_content_str = wiki_content_str.replace(reference.group(),
                                                    " [" + str(index + 1) + "] ")
        references.append((index + 1, reference.group().replace("\n","")))

# CLEAR REFERENCE
reference_section = re.search(pattern='({{Reflist}})|({{Reflist.*</ref>.*?}})',
                              string=wiki_content_str,
                              flags=re.DOTALL)

wiki_content_str = wiki_content_str.replace(reference_section.group(),
                                            "")

# ADD REFERENCES
for ref in references:
    references_str = references_str + "[" + str(ref[0]) + "]" + ": " + str(ref[1]) + "\n"

wiki_content_str = wiki_content_str.replace(reference_section_title.group(),
                                            str(reference_section_title.group()) + "\n" + references_str)

"""REMOVE SECTIONS"""
# FIND PREAMBLE: short description
preamble_segment = re.findall(pattern='(\{\{Short description.*?\}\})',
                           string=wiki_content_str)

# REPLACE PREAMBLE: short description
for preamble in preamble_segment:
    wiki_content_str = wiki_content_str.replace(preamble,
                                                "")

# FIND PREAMBLE: dmy dates
preamble_segment = re.findall(pattern='(\{\{Use dmy dates.*?\}\})',
                           string=wiki_content_str)

# REMOVE PREAMBLE: short description
for preamble in preamble_segment:
    wiki_content_str = wiki_content_str.replace(preamble,
                                                "")

# FIND MAIN
main_segments = re.findall(pattern='(\{\{Main\|.*?\}\})',
                           string=wiki_content_str)

# REMOVE MAIN
for main in main_segments:
    wiki_content_str = wiki_content_str.replace(main,
                                                "")

# FIND PORTAL
portal_segments = re.findall(pattern='(\{\{Portal\|.*?\}\})',
                             string=wiki_content_str)

# REMOVE PORTAL
for portal in portal_segments:
    wiki_content_str = wiki_content_str.replace(portal,
                                                "")

# REMOVE SEE ALSO
# FIND PORTAL
seealso_segments = re.findall(pattern='(\{\{See also\|.*?\}\})',
                             string=wiki_content_str)

# REMOVE PORTAL
for seealso in seealso_segments:
    wiki_content_str = wiki_content_str.replace(seealso,
                                                "")
# {{-}}

"""ADJUST FILES/IMAGES"""
# FIND FILES/IMAGES
files_segments = re.findall(pattern='(\[\[File:.*\]\])',
                            string=wiki_content_str)

# REPLACE FILE/IMAGE TEXT
for file in files_segments:
    wiki_content_str = wiki_content_str.replace(file,
                                                "{{" + str(file[2:-2]) + "}}")

"""ADJUST LIST"""
# FIND LIST
list_segments = re.findall(pattern='(\{\{columns-list\|.*\]\]\n\}\})',
                           string=wiki_content_str,
                           flags=re.DOTALL)

# DETECT ITEMS AND REPLACE LIST
for list in list_segments:
    list_new = ""
    list_items = re.findall(pattern='[*](.*)',
                            string=list)
    for item in list_items:
        list_new = list_new + "* " + str(item).strip() + "\n"

    wiki_content_str = wiki_content_str.replace(list,
                                                list_new)

"""FORMAT TABLES"""
# TODO process table
# FIND TABLES
table_segments = re.findall(pattern='(\{\|[ ]{0,1}class="wikitable".*\|\})',
                            string=wiki_content_str,
                            flags=re.DOTALL)

# BUILD LAYOUT AND REPLACE TABLE
for table in table_segments:
    wiki_content_str = wiki_content_str.replace(table,
                                                "```" + str(table) + "```")

"""REMOVE NOTES"""
note_segments = re.finditer(pattern='<!--.*?-->',
                            string=wiki_content_str,
                            flags=re.DOTALL)

for note in note_segments:
    wiki_content_str = wiki_content_str.replace(str(note.group()),
                                                "")

"""ADJUST HEADINGS"""
# FIND HEADINGS
headings_old = ["=======",
                "======",
                "=====",
                "====",
                "===",
                "=="]
headings_new = ["######",
                "#####",
                "####",
                "###",
                "##",
                "#"]

for (item_old, item_new) in zip(headings_old, headings_new):
    heading_segment = re.findall(pattern="(" + str(item_old) + "[ ]{0,1}(.*?)[ ]{0,1}" + str(item_old) + ")",
                                 string=wiki_content_str)
    for item in heading_segment:
        wiki_content_str = wiki_content_str.replace(item[0],
                                                    str(item_new) + " " + str(item[1]))

"""ADJUST CODE SEGMENTS"""
# FIND ALL CODE SEGMENTS
code_segments = re.findall(pattern='(<syntaxhighlight [\w]*=\"(?P<code_lang>\w+)\".*>)',
                           string=wiki_content_str)

code_segments_old = [item[0] for item in code_segments]
code_segments_new = [item[1] for item in code_segments]

# TRANSLATE TO MD ABBREVIATIONS
code_segments_translated = textScan.str2clang(code_segments_new)

# REPLACE CODE SEGMENTS
for (item_old, item_translated) in zip(code_segments_old, code_segments_translated):
    wiki_content_str = wiki_content_str.replace(item_old,
                                                "```" + item_translated)
wiki_content_str = wiki_content_str.replace("</syntaxhighlight>",
                                            "```")

"""REMOVE SPECIAL CHARACTERS"""
special_strings = ["&nbsp;"]
# FIND SPECIAL CHARACTERS
for sp_ch in special_strings:
    wiki_content_str = wiki_content_str.replace(sp_ch,
                                                " ")

"""REMOVE LINKS"""
# FIND ALL LINKS
links = re.finditer(pattern='(\[\[(.*?)\]\])',
                    string=wiki_content_str)

new_list = []
for item in links:
    string_search = item.groups()[1]
    string_search_br = item.groups()[0]
    output = re.match(pattern=".*\|([\w\s-]*)",
                      string=string_search,
                      flags=re.DOTALL)
    if output is not None:
        new_list.append((string_search_br, string_search, output.groups()[0]))
    elif output is None:
        new_list.append((string_search_br, string_search, None))

for link in new_list:
    if link[2] is not None:
        wiki_content_str = wiki_content_str.replace(link[0],link[2])
    elif link[2] is None:
        wiki_content_str = wiki_content_str.replace(link[0], link[1])
    else:
        #TODO error
        pass



#wiki_content_str = wiki_content_str.replace("[[", "").replace("]]", "")

# for item in page.values():
#     print(item)

# for item in response['query']['pages'].values():
#     print(item)
# page = next(iter(response['query']['pages'].values()))
# wikicode = page['revisions'][0]['*']
# wikicode = page['revisions'][0]['*']
# parsed_wikicode = mwparserfromhell.parse(wikicode)
# print(parsed_wikicode.strip_code())

# RETRIEVE TEMPLATE
with open('wiki_template.md', 'r') as f:
    template = f.read()

# WRITE
with open('processed.md', 'w', encoding="utf-8") as f:
    f.write(template)
    f.write(wiki_content_str)

with open('original.md', 'w', encoding="utf-8") as f:
    f.write(template)
    f.write(wiki_content_original)