from PepperLibrary import Settings
from os import path
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from html import HTML
import socket

from PIL import Image, ImageOps

basepath = path.dirname(__file__)

def pad_image(filename, desired_size, color='white'):
    image = Image.open(filename)
    print(image.size)
    desired_size = tuple(desired_size)
    print(desired_size)
    try:
        image = ImageOps.pad(image, desired_size, method=3, color=color, centering=(0.5, 0.5))
        image.save(filename)
    except:
        pass

def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname : ",host_name)
        print("IP : ",host_ip)
        return(host_ip)
    except:
        print("Unable to get Hostname and IP")

def html_message(header, message):
    h = HTML('h1',header)
    m = HTML('p', message)
    text = str(h) + str(m)
    f = open(path.join(Settings.image_folder, 'index.html'),'w')
    f.write(text)
    f.close()
    url = 'http://' + Settings.computer_ip + ':8000'
    return url


def read_animations():
    animations = {}
    full_path = path.join(basepath, 'animations.csv')
    f = open(full_path, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.rstrip('\n')
        line = line.replace(' ', '')
        parts = line.split('\t')
        animations[parts[0]] = parts[1]
    return animations

def svg2png(filename):
    base = path.splitext(filename)[0]
    png_file = base + '.png'
    drawing = svg2rlg(filename)
    renderPM.drawToFile(drawing, png_file, fmt="PNG")
    pad_image(png_file, Settings.tablet_resolution)

def get_url(image):
    base, ext = path.splitext(image)
    ext = ext.lower()
    if ext == '.svg':
        svg2png(path.join(Settings.image_folder, image))
        image = base + '.png'

    # for this to work, run a http server in the image folder
    # python3 -m http.server
    url = 'http://' + Settings.computer_ip + ':8000/' + image
    return url



def annotate_text(text, label):
    animations = read_animations()
    label_is_animation = True
    if animations.has_key(label): label = animations[label]
    if not animations.has_key(label): label_is_animation = False

    if label_is_animation:
        return "^start(%s) %s ^wait(%s)" % (label, text, label)
    if not label_is_animation:
        return "^startTag(%s) %s ^waitTag(%s)" % (label, text, label)



if __name__ == "__main__":
    get_Host_name_IP()

# def tag_text(text, tag):
#     return "^startTag(%s) %s ^waitTag(%s)" % (tag, text, tag)
#
# def ani_text(text, animation):
#     if not animation.startswith('animations'): animation =  'animations/' + animation
#     return "^start(%s) %s ^wait(%s)" % (animation, text, animation)
