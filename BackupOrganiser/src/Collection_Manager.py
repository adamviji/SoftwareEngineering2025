from main import main
import Data_Collection

class CollectionManager:

    def __init__(self):
        self.collections = []

    def add_collection(self, name, description, creation_date, modification_date, updated):
        new_collection = Data_Collection()
        new_collection.name = name
        new_collection.description = description
        new_collection.creation_date = creation_date
        new_collection.modification_date = modification_date
        new_collection.updated = updated
        self.collections.append(new_collection)
        # self.name = name
        # self.description = description
        # self.creation_date = creation_date
        # self.modification_date = modification_date
        # self.updated = update


    def overview(self):
        out = []
        for i in self.collections:
            out.append(i.brief_str)
        return out


    def detailed_overview(self):
        out = []
        for i in self.collections:
            out.append(i.full_str)
        return out


    def info(collection_name):
        Data_Collection.full_str()
        pass

    def get(collection_name):
        pass

if __name__ == "__main__":
main()
