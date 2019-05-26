#calculates quadratic function and shows data with matplotlib

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkf
import numpy as np
import math
import sys



class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.page_1 = StartPage(container, self)
        self.page_1.grid(row=0, column=0, sticky="nsew")
        self.page_2 = QFunction(container, self)
        self.page_2.grid(row=0, column=0, sticky="nsew")

        self.show_frame(1)

        print(tkf.families())



    def show_frame(self, cont):
        if (cont == 1):
            frame = self.page_1
            frame.tkraise()
            self.page_2.funClear()

        if (cont == 2):
            frame = self.page_2
            frame.tkraise()




class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Lambda 1.2 alpha", fg="#000c33", font=("Helvetica", 14, "bold"))
        #label.pack(padx=10, pady=10)
        label.grid(row=1, column=1, columnspan=3, sticky='we', pady=34)

        # c = tk.Canvas(self, width=250, height=200)
        # c.pack()
        # c.create_rectangle(50,50,100,100, fill="orange")
        # but = tk.Button(self, text = "Quit", command = self.quit, anchor = 'w')
        # but.configure(width = 10, activebackground = "#33B5E5", relief = 'flat')
        # but_w = c.create_window(10, 10, anchor='nw', window=but)

        s = ttk.Style()
        s.configure('TButton', background='pink', foreground='red')

        button_1 = tk.Button(self, width=24, height=2, font=("Helvetica", 9, "bold"), text="QUAD. FUN.",
        command=lambda: controller.show_frame(2))
        #button_1.config(fg="#000c33",  highlightbackground="#001866")
        button_1.grid(row=6, column=1, padx=21, pady=1)

        button_2 = tk.Button(self, width=24, height=2, font=("Helvetica", 9, "bold"), text="QUIT",
        command=lambda: sys.exit())
        #self.btn_img = tk.PhotoImage(file="res/pic_1.png")
        #set width to grid :
        #button_2.config(width="164", height="42")
        button_2.grid(row=7, column=1, padx=21, pady=1)

        canvas = tk.Canvas(self, height=360, width=600, bg='black')
        #canvas.pack(padx=4, pady=10)
        canvas.grid(row=2, column=2, columnspan=2, rowspan=24, padx=21, pady=2, sticky='we')

        self.photo = tk.PhotoImage(file="res/pic_1.png")
        canvas.create_image(301, 200, image=self.photo, anchor='center')

        #button_3 = ttk.Button(self, style='TButton', text='Button')
        #button_3.pack()


