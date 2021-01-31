# Banklikex
## Architecture
Any diagrams associated with the program  
- Drawio diagram can be loaded with vs code plugin or at [draw.io](https://app.diagrams.net/)

## Entities
Holds data models used to store original and manipulated data
- data_models.call_data_field_dict contains all fields that will be used to compare banks in the dataset and can be modified to included different fields

## Example_Data
Contains a small dataset that can be used to run the program without dowloading from [Dataset](#Dataset)

## Repo
Responsible for importing data from external sources

## Requirements
Contains pip requirements files for setting up python environment to run banklikex

## Tests
Includes unittest test cases for various functions in the banklikex application
- Because this is not a production application, tests were only written as an example and are not included for every function

## Usecase
Holds the logic fulfilling the business requirements of the application
- analysis: logic associated with analyzing the dataset
- input_validation: validates any inputs being passed to interface in the usecase layer
- interface: entry point functions from user interface to the usecase layer

## Banklikex
Entry point for the command line interface to the application
- Run the following to see a list of available commands
```
python banklikex.py -h
```

## Resources
### Dataset
[Bulk: Call Reports -- Balance Sheet, Income Statement, Past Due -- Four Periods](https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx)
### Distributions
[Empirical Cumulative Distribution Function](https://machinelearningmastery.com/empirical-distribution-function-in-python/)  
[CDF for Value Percentile](https://www.andata.at/en/software-blog-reader/why-we-love-the-cdf-and-do-not-like-histograms-that-much.html)