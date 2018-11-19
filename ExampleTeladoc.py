import pandas as pd



def loading_data(filename):
	p1 = pd.read_csv(filename,skip_blank_lines=True, keep_default_na=False)
	return p1


def transforming_data(data):
	data['Address 1'] = data['Address 1'].str.replace(',', '')
	data.insert(0,"Primary", "Primary")
	data.insert(1,"Family Plan", "Family Plan")
	data.drop(["Plan", "Employment Status", "Start Date","End Date", "Decline Reason"], axis = 1, inplace = True)
	data.insert(15, "Active", "Active")
	data.drop(0, axis = 0, inplace = True)
	return data


def to_csv(data, newname):	
	data.to_csv(newname+".csv", header = None, index = False)



