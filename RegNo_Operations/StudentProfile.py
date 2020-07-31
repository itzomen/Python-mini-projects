#python3
# StudentProfile.py
#Get student Registration and create profile
#Get Student Number and add to profile

import re

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
    (\d{3})
    (\s | -)?
    (\d{3})
    (\s | -)?
    (\d{3})
    (\s | -)?
    )''', re.VERBOSE)
    
RegNo = 'CT19A096'

if  regNoRegex.match(RegNo):
	print('Valid Reg No')
else:
	print('Invalid Reg No')
