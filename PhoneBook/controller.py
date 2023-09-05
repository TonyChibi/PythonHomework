import interface
import time
import main
from BookManager import BookManager
from BinManager import BinManager


def start(state:bool):
    book=BookManager()
    bin=BinManager()
    is_book=True
    obj=book
    user=interface.greetings()
    interface.show_menu()
    print(time.time())
    while state:
        now=time.time()
        message=interface.assistent(user, obj.name)
        obj.store_file()
        match message:

            case "all":
                if obj.store:
                    interface.show_all(obj.store)
                else:
                    interface.empty(obj.name)

            case "add":
                if is_book:
                    contact=interface.add(is_book,time.time())
                    obj.add_contact(contact)

            case "find":
                cont=interface.seek_contact(message)
                items=obj.find_contact(cont)
                if items:
                    interface.show_finded(user,items)
                else:
                    interface.no_match(user, cont, obj.name)

            case "change":
                if is_book:
                    contact=interface.seek_contact(message)
                    items=obj.find_contact(contact)
                    if items:
                        interface.show_finded(user,items)
                        number=0
                        if len(items)>1:
                            number=interface.choose_contact(user,message,len(items))
                        answer=interface.confirmation(message, items[number])
                        if answer=="yes":
                            bin.add_contact(f"{time.time()};{items[number]}")
                            interface.deleted(obj.delete_contact(items, number),obj.name)
                            contact=interface.add(is_book,time.time())
                            obj.add_contact(contact)   
                    else:
                        interface.no_match(user, contact, obj.name)
            
            case "delete":
                contact=interface.seek_contact(message)
                items=obj.find_contact(contact)
                if items:
                    interface.show_finded(user,items)
                    number=0
                    if len(items)>1:
                        number=interface.choose_contact(user,message,len(items))
                    answer=interface.confirmation(message, items[number])
                    if answer=="yes":
                        if is_book:
                            dumb=obj.delete_contact(items, number)
                            bin.add_contact(f"{time.time()};{dumb}")
                        else:
                            obj.delete_contact(items, number)
                else:
                    interface.no_match(user, contact, obj.name)
            
            case "bin":
                bin.store_file()
                if bin.refresh(now):
                    is_book=False
                    obj=bin
                    interface.bin(obj.store)
                else: 
                    interface.empty(bin.name)
                 # print everything in bin, shows a bin menu, switch is_book to False and obj to bin
            
            case "restore":
                if not is_book:
                    contact=interface.seek_contact(message)
                    items=obj.find_contact(contact)
                    if items:
                        interface.show_finded(user,items)
                        number=0
                        if len(items)>1:
                            number=interface.choose_contact(user,message,len(items))
                        answer=interface.confirmation(message, items[number])
                        if answer=="yes":
                            restored=items[number].split(";")
                            restored.reverse()
                            restored.pop()
                            restored.reverse()
                            restored_str=";".join(restored)
                            book.add_contact(restored_str)
                            bin.delete_contact(items, number)


            case "clear":
                if not is_book:
                    answer=interface.clear(user)
                    if answer=="yes":
                        bin.clear()
                        interface.empty(bin.name)

            case "quit":
                if is_book:
                    interface.goodbye(user)
                    state=False
                else:
                    is_book=True
                    obj=book

            case "help":
                if is_book:
                    interface.show_menu()
                else:
                    interface.show_bin_menu()
            
            case _:
                interface.input_error(user)
    


