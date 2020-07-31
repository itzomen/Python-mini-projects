
# Check Registrayion Number

import re

regNoRegex = re.compile(r'FE(\d{2})A(\d{3})')


text = "This is the registration number of E FE13A067 and C FE17A008. Do you know FE12A056 ou 6"

mo = regNoRegex.search(text)

print('Registration Numbers:' + mo.group())
