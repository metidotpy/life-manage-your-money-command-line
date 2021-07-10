#!/usr/bin/python3

# Import Modules
import sqlite3
import argparse
import os.path
from colorama import Fore

#connect from database function
def connection(path):
    if path.endswith(".db"):
        con=sqlite3.connect(path)
        cur=con.cursor()
    else:
        con=sqlite3.connect(f"{path}.db")
        cur=con.cursor()
    return con,cur
#make table money
def make_table_money(con,cur):
    command='''CREATE TABLE IF NOT EXISTS Money(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Money INTEGER NOT NULL,
        Details VARCHAR(500) NOT NULL
    );'''
    cur.execute(command)
    con.commit()


#insert to money Table
def insert_money(con,cur,data):
    command='''
    INSERT INTO Money (Money,Details) VALUES (?,?)
    '''
    cur.execute(command,data)
    con.commit()

#select the last money
def select_last_money(con,cur):
    command='SELECT Money FROM Money ORDER BY ID DESC LIMIT 1'
    cur.execute(command)
    datas=cur.fetchone()
    for data in datas:
        return data
    con.commit()
#select last Details
def select_last_details(con,cur):
    command='SELECT Details FROM Money ORDER BY ID DESC LIMIT 1'
    cur.execute(command)
    datas=cur.fetchone()
    for data in datas:
        return data
    con.commit()
#select first money
def select_first_money(con,cur):
    command='SELECT Money FROM Money ORDER BY ID ASC LIMIT 1'
    cur.execute(command)
    datas=cur.fetchone()
    con.commit()
    if datas:
        return True
    else:
        return False



# Create ArgumentParser Object

parser=argparse.ArgumentParser(
    description="Welcome to Life Command-Line App for manage Your life",
    prog="life",
    usage="%(prog)s [options]",
    epilog="Write By meti.py\nFollow Me On Github\nhttps://github.com/metidotpy"
)


#add connection command
parser.add_argument(
    '-cr',
    '--create',
    '-CR',
    help='''\
        Create Your Database, And make some config,
        like => -cr [your database name]
        '''
)

#connect to database with name this path
parser.add_argument(
    '-c',
    '--connect',
    '-C',
    help='''\
        Connect To Your Database,
        like => -c [your database name]
    ''',
    required=True
)

#create add salary to the Salary Table
parser.add_argument(
    '-s',
    '--start',
    '-S',
    help='''\
        this command for add your first money or everything you thinks its money,
        like => -s [money 2500000]
    ''',
    type=int
)

#create add details argument
parser.add_argument(
    '-d',
    '--details',
    '-D',
    help='''\
        this command for add details to your datas,
        like => -d ["your details"]
    ''',
    type=str,
    default="Not Details"
)

# add plus and minus argument
parser.add_argument(
    '-p',
    '--plus',
    '-P',
    help='''\
        this command plus your new money to the your money,
        like => -p [your money]
    ''',
    type=int
)

parser.add_argument(
    '-dp',
    '--details-plus',
    '-DP',
    help='''\
        this command for add details to your plus datas,
        like => -dp ["your details for plus"]
    ''',
    type=str,
    default="Not Details"
)

parser.add_argument(
    '-m',
    '--minus',
    '-M',
    help='''\
        this command minus your new money to the your money,
        like => -p [your money]
    ''',
    type=int
)

parser.add_argument(
    '-dm',
    '--details-minus',
    '-DM',
    help='''\
        this command for add details to your minus datas,
        like => -dp ["your details for minus"]
    ''',
    type=str,
    default="Not Details"
)

#show your money
parser.add_argument(
    '-sh',
    '--show',
    '-SH',
    help='''Show Your Last Money From Your Database,
    like => -s
    ''',
    action="store_true"
)

#parse my arguments
arguments = parser.parse_args()



#conds for handle arguments

if arguments.create:
    if os.path.exists(f"{arguments.create}.db") or os.path.exists(f"{arguments.create}"):
        print(Fore.RED+"This File Is Exists, I cant Create A new file!")
    else:
        con,cur=connection(arguments.create)
        make_table_money(con,cur)
        print(Fore.LIGHTGREEN_EX+"I Create This Database From {}".format(os.path.realpath(__file__)))
        con.close()

if arguments.connect:
    if os.path.exists(f"{arguments.connect}.db") or os.path.exists(f"{arguments.connect}"):
        con,cur=connection(arguments.connect)
        print(Fore.LIGHTGREEN_EX+"I Connected To Your Database")
        con.close()
    else:
        print(Fore.RED+"I Cant Find This Database")


if (arguments.connect and arguments.start and arguments.details) or (arguments.connect and arguments.start):
    if os.path.exists(f"{arguments.connect}.db") or os.path.exists(f"{arguments.connect}"):
        con,cur=connection(arguments.connect)
        if(select_first_money(con,cur)):
            print(Fore.RED+"Sorry, You Have First Money From This Database :),\nYou Can Use [-p [your money]] or Use [-m [your money]]")
        else:
            data=[arguments.start,arguments.details]
            insert_money(con,cur,data=data)
            con.close()
            print(Fore.LIGHTGREEN_EX+f"Add Your Data To Your Database\nYour Data => [Start with => {arguments.start}, Details => '{arguments.details}]'")
    else:
        print(Fore.RED+"I Cant Find This Database")


if (arguments.plus and arguments.connect and arguments.details_plus) or (arguments.plus and arguments.connect):
    if os.path.exists(f"{arguments.connect}.db") or os.path.exists(f"{arguments.connect}"):
        con,cur=connection(arguments.connect)
        LAST_MONEY=select_last_money(con,cur)
        LAST_DETAILS=select_last_details(con,cur)
        NEW_DATA=[LAST_MONEY + arguments.plus,arguments.details_plus]
        insert_money(con,cur,NEW_DATA)
        print(Fore.LIGHTGREEN_EX+f"Plus Your Money [OLD => {LAST_MONEY} to NEW => {NEW_DATA[0]}]\nYour Data [Money => {NEW_DATA[0]}, Details => {arguments.details_plus}]")
        con.close()
    else:
        print(Fore.RED+"I Cant Find This Databas")

if (arguments.minus and arguments.connect and arguments.details_minus) or (arguments.minus and arguments.connect):
    if os.path.exists(f"{arguments.connect}.db") or os.path.exists(f"{arguments.connect}"):
        con,cur=connection(arguments.connect)
        LAST_MONEY=select_last_money(con,cur)
        LAST_DETAILS=select_last_details(con,cur)
        NEW_DATA=[LAST_MONEY - arguments.minus,arguments.details_minus]
        insert_money(con,cur,NEW_DATA)
        print(Fore.LIGHTGREEN_EX+f"Minus Your Money [OLD => {LAST_MONEY} to NEW => {NEW_DATA[0]}]\nYour Data [Money => {NEW_DATA[0]}, Details => {arguments.details_minus}]")
        con.close()
    else:
        print(Fore.RED+"I Cant Find This Databas")

if arguments.show:
    if os.path.exists(f"{arguments.connect}.db") or os.path.exists(f"{arguments.connect}"):
        con,cur=connection(arguments.connect)
        LAST_MONEY=select_last_money(con,cur)
        LAST_DETAILS=select_last_details(con,cur)
        print(
            Fore.LIGHTGREEN_EX+
            f"Your Money is Money => {LAST_MONEY}, Details => {LAST_DETAILS}"
        )

    else:
        print(Fore.RED+"I Cant Find This Databas")