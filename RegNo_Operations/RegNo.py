
# Check Registrayion Number

RegNo = "FE19A086"

def isRegNo(RegNo):
	if len(RegNo) != 8:
		return False
	for i in range(2,4):
		if not RegNo[i].isdecimal():
			return False
	if RegNo[4] != 'A':
		return False
	for i in range(5,8):
		if not RegNo[i].isdecimal():
			return False
	return True
	
print(isRegNo(RegNo))
