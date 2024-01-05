from nlp_pipeline.embeddings import DataReader
def main():
    file_path = '../data/textfiletesting.txt' 
    # Create an instance of the DataReader class
    data_reader = DataReader(file_path)

    # Use the class method to read data from the file
    data = data_reader.read_data_from_file()
    
    print("Content of the file:")
    print(data)

if __name__ == "__main__":
    main()
