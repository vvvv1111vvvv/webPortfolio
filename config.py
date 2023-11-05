# Puspose: set configures for Mysql
host = '127.0.0.1'
user = 'webuser'
password = '49721447'
db = 'dbForChart'
table = 'tableForChart'
tableColumn = ['id', 'predict_KOSPI', 'actual_KOSPI']
tableSet = tableColumn[0]+' int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, '+tableColumn[1]+' float(9,8), '+tableColumn[2]+' float(9,8)'