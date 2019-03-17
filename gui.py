from tkinter import *

form = Tk()
form.title('Gym')
form.geometry('210x250')
form.resizable(False,False)
lb1 = Label(form,text='what is your name:')
name = Entry(form)
lb2 = Label(form,text='how old are you:')
age = Entry(form)
lb3 = Label(form,text='How tall you are in meters:')
tall = Entry(form)
lb4 = Label(form,text='what is your weight in kg :')
weight = Entry(form)
v = StringVar()
result = Label(form,textvariable=v)

def test():
    name_ = name.get()
    weight_ = weight.get()
    tall_ = tall .get()
    calo = float(weight_) * 2 * 12
    water = int(float(weight_) * 0.033)
    brotin = int(float(weight_) * 2 )
    perfect_weight = int((float(tall_) - 1) * 100)
    v.set('Mr '+name_ + ' your perfect weight is '+str(perfect_weight)+' kg'+'\n'+'and you are need '+str(water) +' l from water /day'+'\n'+' and you need '+str(calo)+' kcal/day '+'\n'+' and  '+str(brotin)+' g/day ')
    
    
btn = Button(form ,text= 'ok',command=test)

lb1.pack()
name.pack()
lb2.pack()
age.pack()
lb3.pack()
tall.pack()
lb4.pack()
weight.pack()
btn.pack()
result.pack()
form.mainloop()