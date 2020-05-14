import os
import pandas as pd
import sys

def decimate(input_number):

	if int(input_number) < 10:
		output_string = "0" + str(input_number)
	else:
		output_string = str(input_number)
	return output_string

def importd():
	labels_name = "labels.txt"
	home = os.getcwd()
	opened_labels_file = pd.read_csv(labels_name, names = ["exp", "user", "label", "inicio", "fim"], sep = " ")
	started_writing = False
	li = []
	for index, row in opened_labels_file.iterrows():
		current_exp = decimate(row["exp"])
		current_user = decimate(row["user"])
		file_name = "data/acc_exp" + current_exp + "_user" + current_user + ".txt"
		opened_file = pd.read_csv(file_name, sep = " ", names = ["X","Y","Z"])
		current_table = opened_file.iloc[row["inicio"]:row["fim"],:]
		current_table["label"] = row["label"]
		if started_writing == False:
			output_table = current_table
			started_writing = True
		else:
			output_table = pd.concat([output_table,current_table], axis = 0)
			if last_user != current_user:
				li.append(output_table)
				started_writing = False
		last_exp = current_exp
		last_user = current_user

	return li


#for files in os.listdir(home):
#	if files.ensdwith(".txt") and files != labels_name:
