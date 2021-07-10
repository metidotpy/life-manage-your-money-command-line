# life/Manage Your Money/Command-Line


## Commands

### Help
#### you can use -h or --help for the help command

### Create
#### you can use -cr or --create or -CR for create and database and config
#### like => life -cr test.db or life --create test

### Connect
#### you can use -c or --connect or -C for connect to your database(this command required)
#### like => life -cr test.db -c test.db

### Start
#### you can use -s or --start or -S for start your first money (you can use it one time of your database) you must get an integer to this argument
#### like => life -c test.db -s 2500

### Show
#### you can use -sh or --show or -SH for show your money
#### like => life -c test.dv -sh

### Details
#### you can use -d or --details or -D for details your start money
#### like => life -c test.db -s 3500 -d "my salary"

### Plus
#### you can use -p or --plus or -P for plus your money, you must get an integer to this argument
#### like => life -c test.db -p 25000

### Details Plus 
#### you can use -dp or --details-plus or -DP for add details for your plus
#### like => life -c test.db -p 2500 -dp "sell my pc"

### Minus
#### you can use -m or --minus or -M for minus your money, you must get an integer to this argument
#### like => life -c test.db -m 2500

### Details Minus
#### you can use -dm or --details-minus or -DM for add details for you plus
#### like => life -c test.db -m 2500 -dm "buy a new pc"
