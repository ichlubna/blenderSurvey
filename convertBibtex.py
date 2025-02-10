import bibtexparser

sectionFiles = ["sectionA.tex", "sectionB.tex"]
outputDir = "./parsed"
layers = [bibtexparser.middlewares.NormalizeFieldKeys()]
database = bibtexparser.parse_file("literature.bib", append_middleware=layers)
for entry in database.entries:
    url = ""
    if "url" in entry:
        url = entry["url"]
    if "doi" in entry:
        url = entry["doi"]
    link = "["+entry["title"]+"]"+"(https://doi.org/"+url+")"
    print(link)
    for fileName in sectionFiles:
        with open(fileName) as file:
            contents = file.read()
            if entry.key in contents:
                with open(outputDir+"/"+fileName,'a') as f:
                    f.write(link+"\n")

