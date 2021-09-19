import os
import subprocess
import sys
import socket
import time
from tkinter import *
from tkinter import ttk

s = socket.socket()
root = Tk()
root.title('Scroll test')
root.geometry("1410x600")


def set_connection():
    try:
        print(Addr_etr.get())

        adr = (Addr_etr.get())
        pn = (port_etr.get())
        print(type(pn))
        s.connect((adr, int(pn)))
        # c.connect(('localhost', 9999))
        # name=input('Enter your name')
        # c.send(name.encode())
        # print(c.recv(1024).decode())
        print("Connected to server")
    except Exception as e:
        print(e)


def re_rename(rt, lokn, fl, etr):
    try:
        os.rename(f'{lokn}/{fl}', f'{lokn}/{etr}')
        rt.destroy()
        get_files()
        pass
    except Exception as e:
        print(e)


def re_name(lokn, fl):
    try:
        rt = Tk()
        rt.geometry("400x200")
        lbl = Label(rt, text='Current Name: ')
        lbl.grid(row=0, column=0, sticky=E, padx=5, pady=5)
        lbl1 = Label(rt, text=fl)
        lbl1.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        lbl2 = Label(rt, text="Enter New Name: ")
        lbl2.grid(row=1, column=0, sticky=E, padx=5, pady=5)
        etr = Entry(rt)
        etr.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        btn = Button(rt, text='Rename', command=lambda rt=rt, lokn=lokn, fl=fl: re_rename(rt, lokn, fl, etr.get()))
        btn.grid()

        rt.mainloop()
    except Exception as e:
        print(e)


# = 0
def size(locn, name):
    try:
        sz = 0
        if os.path.isdir(f'{locn}/{name}'):
            for path, dirs, files in os.walk(f'{locn}/{name}'):
                for f in files:
                    fp = os.path.join(path, f)
                    sz += os.path.getsize(fp)
        else:
            sz = os.path.getsize(f'{locn}/{name}')
        print(sz)
        if sz > 1024 * 1024 * 1024:
            sz = str(round(sz / (1024 * 1024 * 1024), 2)) + 'GB'
        elif sz > 1024 * 1024:
            sz = str(round(sz / (1024 * 1024), 2)) + 'MB'
        elif sz > 1024:
            sz = str(round((sz / 1024), 2)) + 'KB'
        else:
            sz = str(sz) + 'B'
        print(sz)
        rt = Tk()
        rt.geometry('300x200')
        lbl = Label(rt, text=f'Size of {name}: ')
        lbl.grid(row=0, column=0, sticky=E, padx=5, pady=5)
        lbl1 = Label(rt, text=f'{sz}')
        lbl1.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        rt.mainloop()
    except Exception as e:
        print(e)


def date(locn, name):
    try:
        adt = time.ctime(os.path.getatime(f'{locn}/{name}'))
        mdt = time.ctime(os.path.getmtime(f'{locn}/{name}'))
        cdt = time.ctime(os.path.getctime(f'{locn}/{name}'))
        rt = Tk()
        lbl = Label(rt, text=f'last accessed time of {name}: ')
        lbl1 = Label(rt, text=f'last modified time of {name}: ')
        lbl2 = Label(rt, text=f'{name} created time: ')
        lbl.grid(row=2, column=0, sticky=E, padx=5, pady=5)
        lbl1.grid(row=1, column=0, sticky=E, padx=5, pady=5)
        lbl2.grid(row=0, column=0, sticky=E, padx=5, pady=5)
        lbl3 = Label(rt, text=f'{adt}')
        lbl4 = Label(rt, text=f'{mdt}')
        lbl5 = Label(rt, text=f'{cdt}')
        lbl5.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        lbl4.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        lbl3.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        rt.mainloop()
    except Exception as e:
        print(e)


def open_dir(lokn, fl):
    try:
        lcn_etr.delete(0, END)
        lcn_etr.insert(0, f'{lokn}/{fl}')
        get_files()
    except Exception as e:
        print(e)


