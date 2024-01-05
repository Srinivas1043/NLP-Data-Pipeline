from nlp_pipeline.embeddings import DataReader
def test_main():
    file_path = 'data/textfiletesting.txt' 
    # Create an instance of the DataReader class
    data_reader = DataReader(file_path)

    # Use the class method to read data from the file
    data = data_reader.read_data_from_file()
    print(data)
    assert data == 'This is a sample text file.\nIt contains multiple lines of text.\nFeel free to add more content for testing.\n'

