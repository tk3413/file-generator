from unittest import TestCase, mock

from src.file_generator import FileGenerator, incrementing_sequence


class TestStaticMethods(TestCase):
    def test_increment(self):
        sequence: Generator = incrementing_sequence()
        self.assertTrue(next(sequence) == 1)
        self.assertTrue(next(sequence) == 2)


class TestFileGenerator(TestCase):
    def test_init(self):
        test_file_gen_client = FileGenerator(number_of_rows=10, number_of_columns=100)
        self.assertTrue(test_file_gen_client.get_number_of_rows() == 10)
        self.assertTrue(test_file_gen_client.get_number_of_columns() == 100)
        test_file_gen_client_defaults = FileGenerator()
        self.assertTrue(test_file_gen_client_defaults.get_number_of_rows() == 1)
        self.assertTrue(test_file_gen_client_defaults.get_number_of_columns() == 1)

    @mock.patch("src.file_generator.FileGenerator.get_number_of_columns")
    @mock.patch("pandas.DataFrame")
    @mock.patch("os.getcwd")
    @mock.patch("src.file_generator.incrementing_sequence", return_value=iter([1]))
    def test_generate_file(self, mock_get_cols, mock_dataframe, mock_cwd, mock_gen):
        FileGenerator().generate_file()
        mock_get_cols.assert_called()
        mock_dataframe.assert_called()
        mock_cwd.assert_called()
        mock_gen.assert_called()
