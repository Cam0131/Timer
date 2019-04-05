import tkinter as tk

BLUE = '#99CCFF'
YELLOW = '#FFCC00'
RED = '#FF00FF'
CLOCK = 'image.gif'

class Frame(tk.Frame):    
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)

        self.echo=tk.StringVar()
        self.m=3
        self.echo_set()

        self.master.title('Alarm')
        f_display=tk.Frame(self,relief=tk.RIDGE,bd=4)
        f_display.pack(fill=tk.X,expand=1)

        self.image=tk.PhotoImage(file=CLOCK)
        self.icon=tk.Label(f_display,image=self.image,bg=BLUE)
        self.icon.grid(row=0,column=0,rowspan=2)
        
        display=tk.Label(f_display,textvariable=self.echo,relief=tk.SUNKEN,font=('Helvetica', '24'),bg='white', width=5, anchor=tk.E)
        display.grid(row=0, column=1, rowspan=2, sticky=tk.N+tk.S)
        self.b_inc = tk.Button(f_display, font=('Helvetica', '6'), text='+', command=self.inc_time)
        self.b_inc.grid(row=0, column=2, sticky=tk.W + tk.E + tk.S, pady=1)
        self.b_dec = tk.Button(f_display, font=('Helvetica', '6'), text='-', command=self.dec_time)
        self.b_dec.grid(row=1, column=2, sticky=tk.W + tk.E + tk.N, pady=1)

        f_button=tk.Frame(self)
        f_button.pack(pady=2)
        self.b_start=tk.Button(f_button,text='Start',command=self.start)
        self.b_stop=tk.Button(f_button,text='Stop',command=self.stop,state=tk.DISABLED)
        self.b_reset=tk.Button(f_button,text='Reset',command=self.reset,state=tk.DISABLED)
        self.b_start.pack(side=tk.LEFT,padx=1)
        self.b_stop.pack(side=tk.LEFT,padx=1)
        self.b_reset.pack(side=tk.LEFT,padx=1)

        # self.min=min
        # self.echo.set('%02d:00' % (self.min))
        # self.sec=60*self.min
        # self.label=tk.Label(self,text='Click to start',font=('Helvetica','8'))
        # self.label.pack()
        # f=tk.Frame(self,relief=tk.RIDGE,bd=4)
        # f.pack(fill=tk.BOTH,expand=1)
        # display.pack(side=tk.LEFT)
        # self.bind_all('<KeyPress-s>',self.start_stop)
        # self.bind_all('<KeyPress-space>',self.reset)
    def echo_set(self):
        self.timer=60*self.m
        self.echo.set('%02d:00' % (self.m))
    
    def inc_time(self):
        self.m+=1
        self.echo_set()
    
    def dec_time(self):
        self.m-=1
        self.echo_set()
    

    def start(self):
        self.started=True
        # self.label.configure(text='Click to stop')
        if 0<self.timer<=20:
            self.icon.configure(bg=YELLOW)
        elif 0>=self.timer:
            self.icon.configure(bg=RED)
        #1000mili sec , func:self.counting
        self.after(1000, self.counting)
        self.b_start.configure(state=tk.DISABLED)
        self.b_stop.configure(state=tk.NORMAL)
        self.b_inc.configure(state=tk.DISABLED)
        self.b_dec.configure(state=tk.DISABLED)
        

    def stop(self):
        self.icon.configure(bg=BLUE)
        self.started=False
        self.b_start.configure(state=tk.NORMAL)
        self.b_stop.configure(state=tk.DISABLED)
        self.b_reset.configure(state=tk.NORMAL)

    def reset(self):
        self.echo_set()
        self.b_reset.configure(state=tk.DISABLED)
        self.b_inc.configure(state=tk.NORMAL)
        self.b_dec.configure(state=tk.NORMAL)
        

    def counting(self):
        if self.started:
            self.timer-=1
            self.echo.set('%02d:%02d' % (self.timer/60, self.timer%60))
            if self.timer==20:
                self.icon.configure(bg=YELLOW)
            if self.timer<=0:
                t=-1*self.timer
                self.icon.configure(bg=RED)
                self.echo.set('-%02d:%02d' % (t/60, t%60))
                self.after(500,self.yellow)

            self.after(1000,self.counting)
    
    def yellow(self):
        if self.started:
            self.icon.configure(bg=YELLOW)
            

if __name__ == "__main__":
    f=Frame()
    f.pack()
    f.mainloop()
