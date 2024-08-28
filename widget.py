import os
import tkinter as tk

def second_frame(self):#SECOND_FRAME: Внутренняя рамка и Рабочий стол
    self.frame_buttons = tk.Frame(self.frame_app, border=5)
    self.frame_buttons.columnconfigure(list(range(2)), minsize=10)
    self.frame_buttons.rowconfigure(list(range(10)), minsize=36)
    self.frame_buttons.grid(row=1, column=0, sticky='N')

def entry_second_frame(self):#ENTRY: Поле ввода количества копий и текст названия поля
    self.lbl_quantity_copy_txt = tk.Label(
        self.frame_buttons,
        text='Kоличество копий текста:'
    )                   
    self.ent_quantity_copy = tk.Entry(
        self.frame_buttons, width=7
    )
    self.ent_quantity_copy.insert(0, '0')
    self.lbl_quantity_copy_txt.grid(row=1, column=0, sticky='W') 
    self.ent_quantity_copy.grid(row=1, column=1, sticky='E')

def label_second_frame(self):#LABEL: Виджиты основного поля ввода текста
    self.lbl_header = tk.Label(
        self.frame_app,
        text='ПОЛЕ ВВОДА: Введите в данное поле нужный текст (UTF-8):'
    )                         
    self.lbl_menu_text = tk.Label(
        self.frame_buttons,
        text='Рабочее место:',
        font=('Calibry', 15)
    )
    self.lbl_delete_file_text = tk.Label(
        self.frame_buttons,
        text='"text_output.txt" удалён!',
        fg='green'
    )
    self.lbl_header.grid(row=0, column=2, sticky='W')
    self.lbl_menu_text.grid(row=0, column=0, sticky='W')

def text_work_field(self):#TEXT: Поле ввода текста(скролинг),текст обозначения и ИСКЛЮЧЕНИЯ
    self.txt_input_field = tk.Text(
        self.frame_app, width=50, height=27
    )
    #Боковой скролл
    self.scroll_y = tk.Scrollbar(
        self.frame_app, orient=tk.VERTICAL,
        command=self.txt_input_field.yview
    )
    self.txt_input_field.configure(yscrollcommand=self.scroll_y.set)
    self.scroll_y.grid(row=1, column=2, sticky='N,S,E')
    self.txt_input_field.grid(row=1, column=2, sticky='W')

