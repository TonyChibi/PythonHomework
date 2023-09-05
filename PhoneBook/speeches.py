at_start="\n Howdy! What's your name again?\n>"

menu=["Here is a list of your possibilities:",
      "all - print all of your contacts",
      "add - add new contact to your book",
      "find - seek a contact",
      "change - rewrite a contact",
      "delete - delete a contact",
      "bin - print all existed contacts in bin",
      "quit - to finish it",
      "help - to get help notes"]
bin_menu=["There in Bin you can do next things:", 
          "all - show all existed in bin contacts",
          "delete - delete a contact",
          "restore - restore contact from the bin",
          "clear - clear the bin",
          "help - to get help notes",
          "quit - to get back to PhoneBook"]
addition=["Please insert the name of a contact:",
          "Insert the surname:",
          "Number, please:",
          "Add some coments:"]

def ask_contact(message:str):
    return f"Which contact do you want to {message}?"

def bye(user:str):
    return(f"Farewell, {user}. See ya!")

def assist(user: str, contence:str):
    return(f"How can your humble {contence} assistent helps you, {user}?\nType 'help' for guidence")

def input_error(user: str):
    return(f"Sorry, {user}, I'm too stupid for that. Look at the guidence ")

def find_speech(user: str):
    return(f"My dear {user}, look what I've found: ")

def find_fail(user: str, contact: str, source: str):
    return f"Sorry, {user}, I can't find {contact} in a {source}"

def choise(user:str, message: str):
    return f"Please, {user}, choose the number of contact that you want to {message}"

def confirm(contact:str, message: str):
    return f"Are you sure you wanna {message} ''{contact}''?"

def empty(contance:str):
    return f"The {contance} is empty"

def delete(contact:str, contence:str):
    return f"Contact {contact} has been deleted from {contence}"
def clear(user:str):
    return f"Dear, {user}, are you definite?\nIt'll delete all contenence in bin"
