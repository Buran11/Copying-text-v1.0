import tkinter as tk
from widget import second_frame, entry_second_frame, label_second_frame
from widget import text_work_field, button_app, label_exception

class CopyringTextApp(tk.Tk):#Copyring_text v1.0: Класс приложения
     '''Приложение Copyring_text v1.0 (created by Sli 28.11.2021)'''
     def __init__(self):#ROOT: Конструктор класса CopyringTextApp и инициализация приложения
          super().__init__()          
          self.geometry('640x480')
          self.resizable(width=False, height=False)
          self.title('Copyring_text v1.0 (created by Sli)')
          self.iconbitmap('Files\\icon.ico')
          #Точки запуска виджетов           
          self.first_frame()
          second_frame(self)
          entry_second_frame(self)
          label_second_frame(self)
          text_work_field(self)
          button_app(self) 
          label_exception(self)

     def first_frame(self):#FIRST_FRAME: Основная рамка приложения
          self.frame_app = tk.Frame(self, border=5)
          self.frame_app.columnconfigure(list(range(3)), minsize=1)
          self.frame_app.rowconfigure(list(range(5)), minsize=1)
          self.frame_app.grid(row=0, column=0)


def mainloop_app():#Цикл mainloop
     root = CopyringTextApp()
     root.mainloop()