Feature: generate a csv file

  Scenario: generate a completely random csv file
     Given only number of rows and number of columns as input
      When the file generator app is called
      Then a file is created in the output directory with the desired dimensions
