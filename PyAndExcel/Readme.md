# Automatic Excel checker

I wrote this program to automatically output a file containing fake entries and duplicate data from an Excel sheet
## Why I wrote the code

I created a voting poll using Google forms for our end of year Faculty party.
>We are about 300+ students and going through the Excel file was boring but I needed to check the Excel sheet since everyone could *fake a vote* easily even after collecting emails and adding only one respond per person.
>I wrote this code to check automatically check the following:
1. Valid registration number
2. Valid Names
3. Duplicates
###### I had the class list with all the registration numbers and names for referencing
## What the Code Does
1. It creates two list one from the Students.xlsx ( class list ) and the other from the names and registration number fields in the Form.xlsx
2. Outputs the invalid names and registration numbers by comparing the two lists
3. Outputs the duplicate elements
###### The Excel documents uploaded here are samples

###### The code could be adapted to automate several Excel related tasks