def open_file(lokn, fl):
    try:
        if '.mp4' or '.mp3' in fl:
            ved = '/home/bharath/Videos'
            subprocess.Popen([ved, f'{lokn}/{fl}'])
    except Exception as e:
        print(e)


def type_fl(lokn, fl):
    try:
        if '.' not in fl:
            if os.path.isdir(os.path.join(lokn, fl)):
                tp = 'Directory'
            else:
                tp = 'File'
        ext = fl.split('.')
        ext = '.' + ext[-1]
        d = {'.apk': 'Android Package$Executable File ', '.cpp': 'C plus plus file$Executable File',
             '.java': 'Java File$Executable File', '.bat': 'Batch file$Executable File ',
             '.bin': 'Binary file$Executable File ', '.cgi': 'Perl script file$Web File ',
             '.com': 'MS-DOS command file$Executable File ', '.exe': 'Executable file$Executable File ',
             '.jar': 'Java Archive file$Executable File ', '.py': 'Python file$Executable File ',
             '.wsf': 'Windows Script File$Executable File ', '.aif': 'AIF/Audio Interchange audio file$Audio File ',
             '.cda': 'CD audio track file$Audio File ', '.iff': 'Interchange File Format$Audio File ',
             '.mid': 'MIDI audio file$Audio File ', '.midi': 'MIDI audio file$Audio File ',
             '.mp3': 'MP3 audio file$Audio File ', '.mpa': 'MPEG-2 audio file$Audio File ',
             '.wav': 'WAVE file$Audio File ', '.wma': 'Windows Media audio file$Audio File ',
             '.wpl': 'Windows Media Player playlist$Audio File ', '.avi': 'Audio Video Interleave File$Audio File ',
             '.flv': 'Adobe Flash Video File$Video File ', '.h264': 'H.264 video File$Video File ',
             '.m4v': 'Apple MP4 video File$Video File ', '.mkv': 'Matroska Multimedia Container$Video File ',
             '.mov': 'Apple QuickTime movie File$Video File ', '.mp4': 'MPEG-4 Video File$Video File ',
             '.mpg': 'MPEG video File$Video File ', '.mpeg': 'MPEG video File$Video File ',
             '.rm': 'Real Media File$Video File ', '.swf': 'Shockwave flash File$Video File ',
             '.vob': 'DVD Video Object File$Video File ', '.wmv': 'Windows Media Video File$Video File ',
             '.3g2': '3GPP2 Multimedia File$Video File ', '.3gp': '3GPP multimedia File$Video File ',
             '.doc': 'Microsoft Word File$Text File ', '.docx': 'Microsoft Word file$Text File ',
             '.odt': 'OpenOffice Writer document file$Text File ', '.msg': 'Outlook Mail Message$Text File ',
             '.pdf': 'PDF file$Text File ', '.rtf': 'Rich Text Format File$Text File ',
             '.tex': 'A LaTeX document file$Text File ', '.txt': 'Plain text file$Text File ',
             '.wks': 'Microsoft Works Word Processor Document file$Text File ',
             '.wps': 'Microsoft Works Word Processor Document file$Text File ',
             '.wpd': 'WordPerfect document$Text File$Text File ',
             '.ods': 'OpenOffice Calc spreadsheet file$Spreadsheet File ',
             '.xlr': 'Microsoft Works spreadsheet file$Spreadsheet File ',
             '.xls': 'Microsoft Excel file$Spreadsheet File ',
             '.xlsx': 'Microsoft Excel Open XML spreadsheet file$Spreadsheet File ',
             '.key': 'Keynote presentation$Presentation File ',
             '.odp': 'OpenOffice Impress presentation file$Presentation File ',
             '.pps': 'PowerPoint slide show$Presentation File ', '.ppt': 'PowerPoint presentation$Presentation File ',
             '.pptx': 'PowerPoint Open XML presentation$Presentation File ',
             '.accdb': 'Access 2007 Database File$Database File ', '.csv': 'Comma separated value file$Database File ',
             '.dat': 'Data file$Database File ', '.db': 'Database file$Database File ',
             '.dbf': 'Database file$Database File ', '.log': 'Log file$Database File ',
             '.mdb': 'Microsoft Access database file$Database File ', '.pdb': 'Program Database$Database File ',
             '.sav': 'Save file (e.g. game save file)$Database File ',
             '.sql': 'SQL/Structured Query Language database file$Database File ',
             '.tar': 'Linux / Unix tarball file archive$Database File ', '.bak': 'Backup file$System File ',
             '.cab': 'Windows Cabinet file$System File ', '.cfg': 'Configuration file$System File ',
             '.cpl': 'Windows Control panel file$System File ', '.cur': 'Windows cursor file$System File ',
             '.dll': 'DLL file$System File ', '.dmp': 'Dump file$System File ',
             '.drv': 'Device driver file$System File ', '.icns': 'macOS X icon resource file$System File ',
             '.ico': 'Icon file$Image File ', '.ini': 'Initialization file$System File ',
             '.lnk': 'Windows shortcut file$System File ', '.msi': 'Windows installer package$System File ',
             '.sys': 'Windows system file$System File ', '.tmp': 'Temporary file$System File ',
             '.asp': 'Active Server Page file$Web File ', '.aspx': 'Active Server Page file$Web File ',
             '.cer': 'Internet security certificate$Web File ', '.cfm': 'ColdFusion Markup file$Web File ',
             '.pl': 'Perl script file$Web File ', '.css': 'Cascading Style Sheet file$Web File ',
             '.htm': 'HTML/Hypertext Markup Language file$Web File ',
             '.html': 'HTML/Hypertext Markup Language file$Web File ', '.js': 'JavaScript file$Web File ',
             '.jsp': 'Java Server Page file$Web File ', '.part': 'Partially downloaded file$Web File ',
             '.php': 'PHP Source Code file$Web File$Web File ', '.rss': 'RSS/Rich Site Summary file$Web File ',
             '.xhtml': 'XHTML / Extensible Hypertext Markup Language file$Web File ',
             '.ai': 'Adobe Illustrator file$Image File ', '.bmp': 'Bitmap image File$Image File ',
             '.gif': 'GIF/Graphical Interchange Format image$Image File ', '.jpeg': 'JPEG image$Image File ',
             '.jpg': 'JPEG image$Image File ', '.max': '3ds Max Scene File$Image File ',
             '.obj': 'Wavefront 3D Object File$Image File ', '.png': 'PNG / Portable Network Graphic image$Image File ',
             '.ps': 'PostScript file$Image File ', '.psd': 'PSD / Adobe Photoshop Document image$Image File ',
             '.svg': 'Scalable Vector Graphics file$Image File ', '.tif': 'TIFF image$Image File ',
             '.tiff': 'TIFF image$Image File ', '.3ds': '3D Studio Scene$Image File ',
             '.3dm': 'Rhino 3D Model$Image File '}
        tp = d.get(f'{ext}', 'File$File')
        ind = tp.index('$')
        rt = Tk()
        lbl = Label(rt, text='File Type: ')
        lbl.grid(row=0, column=0, sticky=E, padx=5, pady=5)
        lbl1 = Label(rt, text=f'{tp[ind + 1:]}')
        lbl1.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        if ext != fl:
            lbl2 = Label(rt, text=f'Extension {ext}')
            lbl2.grid(row=1, column=0, sticky=E, padx=5, pady=5)
            lb3 = Label(rt, text=f'{tp[:ind]}')
            lb3.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        rt.mainloop()
    except Exception as e:
        print(e)


