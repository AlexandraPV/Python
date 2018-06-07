from people import *
from tkinter import *
from replecation import main_db

root = Tk()
root.title("Coursework")
root.geometry("400x300+300+250")

result_data = Button(text="Записати дані у БД", command=read_data)
result_data.grid(row=0, column=1, padx=5, pady=5, sticky="e")

gen_data = Button(text="Згенерувати дані", command=generate_data)
gen_data.grid(row=2, column=1, padx=5, pady=5, sticky="e")

plot = Button(text="Графік 1", command=most_popular_language)
plot.grid(row=3, column=1, padx=5, pady=5, sticky="e")

plot1 = Button(text="Графік 2", command=people)
plot1.grid(row=4, column=1, padx=5, pady=5, sticky="e")

plot2 = Button(text="Реплекація", command=main_db)
plot2.grid(row=5, column=1, padx=5, pady=5, sticky="e")

if __name__ == '__main__':
    root.mainloop()