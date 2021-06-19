import json


class Emoji:
    def __init__(self, json_path):
        self.json_path = json_path
    
    def add_emoji(self, name, alt, file_path, description):
        entry = ["emojis/"+file_path, description, [name, alt]]
        json_data = self.emoji_json_load()
        json_data[name] = entry
        self.emoji_json_write(json_data)

    def emoji_json_load(self):
        with open(self.json_path, 'r') as file:
            json_data = json.load(file)
            file.close()
    
        return json_data
        
    def emoji_json_write(self, content):
        with open(self.json_path, 'w') as file:
            json.dump(content, file)
            file.close()
            pass
    
    def obtain_emoji(self, name):
        json_data = self.emoji_json_load()
        for key in json_data.keys():
            if name in json_data[key][2]:
                return json_data[key][0]
        return 0
    
    def alias_list(self):
        json_data = self.emoji_json_load()
        aliases = []
        for key in json_data.keys():
            for val in json_data[key][2]:
                aliases.append(val)

        return aliases

    def emoji_list(self):
        json_data = self.emoji_json_load()
        response = '**Emoji List :notepad_spiral:** (Give me suggestions)\n\n'
        for item in json_data.keys():
            value = '**Name: {}**\n> Accepted Aliases: {}\n> Description: {} \n\n'.format(item,json_data[item][2], json_data[item][1])
            response+=value

        
        return response