def button_app(self):#BUTTON: Реализация кнопок
    def btn_copying():#КНОПКА 1 Копировать текст:
        #Надписи оповещения и исключения удаляются                              
        self.lbl_exception_quantity_copy_type_error.grid_remove()
        self.lbl_exception_quantity_equal_zero.grid_remove()
        self.lbl_exception_quantity_less_zero.grid_remove()
        self.lbl_exception_absence_file.grid_remove()
        self.lbl_delete_file_text.grid_remove()     
        while True:          
            try:                            
                self.text = self.txt_input_field.get('1.0', tk.END)                                                                 
                self.count_value = 0
                if int(self.ent_quantity_copy.get()) == 0:
                    #Выводим Исключение ent_quantity_copy равен 0
                    self.lbl_exception_quantity_equal_zero.grid(row=2, column=0, sticky='W')
                    break
                elif int(self.ent_quantity_copy.get()) < 0:
                    #Выводим Исключение ent_quantity_copy меньше 0
                    self.lbl_exception_quantity_less_zero.grid(row=2, column=0, sticky='W')
                    break
                elif int(self.ent_quantity_copy.get()) > 0:
                    #Правильный ввод данных в ent_quantity_copy больше 0                                                                                                                                             
                    while self.count_value < int(self.ent_quantity_copy.get()):          
                        self.count_value += 1        
                        with open('Result_file\\text_output.txt', 'a', encoding='utf-8') as self.file_txt_out:
                            self.file_txt_out.writelines([str(self.text)])                                   
                    os.startfile('Result_file\\text_output.txt')
                    #После копирования возвращаем значение 0 переменной ent_quantity_copy
                    self.ent_quantity_copy.delete(0, 5)
                    self.ent_quantity_copy.insert(0, '0')                                                  
                    break                                             
            except ValueError:
                    #Выводим Исключение Ввод неверного типа данных в ent_quantity_copy                            
                    self.lbl_exception_quantity_copy_type_error.grid(row=2, column=0, sticky='W')
                    break
    self.lbl_btn_copy = tk.Label(
            self.frame_buttons,
            text='Копировать текст:'
    )
    self.btn_copy = tk.Button(     
        self.frame_buttons,     
        width=5, height=1, text='1',
        bg='#00EB5A', fg='black',
        activebackground='#47EE87', activeforeground='black',
        command=btn_copying
    )
    self.lbl_btn_copy.grid(row=3, column=0, sticky='w')
    self.btn_copy.grid(row=3, column=1, sticky='N')

    def btn_cleaner_txt_input_field():#КНОПКА 2 Очистить поле ввода:
        self.txt_input_field.delete(0.1, tk.END)                               
    self.lbl_btn_cleaner = tk.Label(
        self.frame_buttons,
        text='Очистить поле ввода:'
    )
    self.btn_cleaner = tk.Button(     
        self.frame_buttons,
        width=5, height=1, text='2',
        bg='#EB1F13', fg='white',
        activebackground='#EE625A', activeforeground='white',
        command=btn_cleaner_txt_input_field
    )                              
    self.lbl_btn_cleaner.grid(row=5, column=0, sticky='W')
    self.btn_cleaner.grid(row=5, column=1, sticky='N')

    def btn_delete_text_output_file():#КНОПКА 3 Удалить файл "text_output.txt":
        #Надписи оповещения и исключения удаляются
        self.lbl_exception_quantity_copy_type_error.grid_remove()
        self.lbl_exception_quantity_equal_zero.grid_remove()
        self.lbl_exception_quantity_less_zero.grid_remove()
        self.lbl_exception_absence_file.grid_remove()
        self.lbl_delete_file_text.grid_remove()
        for self.adress, self.dir, self.files in os.walk('Result_file\\'):
            if len(self.files) == 0:
                    #Вывод Исключение файл 'text_output.txt' отсутствует в папке 'Result_file\\'
                    self.lbl_exception_absence_file.grid(row=2, column=0, sticky='W') 
            for self.j in self.files:                                                                                                                                      
                    if self.j == 'text_output.txt':                                                  
                        os.remove('Result_file\\text_output.txt')
                        #Вывод оповещения о том, что файл 'text_output.txt' удалён из папки 'Result_file\\'
                        self.lbl_delete_file_text.grid(row=2, column=0, sticky='W')
    self.lbl_btn_delete = tk.Label(
        self.frame_buttons,
        text='Удалить файл "text_output.txt":'
    )
    self.btn_delete = tk.Button(     
        self.frame_buttons,
        width=5, height=1, text='3',
        bg='#EB1F13', fg='white',
        activebackground='#EE625A', activeforeground='white',
        command=btn_delete_text_output_file
    )                              
    self.lbl_btn_delete.grid(row=6, column=0, sticky='W')
    self.btn_delete.grid(row=6, column=1, sticky='N')

    def btn_open_dir():#КНОПКА 4 Директория с "text_output.txt":
        os.system('explorer.exe Result_file\\')
    self.lbl_btn_open = tk.Label(
        self.frame_buttons,
        text='Директория с "text_output.txt":'
    )
    self.btn_open = tk.Button(     
        self.frame_buttons,
        width=5, height=1, text='4',
        bg='#019DDB', fg='black',
        activebackground='#44B5E1', activeforeground='black',
        command=btn_open_dir
    )                              
    self.lbl_btn_open.grid(row=7, column=0, sticky='W')
    self.btn_open.grid(row=7, column=1, sticky='N')

    def btn_info_app():#КНОПКА Помощь
        os.startfile('Files\\READ_ME.txt')
    self.btn_info = tk.Button(     
        self.frame_buttons,
        width=10, height=1, text='Помощь',
        command=btn_info_app
    )                              
    self.btn_info.grid(row=9, column=0, sticky='W')

    def btn_exit_app():#КНОПКА Выход
        self.destroy()    
    self.btn_exit = tk.Button(     
        self.frame_buttons,
        width=10, height=1, text='Выход',
        command=btn_exit_app
    )
    self.btn_exit.grid(row=10, column=0, sticky='W')

def label_exception(self):#EXСEPTION: Исключения
    self.lbl_exception_quantity_copy_type_error = tk.Label(
        self.frame_buttons,
        text='Неверный типа данных!',
        fg='red'
    )
    self.lbl_exception_absence_file = tk.Label(
        self.frame_buttons,
        text='"text_output.txt" отсутствует!',
        fg='red'
    )
    self.lbl_exception_quantity_equal_zero = tk.Label(
        self.frame_buttons,
        text='Количество копий = 0!',
        fg='red'
    )
    self.lbl_exception_quantity_less_zero = tk.Label(
        self.frame_buttons,
        text='Количество копий < 0!',
        fg='red'
    )