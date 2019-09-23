# -*- coding:utf-8 -*-

def readallstock(filepath):
	filepath=os.path.join(os.getcwd(),"data","allstock.csv")
	allstockdict={}
	with open(filepath, 'r+') as csv_file:
		for line in csv_file:
			no ="%6s"%line.split(",")[0]
			name =line.split(",")[1].decode( "gbk").encode("UTF-8")

			allstockdict[no]=str(name)
			print "%s %s"%(no,str(allstockdict[no]))
	return 