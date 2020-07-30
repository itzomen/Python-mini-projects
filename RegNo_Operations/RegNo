# Check Registrayion Number

RegNo = "FE19ARegNo[4] == 'A':096"

def isRegNo(RegNo):
	if len(RegNo) != 8:
		return False
#	for i in range(0,2):
#		if not RegNo[i].isapla():
	#		return False
	for i in range(2,4):
		if not RegNo[i].isdecimal():
			return False
	if RegNo[4] != 'A' or RegNo[4] != 'B':
		return False

	for i in range(5,8):
		if not RegNo[i].isdecimal():
			return False
	return True
	
print(isRegNo(RegNo))
	
