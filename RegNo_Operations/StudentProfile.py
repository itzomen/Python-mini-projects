#python3
# StudentProfile.py
#Get student Registration and create profile
#Get Student Number and add to profile

import re, sys

# Registration Number Regex

regNoRegex = re.compile(r'''(
    ([ACEFLS][RVTDEPCM])  #Faculty
    (\d{2})      #Year registered
    ([ABC])        #Category
    (\d{3})      #Number
    )''',  re.VERBOSE)

# Student's Number Regex

phoneNoRegex = re.compile(r'''(
    [+]?    # + symbol 
    (\d{3} | \d{2} )? #country code
    (\s | -)?               #separator
    (\d)?
    (\d{2})
    (\s | -)?
    (\d{2})
    (\s | -)?
    (\d{2})
    (\s | -)?
    (\d{2})
    )''', re.VERBOSE)
    
RegNo = 'FE18A096'
Number = '+45 651 31 37 78'

if  regNoRegex.match(RegNo):
	print('Valid Reg No')
else:
	sys.exit('Exit, Invalid Reg No')
if phoneNoRegex.match(Number):
	print('Valid No')
else:
	sys.exit('Exit, invalid No')
	
# TODO: Correct RegNo and phone numbers are used to create student profile
