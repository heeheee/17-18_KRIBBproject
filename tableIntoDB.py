import MySQLdb, sys

fileName = sys.argv[1]
tabName = sys.argv[2]

conn=MySQLdb.connect(host="172.20.213.73", user="lastmhc", passwd="lastmhc", db="ccle")
cur=conn.cursor()

f = open(fileName)

header = f.readline()
headerSplit = header.strip().replace("\"","").split("\t")

#for i in range(7):
    #header = f.readline()

dropQ="drop table if exists " + tabName + ";"
cur.execute(dropQ)

query = "create table " + tabName + " (id varchar(30) NOT NULL,symbol varchar(30),"\

for i in range(2,len(headerSplit)):
    query = query + headerSplit[i] +" float,"

query = query[:-1]
query = query + ");"

#print query
    
#query = "create table " + tabName \
#       + " (id varchar(10) NOT NULL,"\
#       + " gsm_id varchar(10) NOT NULL,"\
#       + " gse_id varchar(10) NOT NULL,"\
#       + " table_id varchar(10) NOT NULL,"\
#       + " table_id2 varchar(15) NOT NULL,"\
#       + " symbol varchar(20)"\
#       + ");"


#print query
cur.execute(query)

vals=""

for line in f:
    lineSplit = line.replace("\n","").split("\t")
    vals = ""

    for j in range(len(lineSplit)):
        vals += lineSplit[j].strip() + ","
        #vals += "\""+lineSplit[j].strip()+"\","
	#if(j==0 or j==1 or j==2 or j==5 or j==6 or j == 7 or j == 8):
	    #vals += "\""+lineSplit[j].strip()+"\","
	#else:
	    #vals += lineSplit[j].strip()+","

    query="insert into " + tabName + " values("+vals[0:len(vals)-1]+");"
    #query = query.replace("=\"","=\\\"").replace("\";", "\\\"\;")
    #print query
    cur.execute(query)

query = "alter table " + tabName + " add index name(id);"
cur.execute(query)

conn.commit()
        
cur.close()
conn.close()
