from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("MA'LUMOT KIRITISH")
window.geometry("500x400")
window.resizable(False, False)
window.configure(bg = "light blue")
malumot = Label(window, text = "MALUMOT TOPLOVCHI DASTUR", font = "Arial 20", bg = "light blue")
malumot.pack()

soz = Label(window, text = "Ismni va Familiyani kiriting", font = "Arial 14", bg = "light blue")
soz.pack()
ism = Entry(window, font = "Arial 14", bg = "white", width= 30)
ism.pack()
yil = Label(window, text = "Tug'ilgan kuningizni kiriting (2005.15.02)", font = "Arial 14", bg = "light blue")
yil.pack()
yil = Entry(window, font = "Arial 14", bg = "white", width= 20)
yil.pack()
def tugilgan_yil():
    ismlar_va_yillar = {}
    ismi = ism.get()
    yili = yil.get()
    ismlar_va_yillar[ismi] = yili
    with open("ism_yil.txt", "a") as file:
        file.write(str(ismlar_va_yillar) + "\n")
    messagebox.showinfo("Ma'lumot", "Ma'lumot saqlandi")
    ism.delete(0, END)
    yil.delete(0, END)
    ism.focus()
    yil.focus()
    print(ismlar_va_yillar)
saqlash = Button(window, text = "Saqlash", font = "Arial 14", bg = "light green", command = tugilgan_yil)
saqlash.pack()
def chiqarish():
    window.destroy()
    import ma
    ma.window.mainloop()
chiqarish = Button(window, text = "Chiqish", font = "Arial 14", bg = "red", command = chiqarish)
chiqarish.pack()
yaratuvchi = Label(window, text = "Yaratuvchi: @BEKFURR", font = "Arial 14", bg = "light blue")
yaratuvchi.pack()


window.mainloop()


