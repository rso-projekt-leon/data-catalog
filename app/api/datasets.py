
items = {
    0: {"name": "First item"}
}


items = {
    0: {"name": "First item"}
}

class DatasetsMetadataResource:
    def read_all(self):
        print()
        return items
    def create(self):
        return items
    def read_one(self, dataset_id):
        print(dataset_id)
        return items
    def update(self, dataset_id):
        return items
    def delete(self, dataset_id):
        # naredi klic na service, ki zbriše dataset iz baze
        return items


datasets = DatasetsMetadataResource()