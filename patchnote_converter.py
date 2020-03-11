import json


output = open('data_dump.txt', 'w', encoding = "utf-8")

with open('patch_scraper/notes.json', encoding="utf-8", errors="ignore") as json_file:
    data = json.load(json_file)
    for instance in data:
        output.write("\n".join(map(str, instance['headings'])))
        output.write("\n".join(map(str, instance['changes'])))

output.close()