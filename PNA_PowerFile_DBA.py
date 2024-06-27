import pandas as pd
import os
import csv

class DataFile:
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.data = self._load_data() if file_path else None

    def _load_data(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        
        # Find the start of the data section
        data_start = next(i for i, line in enumerate(lines) if line.strip() == 'BEGIN CH1_DATA') + 1
        
        # Read the header and the data using csv.reader to handle quoted fields
        header = next(csv.reader([lines[data_start].strip()]))
        data = list(csv.reader(lines[data_start+1:]))
        
        # Remove the last line if it is 'END'
        if data and data[-1] == ['END']:
            data.pop()

        # Debugging prints
        print(f"File: {self.file_path}")
        print("Header (length {}):".format(len(header)), header)
        print("Number of data rows:", len(data))
        if data:
            print("First data row (length {}):".format(len(data[0])), data[0])
        
        # Check if the number of columns matches
        for i, row in enumerate(data):
            if len(row) != len(header):
                print(f"Mismatch at row {i}: {row}")
                raise ValueError("Mismatch between header columns and data columns")
        
        # Create a DataFrame
        df = pd.DataFrame(data, columns=header)
        df = df.apply(pd.to_numeric, errors='ignore')  # Convert columns to numeric where possible
        return df

    def display_data(self, n=5):
        """Display the first `n` rows of the data."""
        return self.data.head(n)

    def get_column(self, column_name):
        """Get a specific column from the data."""
        if column_name in self.data.columns:
            return self.data[column_name]
        else:
            raise ValueError(f"Column {column_name} does not exist in the data.")

    def get_row(self, index):
        """Get a specific row from the data."""
        if index < len(self.data):
            return self.data.iloc[index]
        else:
		
            raise IndexError(f"Index {index} is out of range for the data.")

    @staticmethod
    def load_multiple_files(directory):
        """Load all CSV files from a specified directory."""
        data_files = []
        for filename in os.listdir(directory):
            if filename.endswith(".csv"):
                file_path = os.path.join(directory, filename)
                try:
                    data_files.append(DataFile(file_path))
                except Exception as e:
                    print(f"Error loading file {filename}: {e}")
        return data_files

# Example usage:
data_files = DataFile.load_multiple_files(r'C:/00 Sandbox/')
for data_file in data_files:
     print(data_file.display_data())
