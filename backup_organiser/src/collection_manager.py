from data_collection import DataCollection

class CollectionManager:

    """Hanterar alla DataCollection objekt den är bossen av list-hanteringen
    Managern hanterar endast listorna den har inga egna collections i en lista. returnerar o olika former med hjälp av de olika funktionerna"""
    def __init__(self):
        self.collections = []

    def add_collection(self, name, description, creation_date, last_modified_date, still_updated):
        """Skapar ett DataCollection objekt och lägger till det i listan"""
        new_collection = DataCollection(
            name,
            description,
            creation_date,
            last_modified_date,
            still_updated
        )
        self.collections.append(new_collection)

    def overview(self):
        """Returnerar översikt som JSON-objekt"""
        out = []
        for collection in self.collections:
            out.append(
                {
                    "name": collection.name,
                    "backups": collection.backup_entries,  # Använd backup_entries
                }
            )
        return out

    def detailed_overview(self):
        """Returnerar en array, en lista per DataCollection"""
        out = []
        for collection in self.collections:
            out.append(collection.to_dict())
        return out


    def info(self, collection_name):
        """Returnerar en lista med strängar för EN specifik DataCollection"""
        for collection in self.collections:
            """Kollar om namnet på nuvarande collection matchar namn som söks"""
            if collection.name == collection_name:
                """körs när if är true"""
                return collection.to_dict() 
        """Om ingen match hittas körs denna och endsat då"""
        return [f"Collection {collection_name} not found"]
        pass

    def get(self, collection_name):
        """Returnerar ett DataCollection objekt"""
        for collection in self.collections:
            """Kollar om namnet på nuvarande collection matchar namn som söks"""
            if collection.name == collection_name:
                return collection
        return None

    def edit(self, collection_name, last_modified_date=None, still_updated=None):
        """Redigera en collection"""
        for collection in self.collections:
            if collection.name == collection_name:
                """ Uppdatera last_modified_date om den finns """
                if last_modified_date is not None:
                    collection.last_modified_date = last_modified_date
                """Uppdatera still_updated om den finns"""
                if still_updated is not None:
                    """ Konvertera string "true"/"false" till boolean"""
                    if isinstance(still_updated, str):
                        collection.still_updated = still_updated.lower() == "true"
                    else:
                        collection.still_updated = bool(still_updated)
                return True
        return False

    def delete(self, collection_name):
        """Tar bort den första data collection som matchar collection_name.
        Returnerar TRUE om en collection hittas och tas bort, annars FALSE"""
        old_len = len(self.collections)
        self.collections = [x for x in self.collections if x.name != collection_name]
        new_len = len(self.collections)
        return new_len == old_len - 1

    def search(self, search_term):
        """Söker collections och returnerar som JSON"""
        result = []
        search_lower = search_term.lower()
        for collection in self.collections:
            if search_lower in collection.name.lower():
                result.append({
                    "name": collection.name, 
                    "backups": collection.backup_entries})
        return result
