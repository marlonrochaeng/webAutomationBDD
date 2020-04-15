# Web Automation with Python and Selenium using Behave

This project will generate a document with screenshots.

## Prerequisites

To run this project, you need:

```
Python 3+ and its libraries:
selenium
werkzeug
python-docx
behave
```
## To do
1. Clone project
2. Install libs with pip install requirements.txt 
3. Verify if the drivers are compatible with your browsers
4. Add geckodriver to path to run tests with firefox
5. Allow safari to run with remote automation to run tests with safari

## Running a test case

In working directory, to run all the test cases, execute the command:
```
behave -D browser=chrome
```

In working directory, to run just on test, execute the command:
```
behave -D browser=chrome features/feature_name.feature

you can confiture to run with firefox or safari changing the browser name
```