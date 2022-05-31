import os

from unittest import TestCase, mock

from src.file_generator import FileGenerator, FileGeneratorResponse, incrementing_sequence


def remove_unittest_folder():
    try:
        os.rmdir(os.getcwd() + "/unittest_output")
    except FileNotFoundError as fnfe:
        pass

class TestStaticMethods(TestCase):
    def test_increment(self):
        sequence: Generator = incrementing_sequence()
        self.assertTrue(next(sequence) == 1)
        self.assertTrue(next(sequence) == 2)

class TestFileGeneratorResponse(TestCase):
    def test_response(self):
        self.assertTrue(FileGeneratorResponse().file_path.split("/")[-1] == "generated_test_file.csv")


class TestFileGenerator(TestCase):
    def test_init(self):
        test_file_gen_client = FileGenerator(number_of_rows=10, number_of_columns=100)
        self.assertTrue(test_file_gen_client.get_number_of_rows() == 10)
        self.assertTrue(test_file_gen_client.get_number_of_columns() == 100)
        test_file_gen_client_defaults = FileGenerator()
        self.assertTrue(test_file_gen_client_defaults.get_number_of_rows() == 10)
        self.assertTrue(test_file_gen_client_defaults.get_number_of_columns()
                        == 10)
        self.assertTrue(test_file_gen_client_defaults.get_file_path()
                        == os.getcwd() + "/output")
        self.assertTrue(test_file_gen_client_defaults.get_file_name()
                        == "generated_test_file")
        self.assertTrue(test_file_gen_client_defaults.get_file_type()
                        == "csv")

    @mock.patch("src.file_generator.FileGenerator.get_number_of_columns")
    @mock.patch("pandas.DataFrame")
    def test_generate_file(self, mock_get_cols, mock_dataframe):
        FileGenerator().generate_file()
        mock_get_cols.assert_called()
        mock_dataframe.assert_called()

    def test_create_col(self):
        col: str = FileGenerator().create_col_name(col_num=1)
        assert col == "test_col1"

    @mock.patch("os.path.exists", return_value=False)
    @mock.patch("os.makedirs")
    def test_validated_file_path(self, mock_path_exists,
                                 mock_makedirs):
        remove_unittest_folder()
        FileGenerator().get_validated_file_path(raw_file_path=os.getcwd()+"/unittest_output")
        mock_path_exists.assert_called()
        mock_makedirs.assert_called()
        remove_unittest_folder()
