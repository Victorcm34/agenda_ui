import pickle
from tkinter import *
from tkinter import ttk



#Declaro el nombre del archivo donde se guardará nuestra agenda
SAVE_FILE_NAME = "contacts.save"

#Funcion que recibe una lista e inserta en ella 3 datos
def add_contact(contacts, name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    return contact

#Funcion que recibe un contacto de add_contact y lo muestra en un FRAME
def add_contact_tklist(contacts, name, phone, email, fr_contact_list):
    try:
        contact = add_contact(contacts, name, phone, email)

        col, row = fr_contact_list.grid_size()

        ttk.Label(fr_contact_list, text=contact["name"]).grid(column=1, row=row)
        ttk.Label(fr_contact_list, text=contact["email"]).grid(column=2, row=row)
        ttk.Label(fr_contact_list, text=contact["phone"]).grid(column=3, row=row)
    except:
        pass

#Funcion que carga los datos guardados en la lista y los coloca en el frame
def load_contact_tklist(contacts, fr_contact_list):

    for contact in contacts:

        col, row = fr_contact_list.grid_size()

        ttk.Label(fr_contact_list, text=contact["name"]).grid(column=1, row=row)
        ttk.Label(fr_contact_list, text=contact["email"]).grid(column=2, row=row)
        ttk.Label(fr_contact_list, text=contact["phone"]).grid(column=3, row=row)

#Funcion por hacer
def export_contacts():
    pass


#Funcion que le un archivo binario y carga su contenido
def load_contacts():

    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))

    except FileNotFoundError:
        return []

#Funcion que vuelca el contenido de la lista contacts en un archivo binario
def save_contacts(contacts):

    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)

    print("Datos guardados correctamente.")



def main():

    #Inicio la lista con los varoles del archivo binario guardado
    contacts = load_contacts()


    # Declaro el primer FRAME, en este caso se trata del frame que servirá de input de la agenda
    root = Tk()
    fr_add_contact = ttk.Frame(root, padding="30 12 30 12")
    fr_add_contact.grid()

    #Variables que será asignadas en cada ENTRY para ser guardadas como lista
    name_entry = StringVar()
    email_entry = StringVar()
    phone_entry = StringVar()

    #Etiquetas y posicionamiento dentro del grid del frame
    ttk.Label(fr_add_contact, text="Nombre").grid(column=1, row=1, sticky=W, padx=(5,5))
    ttk.Label(fr_add_contact, text="Email").grid(column=2, row=1, sticky=W, padx=(5,5))
    ttk.Label(fr_add_contact, text="Telefono").grid(column=3, row=1, sticky=W, padx=(5,5))

    #Entrys y asignación a cada una de las variables que representan
    ttk.Entry(fr_add_contact, width=20, textvariable=name_entry).grid(column=1, row=2, padx=(5,5))
    ttk.Entry(fr_add_contact, width=40, textvariable=email_entry).grid(column=2, row=2, padx=(5,5))
    ttk.Entry(fr_add_contact, width=20, textvariable=phone_entry).grid(column=3, row=2, padx=(5,5))


    #Declaro botón para añadir usuarios a la lista y su comando llamando a la funcion add_contact
    ttk.Button(fr_add_contact, text="Añadir",
               command=lambda:
               add_contact_tklist(contacts, name_entry.get(), phone_entry.get(), email_entry.get(),  fr_contact_list)
               ).grid(column=3, row=3, pady=(7,0))

    #Declaro el segundo FRAME, este se encargará de listar todos los contactos almacenados en ella
    fr_contact_list = ttk.Frame(root, padding="30 12 30 12")
    fr_contact_list.grid()

    # Etiquetas y posicionamiento dentro del grid del SEGUNDO frame
    ttk.Label(fr_contact_list, text="Nombre").grid(column=1, row=1, sticky=W, padx=(60,60), pady=(0,10))
    ttk.Label(fr_contact_list, text="Email").grid(column=2, row=1, sticky=W, padx=(60,60), pady=(0,10))
    ttk.Label(fr_contact_list, text="Telefono").grid(column=3, row=1, sticky=W, padx=(60,60), pady=(0,10))

    #Llamamos a la funcion para mostrar el contenido de la lista contacts en el segundo FRAME
    load_contact_tklist(contacts, fr_contact_list)

    #Ejecutamos la ventana
    root.mainloop()

    #Llamamos a laa funcion para guardar el contenido de la lista en el archivo binario
    save_contacts(contacts)
    print("¡Adiós!")


if __name__ == "__main__":
    main()