def download(lokn, fl):
    try:
        locn = 'down:' + f'{lokn}/{fl}'
        s.sendall(locn.encode())
        fil = open(f'{fl}', 'wb')
        sz = 0
        while True:
            info = s.recv(1024)
            print(info, len(info))
            if len(info) < 1024:
                print(info, len(info))
                fil.write(info)
                fil.close()
                print('quit')
                break

            sz += len(info)
            fil.write(info)
        print(sz, 'characters copied')
    except Exception as e:
        print(e)


def delete(locn, fl):
    try:
        lokn = 'del:' + f'{locn}/{fl}'
        s.sendall(lokn.encode())
        msg = s.recv(1024).decode()
        if msg == 'done':
            print('deleted')
            get_files()
    except Exception as e:
        print(e)


nb = 0


def delete_dir(locn, fl):
    try:
        rt = Tk()
        lbl = Label(rt, text=f'Do you really want to delete {fl} ')
        lbl.grid(row=0, column=0, padx=5, pady=5)
        lbl1 = Button(rt, text=f'Yes ', command=lambda locn=locn, fl=fl: del_dir(rt, locn, fl))
        lbl2 = Button(rt, text=f'No ', command=lambda: rt.destroy())
        lbl1.grid(row=1, column=0, padx=5, pady=5)
        lbl2.grid(row=1, column=1, padx=5, pady=5)
    except Exception as e:
        print(e)


