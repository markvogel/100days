import glom

target = {'galaxy': {'system': {'planet': 'jupiter'}}}
target2 = {
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
target3 = {"menu": {
    "id": "file",
    "value": "File",
    "popup": {
        "menuitem": [
            {"value": "New", "onclick": "CreateNewDoc()"},
            {"value": "Open", "onclick": "OpenDoc()"},
            {"value": "Close", "onclick": "CloseDoc()"}
        ]
    }
}}


# https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
def read_file(file_to_read):
    with open(f'{file_to_read}.txt', 'r') as open_file:
        all_text = open_file.read()
        return all_text


if __name__ == '__main__':
    # print(glom.glom(target2, 'glossary.GlossDiv.GlossList.GlossEntry.Abbrev'))
    # print(glom.glom(target3, 'menu.popup.menuitem'))
    # namestext = read_file('nameslist')
    # nameslist = (namestext.split(sep='\n'))
    # print(len(nameslist))
    training_text = read_file('Training_01')
    training_text_list = (training_text.split(sep='\n'))
    x = [i.split(sep='/') for i in training_text_list]
    y = [x[1][2] for a in x]
    y = []
    for a in range(len(x)):
        y.append(x[a][2])
    set_y = set(y)
    print(sorted(set_y))
    # TODO need to make this work with a dictionary and output the count of each key
