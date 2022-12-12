import wikipedia

wiki_page = wikipedia.page("Websockets")

print(wiki_page.url)
print(wiki_page.images)
print(wiki_page.links)