def del_dir(rt, locn, fl):
    try:
        lokn = 'deld:' + f'{locn}/{fl}'
        s.sendall(lokn.encode())
        msg = s.recv(1024).decode()
        rt.destroy()
        if msg == 'done':
            print('deleted')
            get_files()
    except Exception as e:
        print(e)


def up_load_a(lokn_c, k):
    try:
        fl = open(lokn_c, 'rb')

        if k == 1:
            s.sendall(('upld:' + lcn_etr.get() + '/' + lokn_c.split('/')[-1] + f'{k}').encode())
        else:
            s.sendall(
                ('upld:' + lcn_etr.get() + '/' + lokn_c.split('/')[-2] + '/' + lokn_c.split('/')[-1] + f'{k}').encode())
        size = 0
        while True:
            info = fl.read(1024)
            print(info)
            if len(info) < 1:
                # c.send(b'end')
                fl.close()
                print('quit')
                break
            size += len(info)

            s.send(info)
        print(size)
        msg = s.recv(1024).decode()
        if msg == 'recv':
            print('uploaded', lokn_c.split('/')[-1])
    except Exception as e:
        print(e)


def up_load():
    try:
        lokn = up_etr.get()
        if os.path.isfile(lokn):
            k = 1
            up_load_a(lokn, k)
            get_files()

        if os.path.isdir(lokn):
            for file in os.listdir(lokn):
                print(file)
                k = 2
                up_load_a(lokn + '/' + file, k)
            get_files()
    except Exception as e:
        print(e)


def back():
    try:
        lcn = lcn_etr.get()
        l = lcn.split('/')

        s = ''

        for i in range(1, len(l)-1):
            if l[i] != '':
                s += '/'+l[i]
                continue
        if s=='':
            s='/'

        lcn_etr.delete(0, len(lcn))
        lcn_etr.insert(0, s)
        print(lcn, 'lcnetr')
        print(s, 'newlcn')
        get_files()
    except Exception as e:
        print(e)


