import zosftplib

Myzftp = zosftplib.Zftp('mainframe_ip', 
                        'mainframe_userid', 
                        'mainframe_password',
                        timeout=500.0, 
                        sbdataconn='(ibm-1147,iso8859-1)')
Myzftp.download_text('mainframe_dataset_name', '/tmp/local_filename.txt')

mf_file = open('/tmp/local_filename.txt', 'r+')
ffa = mf_file.read(16);
print ("Read record is :", ffa)
mf_file.close()