class QFunction(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, fg="#000c33", text="Quadratic function - Lambda", font=("Helvetica", 14, "bold"))
        label.grid(row=1, column=1, columnspan=5, sticky='we', pady=34)

        back_but= tk.Button(self, width=24, height=2, font=("Helvetica", 9, "bold"), text="BACK",
        command=lambda: controller.show_frame(1))
        back_but.grid(row=7, column=1, rowspan=1, padx=21, pady=1)

        button_2 = tk.Button(self, width=24, height=2, font=("Helvetica", 9, "bold"), text="QUIT",
        command=lambda: sys.exit())
        button_2.grid(row=8, column=1, padx=21, pady=1)

        form = tk.Frame(self, highlightbackground="grey",  highlightthickness=1, bd= 0, width=600)
        form.grid(row=2, column=2, columnspan=4, rowspan=8, padx=21, pady=2, sticky='we')
        #form.configure(width=500, height=100)
        #form.grid_propagate(0)

        cal_but= tk.Button(self, width=24, height=2, font=("Helvetica", 9, "bold"), text="CALCULATE",
        command=lambda: self.calc(self.en_a.get(), self.en_b.get(), self.en_c.get()))
        #cal_but.configure(width='20')
        cal_but.grid(row=10, column=2, rowspan=1, padx=21, pady=2, sticky='w')

        label_1 = tk.Label(form, text="Enter values:", font=("Verdana", 10))
        label_1.grid(row=0, column=0, columnspan=2, sticky='ew')

        label_2 = tk.Label(form, text="('a' can't be equal 0)", font=("Verdana", 8))
        label_2.grid(row=1, column=0, columnspan=2, sticky='ew')

        lab_a = tk.Label(form, text="a = ", font=("Verdana", 10))
        lab_a.grid(row=2, column=0, sticky='w')
        self.en_a = tk.Entry(form)
        self.en_a.grid(row=2, column=1)

        lab_b = tk.Label(form, text="b = ", font=("Verdana", 10))
        lab_b.grid(row=3, column=0, sticky='w')
        self.en_b = tk.Entry(form)
        self.en_b.grid(row=3, column=1)

        lab_c = tk.Label(form, text="c = ", font=("Verdana", 10))
        lab_c.grid(row=4, column=0, sticky='w')
        self.en_c = tk.Entry(form)
        self.en_c.grid(row=4, column=1)

        lab_d = tk.Label(form, text="del = ", font=("Verdana", 10))
        lab_d.grid(row=5, column=0, sticky='w')
        self.lab_del = tk.Label(form, text=" ", font=("Verdana", 10))
        self.lab_del.grid(row=5, column=1, sticky='w')

        lab_x1 = tk.Label(form, text="x1 = ", font=("Verdana", 10))
        lab_x1.grid(row=6, column=0, sticky='w')
        self.x1 = tk.Label(form, text=" ", font=("Verdana", 10))
        self.x1.grid(row=6, column=1, sticky='w')

        lab_x2 = tk.Label(form, text="x2 = ", font=("Verdana", 10))
        lab_x2.grid(row=7, column=0, sticky='w')
        self.x2 = tk.Label(form, text=" ", font=("Verdana", 10))
        self.x2.grid(row=7, column=1, sticky='w')

        self.lab_inf = tk.Label(form, text=" ", font=("Verdana", 10))
        self.lab_inf.grid(row=8, column=0, sticky='w')

        self.f = Figure(figsize=(4,4), dpi=110)
        self.pl = self.f.add_subplot(111)
        self.frame = tk.Frame(self)
        self.frame.grid(row=11, column=2, columnspan=2, rowspan=15, padx=21, pady=2, sticky='we')
        self.canvas = FigureCanvasTkAgg(self.f, self.frame)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame)

        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)



    def funClear(self):

        self.pl.cla()   #clear current matplotlib canvas
        self.canvas.draw()
        self.lab_inf.config(text = "")
        self.lab_del.config(text = "")
        self.x1.config(text = "")
        self.x2.config(text = "")

        self.en_a.delete(0, 'end')
        self.en_b.delete(0, 'end')
        self.en_c.delete(0, 'end')


    def calc(self, var_a=0, var_b=0, var_c=0):

        self.pl.cla()   #clear current matplotlib canvas
        self.canvas.draw()
        self.lab_inf.config(text = "")

        try:
            a = float(var_a)
            b = float(var_b)
            c = float(var_c)

            delta = (b**2) - 4 * a * c
            if (delta > 0):
                d = str(delta)
                del_sqr = math.sqrt(delta)
                x1 = (-b - (del_sqr)) / (2 * a)
                x2 = (-b + (del_sqr)) / (2 * a)

                #x1 = [0,1,2,3,4]
                #y1 = [0,2,4,6,8]
                #pl.plot(x1, y1)

                if (x1>x2):
                    dx1 = x2 - 3
                    dx2 = x1 + 3
                else:
                    dx1 = x1 - 3
                    dx2 = x2 + 3

                ax = []
                ay = []

                for x in np.arange(dx1, dx2, 0.1):
                    y = a * (x**2) + b * x + c
                    ax.append(x)
                    ay.append(y)

                self.pl.plot(ax ,ay, label='quadrat fun')
                self.pl.axhline(0, linewidth=1, color='black')
                self.pl.axvline(0, linewidth=1, color='black')
                self.canvas.draw()

                self.toolbar.update()
                self.canvas._tkcanvas.pack()

            else:
                d = 0
                x1 = 0
                x2 = 0
                self.lab_inf.config(text =
                "Delta has to be greater than 0. Try other numbers")
        except:
            if (var_a == '0'):
                self.lab_inf.config(text = "a can't be 0")
            else:
                self.lab_inf.config(text = "Insert only number. ('a' can't be equal 0)")

            d = 0
            x1 = 0
            x2 = 0

        self.lab_del.config(text = d)
        self.x1.config(text = "%.2f" % (x1))
        self.x2.config(text = "%.2f" % (x2))

    #end of calc function

a = MainApp()
a.title("Lambda")
a.mainloop()