def get_files():
    try:
        global nb
        # global i
        locn = 'locn:' + lcn_etr.get()
        s.sendall(locn.encode())
        # con=0
        for widget in second_frame.winfo_children():
            widget.destroy()
        text1 = []
        d = {}
        i = 0
        while True:

            data = s.recv(1024)
            print(data, 'data')
            data = data.decode()
            # con+=1
            # print(con)
            if data == 'endlast':
                break
            t = 0

            for file in data.split('&'):
                if file == 'endlast':
                    t = 1
                    break
                if file == '':
                    continue
                if '$' in file:
                    continue
                text1.append(f'{file}')

                if os.path.isdir(os.path.join(locn[5:], file)):
                    menubutton = Menubutton(second_frame, width=50, text=f'{file}', fg='#ff1944', bg='cyan')
                    menubutton.grid(row=nb, column=1, padx=1, pady=1)
                    menubutton.menu = Menu(menubutton, tearoff=0, activeborderwidth=25)

                    menubutton["menu"] = menubutton.menu

                    menubutton.menu.add_command(label="Rename", command=lambda i=i: re_name(locn[5:], text1[i]))

                    menubutton.menu.add_command(label="Size ", command=lambda i=i: size(locn[5:], text1[i]))
                    menubutton.menu.add_command(label="Date created", command=lambda i=i: date(locn[5:], text1[i]))
                    menubutton.menu.add_command(label="Open", command=lambda i=i: open_dir(locn[5:], text1[i]))
                    menubutton.menu.add_command(label="Type", command=lambda i=i: type_fl(locn[5:], text1[i]))
                    menubutton.menu.add_command(label="Delete", command=lambda i=i: delete_dir(locn[5:], text1[i]))
                    nb = nb + 1
                    i = i + 1
                    print(i)
                    continue

                # if os.path.isdir(os.path.join(locn[5:], file)):
                menubutton = Menubutton(second_frame, width=50, text=f'{file}',
                                        bg='blue')  # ,command=btn_clicked(os.path.join(locn, file)))
                menubutton.grid(row=nb, column=1, padx=1, pady=1)
                menubutton.menu = Menu(menubutton, tearoff=0, activeborderwidth=25)
                menubutton["menu"] = menubutton.menu

                menubutton.menu.add_command(label="Rename", command=lambda i=i: re_name(locn[5:], text1[i]))

                menubutton.menu.add_command(label="Size ", command=lambda i=i: size(locn[5:], text1[i]))
                menubutton.menu.add_command(label="Date created", command=lambda i=i: date(locn[5:], text1[i]))
                menubutton.menu.add_command(label="Download", command=lambda i=i: download(locn[5:], text1[i]))
                menubutton.menu.add_command(label="Type", command=lambda i=i: type_fl(locn[5:], text1[i]))
                menubutton.menu.add_command(label="Delete", command=lambda i=i: delete(locn[5:], text1[i]))

                nb = nb + 1
                i = i + 1
                print(i)
                #    continue
                # file_btn = tk.Button(frame1, width=300, text=f'{file}')
                # file_btn.pack()
                print(file)

            if t:
                print(nb)
                break
    except Exception as e:
        print(e)


frameh = Frame(root)
frameh.pack()
# create a main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a scroll bar to canvas
scroll_bar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
scroll_bar.pack(side=RIGHT, fill=Y)

# configure canvas
my_canvas.configure(yscrollcommand=scroll_bar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# create another frame in canvas
second_frame = Frame(my_canvas)

# add the new frame to a window in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

Addr_label = Label(frameh, text="Server Address : ")
Addr_label.grid(row=0, column=0, sticky=E, padx=10, pady=10)
Addr_etr = Entry(frameh)
Addr_etr.grid(row=0, column=1, sticky=W, padx=10, pady=10)
port_label = Label(frameh, text="Port No : ")
port_label.grid(row=0, column=2, sticky=E, padx=10, pady=10)

port_etr = Entry(frameh)
port_etr.grid(row=0, column=3, sticky=W, padx=10, pady=10)
cnt_button = Button(frameh, text="Connect", width=20, command=set_connection)
cnt_button.grid(row=0, column=4, padx=10, pady=10)
lcn_label = Label(frameh, text="Enter Location : ")
lcn_label.grid(row=0, column=5, sticky=E, padx=10, pady=10)
lcn_etr = Entry(frameh)
lcn_etr.grid(row=0, column=6, sticky=W, padx=10, pady=10)
get_files_btn = Button(frameh, text="GET files", command=get_files)
get_files_btn.grid(row=0, column=7, padx=10, pady=10)
up_label = Label(frameh, text='File location: ')
up_label.grid(row=1, column=1, sticky=E, padx=10, pady=10)
up_etr = Entry(frameh)
up_etr.grid(row=1, column=2, sticky=W, padx=10, pady=10)
up_btn = Button(frameh, text='UPLOAD', width=20, command=up_load)
up_btn.grid(row=1, column=3, padx=10, pady=10)
bc_btn = Button(frameh, text='BACK', width=20, command=back)
bc_btn.grid(row=1, column=0, sticky=W, padx=10, pady=10)
# for thing in range(100):
#    Button(second_frame,text=f'Button {thing} bro').grid(row=thing+1,column=0,pady=10,padx=10)

root.mainloop()