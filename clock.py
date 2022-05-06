from tkinter import *
global count
count =0
a=0
b=0

class stopwatch():
    def stop(self):
        global count,a,b
        self.d = str(self.t.get())
        a=self.d
        a,b = b,a
        
        print(b,a)
        count=1
        self.t.set('00')  


    def start(self):
        global count
        count=0
        self.timer() 

    def pause(self):
       global count,a
       self.d = str(self.t.get())
       s= int(self.d )
       if 1<=s<5:
           a+=10
       elif 5<=s<9:
            a+=15
       else:
           a+=20
       count=1


    def submit(self):
        result=a+b
        print(result)
    


    def timer(self):    
        global count
        if(count==0):
            self.d = str(self.t.get())
            s = int(self.d )
           
            if(s<12):
                s+=1
            else:
                s=0
           
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=s           
            self.t.set(self.d)
            if(count==0):
                self.root.after(1000,self.timer) 



    def __init__(self):
        self.root=Tk()
        self.root.title("Clock")
        self.root.geometry("600x200")
        self.t = StringVar()
        self.t.set("00")
        self.t1=Entry()
        self.lb = Label(self.root,textvariable=self.t,font=("Times 40 bold"),bg="white")
        self.bt1 = Button(self.root,text="Start",command=self.start,font=("Times 12 bold"),bg=("green"))
        self.bt2 = Button(self.root,text="Pause",command=self.pause,font=("Times 12 bold"),bg=("red"))
        self.bt3 = Button(self.root,text="Stop",command=self.stop,font=("Times 12 bold"),bg=("orange"))
        self.bt4 = Button(self.root, text="Submit", command=self.submit,font=("Times 12 bold"),bg=("yellow"))
        self.lb.place(x=160,y=10)
        self.bt1.place(x=120,y=100)
        self.bt2.place(x=220,y=100)
        self.bt3.place(x=320,y=100)
        self.bt4.place(x=420,y=100)
        self.label = Label(self.root,text="",font=("Times 40 bold"))
        
        self.root.configure(bg='black')
        self.root.mainloop()
a=stopwatch()      