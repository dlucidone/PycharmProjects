"""import tkinter
import tkinter.filedialog
def get_dir():
    return tkinter.FileDialog.askdirectory(dir_opt)


"""
'''
import os
import time
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror

global dir_name
class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Example")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S)

        self.button = Button(self, text="Browse", command=self.load_file, width=10)
        self.button.grid(row=1, column=0, sticky=W)

    def load_file(self):
        fname = askdirectory()
        dir_name = fname
        if fname:
            try:
                print(fname)
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return


if __name__ == "__main__":
        MyFrame().mainloop()
        if os.system(zip_command) == 0:
            print('Successful backup to', dir_name)

        else:
            print('Backup FAILED')





source = [dir_name]
#source = ['/Users/Dlucidone/Documents/imp']
target_dir = '/Users/Dlucidone/Documents/'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
comment = input('Enter a comment --> ')
if len(comment) == 0:

   target = today + os.sep  + '.zip'
else:
     target = today + os.sep  + '_' + \
         comment.replace(' ', '_') + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
print('Successfully created directory', today)

zip_command = "zip -r {0} {1}".format(target,' '.join(source))

print("Zip command is:")
print(zip_command)
print("Running:")


   if os.system(zip_command) == 0:
        print('Successful backup to', target)

    else:
     print('Backup FAILED')'''



'''

from tkinter import *
from tkinter.filedialog import askdirectory
import os
import time

source1 = askdirectory()
print(source1)
source = [source1]
target_dir = '/Users/Dlucidone/Documents/'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
comment = "ZippedDir"
if len(comment) == 0:

   target = today + os.sep  + '.zip'
else:
     target = today + os.sep  + '_' + \
         comment.replace(' ', '_') + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
print('Successfully created directory', today)

zip_command = "zip -r {0} {1}".format(target,' '.join(source1))

print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')


'''
from tkinter import *
from tkinter.filedialog import askdirectory
import os
import time

source1 = askdirectory()
print(source1)
source = [str(source1)]
target_dir = '/Users/Dlucidone/Documents/'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
comment = "zippingDir"#input('Enter a comment --> ')
if len(comment) == 0:

   target = today + os.sep  + '.zip'
else:
     target = today + os.sep  + '_' + \
         comment.replace(' ', '_') + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
print('Successfully created directory', today)

zip_command = "zip -r {0} {1}".format(target,' '.join(source))

print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')