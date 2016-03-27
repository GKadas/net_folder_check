# net_folder_check

This small script checks if a network folder (Samba) is accessible on the network and reports back with a console message.
If the folder is accessible, it opens the folder.
If the folder is not accessible, it sleeps and retries.

This script was made to be run on a pc that already had access rights provided from Active Directory, so user access was not
taken into account when this was created.
This script checks for folders in a Samba server.
