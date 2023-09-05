def Book_manager(path):
    state=True
    file=open(path, 'r', encoding="UTF-8")
    store=file.read().split('\n')
    file.close()
    def greeting():
        user=input("Howdy! Wat's your name again?\n>")
        print(f"Long time no see, {user}\n Here is a list of your possibilities:")
        note()
        interface(state, user)
        
        
    def interface(state, user):
        while state:
            file=open(path, 'r', encoding="UTF-8")
            store=file.read().split('\n')
            file.close()
            message=input(f"\nhow can i help you, {user}?\ntype 'help' for guidence\n>").lower()
            if message=='all':
                seek_messege(store)
            elif message=='add':
                new()
            elif message=="delete":
                str=input("\nWhich contact do you wanna delete?\n>").lower()
                result=seek(str, store)
                if result:
                    seek_messege(result)
                    delete(result, store, message)
                else:
                    print("there in no such contact")
            elif message=='find':
                str=input("\nwhich contact do you want to find?\n>").lower()
                result=seek(str, store)
                if result:
                    seek_messege(result)
                else:
                    print(f"sorry, cannot find {str}")
                        
            elif message=='change':
                str=input("\nwhich contact do you wanna change?\n").lower()
                change(str,store,message)
            elif message=="help":
                note()
            elif message=="quit":
                state=False
                print(f"\ngood bye, {user}")
            else:
                print(f"sorry,{user}, I'm too stupid for that.\n See the guidence:")
                note()

    def note():
        print("\n+    all - print all your contacts")
        print("+    add - add new contact to your book")
        print("+    delete - delete the contact")
        print("+    change - rewrite the contact")
        print("+    find - seek the contact")
        print("+    quit - to finish it")
        print("+    help - to get help notes")



    def seek(str, store):
        result=[item for item in store if str in item]
        return result

    def seek_messege(result):
        print("\nHere is what I've found:")
        for i in range (0,len(result)):
            print(len(result))
            print(f'{i+1}: {result[i].replace(";", "  ")}')
        

    def new():
        file=open(path, 'a', encoding='utf-8' )
        name=input("insert Name: ").lower()
        surname=input("insert Surname: ").lower()
        number=input("insert number: ").lower()
        comments=input("insert comments: ").lower()
        file.write(f"{name};{surname};{number};{comments}\n")
    

    def delete(items,store,message):
        position=0
        if len(items)>1:
            position=-1+int(input(f"\nthe contact under which number you want to {message}?\n>"))
        ask=input(f"is it [{items[position].replace(';',' ')}] you wanna {message}? \n answer 'yes' or 'no'\n ")
        if ask=='yes':
            store.remove(items[position])
            file=open(path, "w", encoding="utf-8")
            for i in store:
                if i:
                    file.write(f"{i}\n")

            

    
    def change(str,store,message):
        result=seek(str,store)
        if result:
            seek_messege(result)
            delete(result,store,message)
            new()
        else:
            print("there in no such contact")


    
    greeting()
Book_manager('C:/Users/GlazH/OneDrive/Рабочий стол/PythonGeek/PyHomework/Hm_08/phone_book.txt')