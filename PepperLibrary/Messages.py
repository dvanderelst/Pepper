import Settings
from html import HTML
from os import path


# def html_message(header, message):
#     h = HTML('h1',header)
#     m = HTML('p', message)
#     text = str(h) + str(m)
#     f = open(path.join(Settings.image_folder, 'index.html'),'w')
#     f.write(text)
#     f.close()
#     url = 'http://' + Settings.computer_ip + ':8000'
#     return url


def html_message(header, message):
    f = open(path.join(Settings.image_folder, 'template.html'),'r')
    contents = f.read()
    f.close()
    contents = contents.replace('xxx', header)
    contents = contents.replace('yyy', message)
    f = open(path.join(Settings.image_folder, 'index.html'),'w')
    f.write(contents)
    url = 'http://' + Settings.computer_ip + ':8000'
    return url

