class BackupManager:
    def __init__(self, collection_manager):
        self.collection_manager = collection_manager

    def add_backup(self, collection_object, backup_name, backup_date, backup_location):
        self.collection_object = collection_object
        self.backup_name = backup_name
        self.backup_date = backup_date
        self.backup_location = backup_location
        if collection_object is None:
            print("Error: Collection object is None")
            return False
        backup_entry = {
            "name": backup_name,
            "date": backup_date,
            "location": backup_location,
        }
        collection_object.backup_entries.append(backup_entry)
        return True

    def remove_backup(self, collection_name, backup_name, backup_date):
        """Ta bort en backup från en collection"""
        collection_object = self.collection_manager.get(collection_name)
        if collection_object is None:
            return False
        """Hitta och ta bort backupen"""
        for i, backup in enumerate(collection_object.backup_entries):
            if backup["name"] == backup_name and backup["date"] == backup_date:
                collection_object.backup_entries.pop(i)
                return True
        return False