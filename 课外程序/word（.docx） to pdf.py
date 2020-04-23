from os import path, remove
from tkinter import *
from tkinter import messagebox, filedialog
from win32com import client

def docx2pdf(docx_name, pdf_name):
    '''
    word文件转pdf
    :param doc_name: word文件名称
    :param pdf_name: 转换后pdf文件名称
    :return:
    '''
    try:
        word = client.DispatchEx("Word.Application")
        if path.exists(pdf_name):
            remove(pdf_name)
        if path.exists(docx_name):
            worddocx = word.Documents.Open(docx_name, ReadOnly = 1)
            worddocx.SaveAs(pdf_name, FileFormat=17)
            worddocx.Close()
            word.Quit()

        else:
            messagebox.showinfo(title='提示', message='文件不存在')
    except:
        messagebox.showinfo(title='提示', message='未知原因导致转换失败')


def openfile():
    file = filedialog.askopenfilename(title="打开文件", filetypes=[('All Files', '*.docx')])
    filespath_text.set(file)


def on_click():
    filepath = filespath_text.get()
    if filepath[-4:] == 'docx':
        pdf_name = filepath.replace('docx', 'pdf')
        docx_name = filepath.replace("\\", "/")
        docx2pdf(docx_name, pdf_name)
    else:
        messagebox.showinfo(title='提示', message='文件不存在或类型错误(*.docx)')
if __name__=='__main__':
    # UI
    root = Tk()
    root.title("@ LYL")
    root.geometry('265x66')
    root.resizable(width=False, height=False)

    filespathL = Label(root, text="path:", font=11)
    filespathL.grid(row=0, column=0, sticky=E)
    filespath_text = StringVar()
    filespathE = Entry(root, textvariable=filespath_text, font=11)
    filespath_text.set("")
    filespathE.grid(row=0, column=1, sticky=E)

    Button(root, bd=5, text="open", font=11, command=openfile).grid(row=1, column=0, sticky=E)
    Button(root, bd=5, text="word2pdf", font=11, command=on_click).grid(row=1, column=1, sticky=E)
    root.mainloop()