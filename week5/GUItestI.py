import tkinter as tk
import os
from tkinter import filedialog as fd


class MyApp(tk.Frame):  #MyApp繼承tk.Frame

    def __init__(self, master=None):
        super().__init__(master)    #引用父類別即tk.Frame中的初始化
        self.master.geometry('400x400') #設定視窗大小

        #標題
        self.master.title('110502018') #調用自身之master之tittle

        #按鈕
        self.MyButton = tk.Button(self.master, text='open  file', command=self.button_event) #設定self.button_event為按鈕事件
        self.MyButton.pack()#印到畫面上

    def button_event(self):
        #open the file
        f = fd.askopenfilename()    #開起檔案
        filename = os.path.basename(f)  #得到檔案名稱
        #更改標籤
        self.MyLabel=tk.Label(self.master,text = filename)    #設定label
        self.MyLabel.pack() #印到畫面上



root = tk.Tk()
app = MyApp(master=root)
app.mainloop()

