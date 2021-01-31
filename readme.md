# Banklikex
Goal: Determine which banks are like others in FFIEC government [Dataset](#Dataset)

## Architecture
Any diagrams associated with the program  
- Drawio diagram can be loaded with vs code plugin or at [draw.io](https://app.diagrams.net/)

## Docs
Any documentation associated with banklikex
- Assignment_Questions: Details of the assignment and answers to questions included with the bank like x assignment

## Entities
Holds data models used to store original and manipulated data
- data_models.call_data_field_dict contains all fields that will be used to compare banks in the dataset and can be modified to included different fields

## Example_Data
Contains a small dataset that can be used to run the program without downloading from [Dataset](#Dataset)
- Currently only the 2020 dataset is included, but the program can take datasets from multiple years at the same time if all files are included in the input directory

## Images
Images used in docs and application

## Repo
Responsible for importing data from external sources

## Requirements
Contains pip requirements files for setting up python environment to run banklikex
- requirements-prod should be used when setting up an environment to just run the app
- requirements-dev includes additional libraries such as those to build auto html documentation

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
- Note that for the idrssd input, an idrssd from the referenced data will need to be used, see [Example Data](#Example_Data)

## Resources
### Dataset
[Bulk: Call Reports -- Balance Sheet, Income Statement, Past Due -- Four Periods](https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx)
### Distributions
[Empirical Cumulative Distribution Function](https://machinelearningmastery.com/empirical-distribution-function-in-python/)  
[CDF for Value Percentile](https://www.andata.at/en/software-blog-reader/why-we-love-the-cdf-and-do-not-like-histograms-that-much.html)