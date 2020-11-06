from tkinter import *
from covid import Covid
from tkinter import ttk
from tkinter import messagebox
# {'id': '82', 'country': 'Iran', 'confirmed': 663800, 'active': 116439, 'deaths': 37409, 'recovered': 509952, 'latitude': 32.427908, 'longitude': 53.688046, 'last_update': 1604687076000}
# iran_cases = covid.get_status_by_country_name("iran")


root = Tk()
root.title('Covid App')
root.geometry('700x250')
root.config(bg='#333456')
style = ttk.Style(root)
style.configure('Treeview', rowheight=5) 
def search():
    global confirmed, active, deaths, recovered, country
    country = country_entry.get()
    covid = Covid()
    covid.get_data()
    try:
        country_cases = covid.get_status_by_country_name(country)
        confirmed = country_cases['confirmed']
        active = country_cases['active']
        deaths = country_cases['deaths']
        recovered = country_cases['recovered']
        
        showResult()
    except ValueError:
        noResult()
    
    
    

def noResult():
    my_tree.destroy()
    messagebox.showerror('Error', 'No Country Found Named {}'.format(country))

def showResult():
    global my_tree
    
    my_tree = ttk.Treeview(root)
    my_tree['columns'] = ( "Confirmed Cases", "Active Cases", "Deaths", "Recoverd")
    
    my_tree.column("#0", width=120)
    
    my_tree.column("Confirmed Cases", anchor=W, width=120)
    my_tree.column("Active Cases", anchor=W, width=120)
    my_tree.column("Deaths", anchor=W, width=120)
    my_tree.column("Recoverd", anchor=W, width=120)
    
    my_tree.heading("#0", text="Country", anchor=W)
    
    my_tree.heading("Confirmed Cases", text="Confirmed Cases", anchor=W)
    my_tree.heading("Active Cases", text="Active Cases", anchor=W)
    my_tree.heading("Deaths", text="Deaths", anchor=W)
    my_tree.heading("Recoverd", text="Recoverd", anchor=W)
        
    my_tree.insert(parent='', index='end', iid=0, text=country.lower(), values=(confirmed, active, deaths, recovered))
    my_tree.place(relx=0.5, rely=0.65, anchor='c')


country_entry = Entry(root, bg='#595b83', fg='white', borderwidth=5, width=40)
country_entry.place(relx=0.5, rely=0.2, anchor='c')

search_btn = Button(root, text='Search Country', bg='#060930', fg='white', borderwidth=3, padx=30, command=search)
search_btn.place(relx=0.5, rely=0.4, anchor='c')


root.mainloop()