import paramiko


#Print progress to console
progressDict={}
progressEveryPercent=10

for i in range(0,101):
    if i%progressEveryPercent==0:
        progressDict[str(i)]=""

def printProgressDecimal(x,y):
    if int(100*(int(x)/int(y))) % progressEveryPercent ==0 and progressDict[str(int(100*(int(x)/int(y))))]=="":
        print("{}% ({} Transfered(B)/ {} Total File Size(B))".format(str("%.2f" %(100*(int(x)/int(y)))),x,y))
        progressDict[str(int(100*(int(x)/int(y))))]="1"

def sftp(host,port,username,password,remote_path,local_path):
	host = host                   #hard-coded
	port = port
	transport = paramiko.Transport((host, port))

	password = password                #hard-coded
	username = username              #hard-coded
	transport.connect(username = username, password = password)

	sftp = paramiko.SFTPClient.from_transport(transport)

	path = remote_path    #hard-coded
	localpath = localpath
	sftp.put(localpath, path, callback=lambda x,y: printProgressDecimal(x,y))

	sftp.close()
	transport.close()
	print ('Upload done.')


