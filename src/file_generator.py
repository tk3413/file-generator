"""
can create a csv file based on dimensions specified.
"""

import os
from typing import Generator

import pandas


def incrementing_sequence() -> Generator[int, None, None]:
    """
    returns a Generator function that will return incrementing int
    values by invoking next on the initialized generator.
    """
    current_number: int = 1

    while True:
        yield current_number
        current_number += 1

class FileGeneratorResponse:
    def __init__(self, file_path=os.getcwd() + "/output/generated_test_file.csv"):
        self.file_path = file_path
        print(self.file_path)


class FileGenerator:
    """
    class handles all logic to generate csv files based oninitialized input
    """

    def __init__(self,
                 number_of_columns: int = 10,
                 number_of_rows: int = 10,
                 file_path: str = os.getcwd() + "/output",
                 file_name: str = "generated_test_file",
                 file_type: str = "csv"):
        self.number_of_columns = number_of_columns
        self.number_of_rows = number_of_rows
        self.file_path = self.get_validated_file_path(raw_file_path=file_path)
        self.file_name = file_name
        self.file_type = file_type

    def get_validated_file_path(self, raw_file_path: str) -> str:
        """
        ensures that the desired file path exists, and returns it as a
        string to be used
        """
        if not os.path.exists(raw_file_path):
            os.makedirs(raw_file_path)
        return raw_file_path

    def get_number_of_columns(self) -> int:
        """
        returns an int that represents the desired number of columns
        in the generated file
        """
        return self.number_of_columns

    def get_number_of_rows(self) -> int:
        """
        returns an int that represents the desired number of rows in the
        generated file
        """
        return self.number_of_rows

    def get_file_path(self) -> str:
        """
        returns the desired file path to which the generated test file
        will be written
        """
        return self.file_path

    def get_file_name(self) -> str:
        """
        returns the desired generated test file name
        """
        return self.file_name

    def get_file_type(self) -> str:
        """
        returns the desired generated file type
        """
        return self.file_type

    def create_col_name(self, col_num: int) -> str:
        return "test_col" + str(col_num)

    def generate_file(self) -> str:
        """
        generates the file and returns the full filepath to the file
        """
        data_dictionary: dict = {}
        for col in range(1, self.get_number_of_columns()):
            col_name = self.create_col_name(col_num=col)
            data_dictionary[col_name] = []
            for _row in range(0, self.get_number_of_rows()):
                data_dictionary[col_name].append("x")
        data_dataframe: pandas.DataFrame = pandas.DataFrame(data=data_dictionary)
        full_file_path: str = f"{self.get_file_path()}/{self.get_file_name()}.{self.get_file_type()}"
        data_dataframe.to_csv(full_file_path)
        return FileGeneratorResponse(file_path=full_file_path)

if __name__ == "__main__":
    FileGenerator().generate_file()
