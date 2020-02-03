# my freenss scripts
This is a collection of the scripts I use on my FreeNAS server. 

--- drive_info.sh ---

Based on a script by: <TBA>
Which can be found here: <TBA>

Get the GPTID and serial number of each HDD in the system.
So that you can physically find a given HDD in the box (by its serial number)

NOTE: Be sure to edit script before use to specify the list of drives


-- jail-backup.sh --
Based on a script by: digiMoot
Which can be found here: http://digimoot.wordpress.com/2020/01/11/freenas-backup-jails-automatically-using-iocage-import-and-export/

Usage: # ./ jail-back.sh <jailname>

Backs up the specified jail

NOTE: Be sure to edit script before use to specifiy backup location
