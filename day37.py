# https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

import day33

url = 'https://www.nytimes.com/'


def write_to_file(file_name: str, file_text: str):
    with open(f'{file_name}.txt', 'w') as open_file:
        open_file.write(file_text)


if __name__ == '__main__':
    website_text = ''
    for title in day33.get_titles(day33.get_html(url)):
        if 'Site' not in title.text:
            website_text += title.text + '\n'
    write_to_file('nytimes', website_text)
