#begin import modules
import math
from datascience import *
import numpy as np
# end import modules

#begin msg definitions
default_err_msg = "Something is wrong with your solution.  See if you can figure out what the mistake might be, or ask a neighbor or TA for help!"
type_err_msg = "Your solution is not in the correct format!"
correct_msg = "Your solution is correct!"
okay_msg = "The format of your solution looks okay!"
#end msg definitions


CorrectTable = """FMID    | MarketName                                       | Website
1011871 |  Stearns Homestead Farmers' Market               | http://Stearnshomestead.com
1011878 | 100 Mile Market                                  | http://www.pfcmarkets.com
1012063 |  Caledonia Farmers Market Association - Danville | https://sites.google.com/site/caledoniafarmersmarket/"""


###This function takes tables outlined in the check functions written by the Berkeley Team
###And turns them into datascience.table objects for easy comparison
def string_to_table(TableText):
	FinalTable = Table()
	lines = TableText.split('\n')
	columns = len(lines[0].split("|"))
	for x in range(0,columns):
		ColumnName = lines[0].split("|")[x].strip()
		ArrayForList = []
		for y in lines[1:]:
			z = y.split('|')
			ArrayForList.append(z[x].strip())
			#tupleForArray = tuple(ArrayForList)
		FinalTable = FinalTable.with_columns(ColumnName,np.array(ArrayForList))
	return FinalTable

def CheckTables(Table1,Table2,sortcol = 0,sort = True):
	if sort == True:
		Table1 = Table1.sort(sortcol)
		Table2 = Table2.sort(sortcol)
	ColumnLen = Table1.num_columns
	RowLen =Table1.num_rows
	if (Table1.num_columns == Table2.num_columns) & (Table1.num_rows == Table2.num_rows):
		FinalCheck = True
		for x in range(0,ColumnLen):
			StrArray1 = []
			StrArray2 = []
			for q in range(0,RowLen):
				try:
					StrArray1.append(float(Table1.column(x)[q]))
					StrArray2.append(float(Table2.column(x)[q]))
				except:
					StrArray1.append(str(Table1.column(x)[q].strip()))
					StrArray2.append(str(Table2.column(x)[q].strip()))
			StringArray1 = make_array(StrArray1)
			StringArray2 = make_array(StrArray2)
			ColumnCheck = np.array_equal(StringArray1,StringArray2)
			FinalCheck = FinalCheck & ColumnCheck
		return FinalCheck
	else:
		return False

def check6_1(farmers_markets):
	if isinstance(farmers_markets,Table):
		StudentTable = farmers_markets.select(range(3)).take(range(3)).sort(0)
		ATable = string_to_table(CorrectTable)
		if not CheckTables(StudentTable,ATable,sortcol=0):
			print(default_err_msg)
			print(StudentTable)
			print(ATable)
		else:
			print(correct_msg)
	else:
		print(type_err_msg)
