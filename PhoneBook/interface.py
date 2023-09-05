import speeches


def greetings():
    user=input(speeches.at_start)
    return user
def show_menu():
    for i, item in enumerate(speeches.menu):
        if i==0:
            print(f"{item}")
        else:
            print(f"|\t{item}")
    

def show_all(store: list):
    for i, item in enumerate(store):
        if item:
            print(f"\n{i+1}\t{item}")

def bin(store:list):
    print("\nThere is what we got in the Bin:")
    show_all(store)

def empty(contance:str):
    print(speeches.empty(contance))

def show_bin_menu():
    for i, item in enumerate(speeches.bin_menu):
        if i>0:
            print(f"\n\t{item}")
        else:    
            print(f"\n{item}")

    pass

def assistent(user:str, contence:str):
    message=input(f"\n{speeches.assist(user, contence)}\n> ").lower()
    return message

def add(is_book:bool, timestamp:int):
    name=input(f"\n{speeches.addition[0]}\n> ")
    surname=input(f"\n{speeches.addition[1]}\n> ")
    number=""
    while not number.isdigit():    
        number=input(f"\n{speeches.addition[2]}\n> ")
    comments=input(f"\n{speeches.addition[3]}\n> ")
    if is_book:
        return(f"{name};{surname};{number};{comments}")
    else:
        return(f"{timestamp};{name};{surname};{number};{comments}")

def seek_contact(message:str):
    contact=input(f"\n{speeches.ask_contact(message)}\n> ").lower()
    return contact

def show_finded(user:str, items:list):
    print(f"\n{speeches.find_speech(user)}")
    for i,item in enumerate(items):
        if item:
           print(f"\n\t{i+1}) {item}")

def no_match(user:str, contact:str, source:str):
    print(speeches.find_fail(user,contact, source))

def choose_contact(user: str, message:str, length:int):
    number=""
    while not number.isdigit() or int(number)>length or int(number)<1:
            number=input(f"\n{speeches.choise(user, message)}\n>").lower()
    return int(number)-1


def input_error(user: str):
    print(f"\n{speeches.input_error(user)}")

def confirmation(message:str, contact:str):
    answer=""
    while not answer=="yes" and not answer=="no":
        l=len(speeches.confirm(contact, message))
        print(f"="*l)
        answer=input(f"{speeches.confirm(contact, message)}\n"+"="*l+"\n>").lower()
    return answer

def deleted(contact:str, contence:str):
    print(speeches.delete(contact,contence))

def goodbye(user:str):
    print(f"\n{speeches.bye(user)}")

def clear(user:str):
    answer=""
    while not answer=="yes" and not answer=="no":
        answer=input(f"\n{speeches.clear(user)}\n> ")
    return(answer)