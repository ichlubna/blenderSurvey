import bibtexparser

layers = [bibtexparser.middlewares.NormalizeFieldKeys()]
database = bibtexparser.parse_file("literature.bib", append_middleware=layers)
for entry in database.entries:
    url = ""
    if "url" in entry:
        url = entry["url"]
    if "doi" in entry:
        url = entry["doi"]
    print("["+entry["title"]+"]"+"(https://doi.org/"+url+")")

