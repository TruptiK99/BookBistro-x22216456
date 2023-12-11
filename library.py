class CustomLib:
    def __init__(self, model):
        self.model = model.objects
    
    def get_id_specific_data(self, id):
        data = self.model.get(id=id)
        return data
    