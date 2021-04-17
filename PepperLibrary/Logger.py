from PepperLibrary import HTML
from PepperLibrary import Misc
from PepperLibrary import Settings
import time
import os.path as path
import webbrowser

input_color = "#a9cce3"
output_color = "##aeb6bf"

warning_color = '#f5cba7'
error_color = '#f5b7b1'
info_color = '#a2d9ce'

class Logger:
    def __init__(self):
        self.table = HTML.Table(header_row=['Time', 'Text'])
        self.print_comments = True

    def add(self, text, level='i', pre=False):
        if pre: text = '<pre>' + text + '</pre>'
        time_string = time.asctime()
        c = info_color
        if level.startswith('w'): c = warning_color
        if level.startswith('e'): c = error_color
        time_stamp = HTML.TableCell(time_string, bgcolor=c)
        text = HTML.TableCell(text, bgcolor=c)
        self.table.rows.append([time_stamp, text])

    def write(self, file_name):
        htmlcode = str(self.table)
        out_file = path.join(Settings.log_dir, file_name)
        f = open(out_file, 'w')
        f.write(htmlcode)
        f.close()

    def view(self):
        out_file = path.join(Settings.log_dir, 'temp.html')
        self.write(out_file)
        webbrowser.open(out_file)

# l = logger()
# l.add('well', 'c')
# l.add('well well', 'step')
# l.add('sfdfd\r\n    fsdsf', 'o')
# l.view()
