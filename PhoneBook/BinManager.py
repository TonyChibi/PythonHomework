from BookManager import BookManager
class BinManager(BookManager):
    def __init__(self, book_path: str = "BooksBin.txt"):
          super().__init__(book_path)

    store=[]
    name="bin"

    def is_inspire(self, created:float, current: float):
        insp_date=86400*30 # 30 days in seconds
        # print(current)
        # print(created)
        # print(current-created)
        # print(insp_date)
        if current-created>=insp_date:
            return True
        else:
             return False
        
    def refresh(self,current_time:int):
        if self.store:
            print(f"{self.store}")
            for i, item in enumerate(self.store):
                    if item:
                        contact=item.split(";")
                        created=float(contact[0])
                        print(created)
                        if self.is_inspire(created,current_time):
                            self.delete_contact(self.store,i)
            return True
        else:
             return False
        
    def clear(self):
        with open(self.path, "w", encoding="utf-8") as file:
             file.write("")