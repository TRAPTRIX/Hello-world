
from youtube_dl import YoutubeDL
options = {}

ydl = YoutubeDL(options)


info = ydl.extract_info("https://www.youtube.com/watch?v=2Vv-BfVoq4g", download=False)


# ython-dictionary-to-json-tutorial-with-example/ phần "Writing JSON to a file"
# import json
# with open('info.json', 'w',encoding="utf8") as json_file:
#   json.dump(info, json_file)
# print(info)

# info_2 = ydl.extract_info("https://www.youtube.com/watch?v=WX7dUj14Z00", download=False)
# print(info_2["id"])
# Fucking_information=[]
# Fucking_information.append(info_2["id"])
# print(Fucking_information)



