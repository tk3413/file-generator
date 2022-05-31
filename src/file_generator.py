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


class FileGenerator:
    """
    class handles all logic to generate csv files based oninitialized input
    """

    def __init__(self, number_of_columns: int = 10, number_of_rows: int = 10):
        self.number_of_columns = number_of_columns
        self.number_of_rows = number_of_rows

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

    def create_col_name(self, col_num: int) -> str:
        return "test_col" + str(col_num)

    def generate_file(self) -> str:
        """
        generates the file and returns the full filepath to the file
        """
        data_dictionary: dict = {}
        col_sequence: Generator = incrementing_sequence()
        for col in range(1, self.get_number_of_columns()):
            col_name = self.create_col_name(col_num=col)
            data_dictionary[col_name] = []
            for _row in range(0, self.get_number_of_rows()):
                data_dictionary[col_name].append("x")
        data_dataframe: pandas.DataFrame = pandas.DataFrame(data=data_dictionary)
        file_name: str = "out.csv"
        data_dataframe.to_csv(file_name)
        return os.getcwd() + "/" + file_name

if __name__ == "__main__":
    FileGenerator().generate_file()
