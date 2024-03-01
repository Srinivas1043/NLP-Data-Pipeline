class DataReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data_from_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
