
class BookManager:
    def __init__(self, book_path: str="book.txt", store: str=""):
        self.path=book_path
        self.store=store
    store=[]
    name="book"

    def store_file(self):
        file=open(self.path, "r", encoding="utf-8")
        self.store=file.read().split("\n")
        file.close()
        return self.store
    
    def find_contact(self, contact: str):
        items=[item for item in self.store if contact in item]
        return items
    
    def delete_contact(self,items:list, position: int=0):
        self.store.remove(items[position])
        with open(self.path, "w", encoding="utf-8") as file:
            for i in self.store:
                if i:
                    file.write(f"{i}\n")
        return items[position]

    def add_contact(self, contact: str):
        with open(self.path, "a", encoding="utf-8") as file:
            file.write(f"{contact}\n")
    
    
        

