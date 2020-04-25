import json

array = []
nl = '\n'
story = ''
data = {}
data['Story'] = []

with open("Diatribe.txt", "r") as ins:
    for line in ins:
        if line == nl:
            array.append(story)
            story = ''
        else:
            story += line.rstrip()

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    data['Story'] = array

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4, sort_keys=True)