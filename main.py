import teladoc, sftp

pointeNorth = Transform(filename, newname)
p1 = pointeNorth.loadingdata(filename)
pointeNorth.transforming_data(p1)
pointeNorth.to_csv(p1, pointeNorth.newname)
sftp.sftp(host,port,username,password,remote_path,pointeNorth.newname)