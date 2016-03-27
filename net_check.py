import time
from win_unc import (DiskDrive, UncDirectory,
                     UncDirectoryConnection, UncDirectoryMount)

# Connect a shared directory without authorization.
unc = UncDirectory(r'\\path\to\file')
conn = UncDirectoryConnection(unc, persistent=True)

while (True):
    conn.connect()

    if (conn.is_connected() == False):
        print '...'
        conn.disconnect()
        time.sleep(60)
    elif (conn.is_connected()== True):
        print 'Connected?', conn.is_connected()
        break
	else:
		print 'You should never see this assuming the script works correctly'


