"""
step implementation for happy paths in code

author: taimore khan
"""
import pandas
from behave import given, then, when  # pylint: disable=no-name-in-module

from src import file_generator


@given(u"only number of rows and number of columns as input")
def step_impl(context):
    context.number_of_columns = 10
    context.number_of_rows = 10


@when(u"the file generator app is called")
def step_impl(context):
    context.output_filepath = file_generator.FileGenerator(
        number_of_columns=context.number_of_columns,
        number_of_rows=context.number_of_rows,
    ).generate_file()


@then(u"a file is created in the output directory with the desired dimensions")
def step_impl(context):
    resulting_dataset: pandas.DataFrame = pandas.read_csv(context.output_filepath)
    if resulting_dataset is not None:
        assert len(resulting_dataset.index) == context.number_of_rows
    else:
        raise FileNotFoundError
