import mysql.connector, datetime, random, os
from tabulate import tabulate
def database_check():
    def create(purpose):
        print("| Database {} Operation".format(purpose))
        print("| Loading: [",end='')
        qry = "CREATE DATABASE mall_management"
        mycursor.execute(qry)
        print("==",end='')
        qry = "USE mall_management"
        mycursor.execute(qry)
        qry = "CREATE TABLE CUSTOMER(C_ID VARCHAR(15),NAME VARCHAR(15),AGE INT,ADDRESS VARCHAR(35),CONTACT BIGINT,EMAIL VARCHAR(30),PASSWD VARCHAR(25))"
        mycursor.execute(qry)
        print("==",end='')
        qry = "create table sessions(C_ID VARCHAR(20) NOT NULL, BILL_ID VARCHAR(10) NOT NULL,SERIAL_NO INT NOT NULL,DATE_OF_ISSUE DATE NOT NULL)"
        mycursor.execute(qry)
        qry = "CREATE TABLE BILLS(BILL_ID VARCHAR(10) NOT NULL,C_ID VARCHAR(20) NOT NULL,TEXTILEBILL INT DEFAULT 0,FOODBILL INT DEFAULT 0,MOVIEBILL INT DEFAULT 0,GME_BILL INT DEFAULT 0,ELECTRONICSBILL INT DEFAULT 0,STATIONARYBILL INT DEFAULT 0,COSMETICSBILL INT DEFAULT 0,GAMEBILL INT DEFAULT 0,STATUS VARCHAR(7))"
        mycursor.execute(qry)
        print("==",end='')
        qry = "CREATE TABLE ELECTRONICS(P_ID VARCHAR(10),NAME VARCHAR(25),BRAND VARCHAR(20), PRICE INT)"
        mycursor.execute(qry)
        print("==",end='')
        qry = "INSERT INTO ELECTRONICS VALUES('L01259', 'LAPTOP', 'DELL', 59999),('M202456', 'MOBILE', 'REDMI', 14999),('T87542', 'TV', 'LG', 44999),('B8950','AIR PODS','BOAT',1499),('G98987','GAMING CONSOLE','NVIDIA',49999),('G2493','GRAPHICS CARD','ASUS',64999),('B19430','BT SPEAKER','ZEBRONICS',4999),('S23693','SMART WATCH','SAMSUNG',34999),('P93651','PENDRIVE 128GB','SANDISK',1499),('S12985','SD CARD 64GB','SAMSUNG',799),('W14703','WIFI ADAPTER (10-70 mb/s)','TP-LINK',899),('B75390','BT ADAPTER','TP-LINK',599)"
        mycursor.execute(qry)
        print("==",end='')
        qry = "CREATE TABLE FOOD(D_ID VARCHAR(20),NAME VARCHAR(20),CATAGORY VARCHAR(7),PRICE INT)"
        mycursor.execute(qry)
        print("==",end='')
        qry = "INSERT INTO FOOD(D_ID,NAME,PRICE) VALUES('V2036', 'NOODLES', 100),('NV2036', 'NOODLES', 150),('V2016', 'BURGER', 95),('NV2016', 'BURGER', 120),('V4678','MOMOS',200),('V6023','PANI-PURI',30),('V5029','PIZZA',250),('V7854','SANDWITCH',70),('V1874','WRAP',120),('V1937','NUGGETS',80),('V4764','SAMOSA',45),('V8008','BIRIYANI',170),('V2082','CAKE',350),('V7521','COFFEE',50),('V8721','TEA',50),('V9526','SMOOTHY',80),('V4761','PANCAKE',50),('V2480','MILKSHAKE',120),('V2220','ICE-CREAM',100),('NV2069','WRAP',150),('NV6874','PIZZA',200),('NV6520','SANDWITCH',170),('NV4793','NUGGETS',120),('V2013','CHEESE-BALLS',130),('V9871','BIRIYANI',250)"
        mycursor.execute(qry)
        qry = "UPDATE FOOD SET CATAGORY = 'VEG' WHERE D_ID LIKE 'V%'"
        mycursor.execute(qry)
        qry = "UPDATE FOOD SET CATAGORY = 'NON-VEG' WHERE D_ID LIKE 'NV%'"
        mycursor.execute(qry)
        print("==",end='')
        qry = "CREATE TABLE MOVIE(M_ID VARCHAR(20),NAME VARCHAR(20),PRICE INT)"
        mycursor.execute(qry)
        print("==",end='')
        qry = "INSERT INTO MOVIE VALUES('BIO357', 'THE AVIATOR', 120),('COM341', 'INSIDE OUT 2', 120),('ADV583', 'DUNE: PART TWO', 150),('ADV326', 'THE MUMMY', 100),('FCY491', 'THE FLASH', 120)"
        mycursor.execute(qry)
        print("==",end='')
        qry = "CREATE TABLE PURCHASE(PUR_ID VARCHAR(30) NOT NULL,BILL_ID VARCHAR(10) NOT NULL,C_ID VARCHAR(20),PID VARCHAR(7),CATAGORY VARCHAR(20),PRICE INT,QUT INT,AMOUNT INT,PUR_DATE DATE)"
        mycursor.execute(qry)
        print("==",end='')
        qry = "CREATE TABLE TEXTILE(P_ID VARCHAR(10),NAME VARCHAR(20),CATAGORY VARCHAR(20),BRAND VARCHAR(20),PRICE INT)"
        mycursor.execute(qry)
        print("==",end='')
        qry = "INSERT INTO TEXTILE VALUES('K01324', 'T-SHIRT', 'KIDS', 'JAGUVAR', 799),('G04963', 'SHIRT', 'MALE', 'OTTO', 999),('K04957', 'TRACKS', 'KIDS', 'GRAVITY', 699),('L0356', 'TOPS', 'FEMALE', 'PUMA', 899),('G01324','T-SHIRT','MALE','ALLEN SOLLY',899),('G94783','COURT SUIT','MALE','RAYMOND',9999),('L52935','SAREE','FEMALE','SABYASACHI',1499),('M20459','SWEATERS','MALE','MONTE CARLO',999),('L20459','SWEATERS','FEMALE','HUNDRED',999),('K20459','SWEATERS','KIDS','CHOCO',799),('K05357','JEANS','KIDS','LILLIPUT',499),('L50349','PALAZZO','FEMALE','SMOKE',599),('L50350','KURTHI','FEMALE','TEDY',1799)"
        mycursor.execute(qry)
        print("==",end='')
        qry = "CREATE TABLE STATIONARY(P_ID VARCHAR(20),NAME VARCHAR(30),BRAND VARCHAR(25),PRICE INT);"
        mycursor.execute(qry)
        print("==",end='')
        qry = "INSERT INTO STATIONARY VALUES('P2487','PENCIL','DOMS',10),('E5486','ERASER','APSARA',5),('I1298','FOUNTAIN-PEN','CAMLIN',50),('C8075','COLOR-PENCIL','FABRI-CASTEL',100),('B4927','BRUSH-PENS','CLASSMATE',120),('W3254','WATER-COLOURS','CAMLIN',125),('I5835','INK-BOTTLE','BRIL',30),('P5310','MACHANICAL-PENCIL','PENTONIC',25)"
        mycursor.execute(qry)
        print("==",end='')
        qry = "CREATE TABLE COSMETICS(P_ID VARCHAR(10),NAME VARCHAR(20),BRAND VARCHAR(20),PRICE INT)"
        mycursor.execute(qry)
        print("==",end='')
        qry = "INSERT INTO COSMETICS VALUES('E24510','LIQUID EYESHADOW','NORTHERN LIGHTS',599),('L49837','LIPSTICK','LAKME',249),('F25791','FACE PALETTE','FANTASY',299),('S67851','TRAVEL SET','STAR',1199),('L95316','LIP BALM','POPSTAR',229),('K76491','KAJAL','FAB',149),('E32795','LIQUID EYELINER','MARS',199),('M94283','FACE MASK','CANEL',179),('R54328','ROLL-ON','NIVIA',149),('M34876','MOISTUTIZER','BIOTIQUE',149),('B34671','BEAUTY CREAM','PONDS',169),('F26915','FOUNDATION','PRADA',199),('M95842','MASCARA','MAYBELLINE',259)"
        mycursor.execute(qry)
        print("==",end='')
        qry = "ALTER TABLE COSMETICS ADD STOCK INT"
        mycursor.execute(qry)
        qry = "select p_id from cosmetics"
        mycursor.execute(qry)
        myrec = mycursor.fetchall()
        for rec in myrec:
            rand = random.randint(30, 90)
            qry = "update cosmetics set stock = {} where p_id = '{}'".format(
                rand, rec[0])
            mycursor.execute(qry)
        qry = "ALTER TABLE TEXTILE ADD STOCK INT"
        mycursor.execute(qry)
        qry = "select p_id from TEXTILE"
        mycursor.execute(qry)
        myrec = mycursor.fetchall()
        for rec in myrec:
            rand = random.randint(30, 90)
            qry = "update TEXTILE set stock = {} where p_id = '{}'".format(
                rand, rec[0])
            mycursor.execute(qry)
        qry = "ALTER TABLE ELECTRONICS ADD STOCK INT"
        mycursor.execute(qry)
        qry = "select p_id from ELECTRONICS"
        mycursor.execute(qry)
        myrec = mycursor.fetchall()
        for rec in myrec:
            rand = random.randint(10, 50)
            qry = "update ELECTRONICS set stock = {} where p_id = '{}'".format(
                rand, rec[0])
            mycursor.execute(qry)
        qry = "ALTER TABLE STATIONARY ADD STOCK INT"
        mycursor.execute(qry)
        qry = "select p_id from STATIONARY"
        mycursor.execute(qry)
        myrec = mycursor.fetchall()
        for rec in myrec:
            rand = random.randint(30, 90)
            qry = "update STATIONARY set stock = {} where p_id = '{}'".format(rand, rec[0])
            mycursor.execute(qry)
        qry = "CREATE TABLE STOCK(S_ID VARCHAR(10),P_ID VARCHAR(10),CATAGORY VARCHAR(20),QUT INT,STATUS VARCHAR(10))"
        mycursor.execute(qry)
        print("==",end='')
        qry = "CREATE TABLE SNACKS(S_ID VARCHAR(5),NAME VARCHAR(20),PRICE INT)"
        mycursor.execute(qry)
        qry = "insert into snacks values('C5481','COKE',100),('P1010','POPCORN',120),('C6032','COOKIES',80),('F2827','FRIES',100),('I8426','ICE CREAM',75),('C5010','POTATO CHIPS',60)"
        mycursor.execute(qry)
        qry = "CREATE TABLE game(G_ID VARCHAR(6),NAME VARCHAR(20),PRICE INT)"
        mycursor.execute(qry)
        qry = "INSERT INTO game(G_ID,NAME,PRICE) VALUES('S43297', 'Swimming', 500), ('F12345', 'Football', 800), ('T67890', 'Tennis', 600), ('C82345', 'Cricket', 700), ('B98765', 'Basketball', 400), ('V54321', 'Volleyball', 300), ('G45678', 'Golf', 600), ('P98701', 'Ping Pong', 200), ('S56432', 'Soccer', 700)"
        mycursor.execute(qry)
        qry = "CREATE TABLE CASHIER(E_ID VARCHAR(7),NAME VARCHAR(20),PASSWD VARCHAR(20))"
        mycursor.execute(qry)
        qry = "CREATE TABLE RETURNED(PUR_ID VARCHAR(20),BILL_ID VARCHAR(10),C_ID VARCHAR(10),PID VARCHAR(10),CATAGORY VARCHAR(20),PRICE INT, QUT INT,AMOUNT INT, RETURN_DATE DATE)"
        mycursor.execute(qry)
        mydb.commit()
        print(']')
        print("| Database {} Successfull !!".format(purpose))
        print("+-------------------------------------------------------------+")
    mydb = mysql.connector.connect(host='localhost',user='Kishore',passwd='Kishore@2008')
    if mydb.is_connected():
        mycursor = mydb.cursor()
        qry = "show databases"
        mycursor.execute(qry)
        data = mycursor.fetchall()
        dbs = [i[0] for i in data]
        run = 'mall_management' in dbs
        if run == False:
            print("+-------------------------------------------------------------+")
            print("|                   MALL MANAGEMENT PROGRAM                   |")
            print("+-------------------------------------------------------------+")
            print("| The Database Required for this Program is Not Available...")
            start = input("| Enter Y to start Database Creation: ")
            if start.lower() == 'y':
                create('Creation')
                return True
            else:
                print("| Creation Aborted !!")
                print("+-------------------------------------------------------------+")
                return False
        elif run == True:
            qry = "use mall_management"
            mycursor.execute(qry)
            qry = "show tables"
            mycursor.execute(qry)
            info = mycursor.fetchall()
            tables = [i[0] for i in info]
            if not (tables == ['admin', 'bills', 'cashier', 'cosmetics', 'customer', 'electronics', 'food', 'game', 'movie', 'purchase', 'returned', 'sessions', 'snacks', 'stationary', 'stock', 'textile'] or tables == ['bills', 'cashier', 'cosmetics', 'customer', 'electronics', 'food', 'game', 'movie', 'purchase', 'returned', 'sessions', 'snacks', 'stationary', 'stock', 'textile']):
                print("+--------------------------------------------------------------------------------+")
                print("|                            MALL MANAGEMENT PROGRAM                             |")
                print("+--------------------------------------------------------------------------------+")
                print("| There were some tables missing in the Database...")
                print("| To Run this Program, the Database must be Re-created...")
                print("| (Note: Re-Creation may lead to loss of customer, admin, bill and purchase data)")
                recreate = input("| Enter Y to Re-create the Database: ")
                if recreate.lower() == 'y':
                    qry = "drop database mall_management"
                    mycursor.execute(qry)
                    create('Re-Creation')
                    return True
                else:
                    print("Exiting...")
                    print("Program Ended !!")
                    return False
            else:
                return True
        else:
            print("Exiting...")
            print("Program Ended !!")
            return False
        
def clrscreen():
    os.system('cls')
        
def addcustomer():                #To Add the Customer Details
    print('',"CUSTOMER ADDING OPERATAION",'--------------------------',sep='\n')
    name = input("Enter Customer Name: ").upper()
    while True:
        try:age = int(input("Enter Customer Age: "));break
        except ValueError:print("Only Integers are allowed !!")
    address = input("Enter Customer Address: ").upper()
    while True:
        contact = int(input("Enter Mobile Number: "))
        if len(str(contact)) == 10:break
        else:print("Enter a Valid Mobile Number !!")
    while True:
        email = input("Enter E-Mail Address: ").lower()
        if '@' in email: break
        else: print("Enter a Valid E-Mail Addreass !!")
    while True:
        print("+-----------------------------------------+")
        print("Password Creation","-----------------",sep='\n')
        passwd1=input("Create Password: ")
        passwd2 = input("Enter Password Again: ")
        if passwd1 != passwd2:
            print("Password Does Not Match !!")
            print("Please Try Again...")
        else:
            print("Password Set Successfully !!")
            print("+-----------------------------------------+")
            break
    rand = int(random.random()*(10**7))
    c_id = 'C'+str(int(rand))
    qry = "select c_id from customer where c_id = '{}'".format(c_id)
    mycursor.execute(qry)
    resrec_1 = mycursor.fetchone()
    b_rand = int(random.random()*(10**9))
    bill_id = 'B'+str(b_rand)
    qry = "select bill_id from bills where bill_id = '{}'".format(bill_id)
    mycursor.execute(qry)
    date = (datetime.datetime.now()).date()
    resrec_2 = mycursor.fetchone()
    if resrec_1 == None and resrec_2 == None:
        qry = "insert into customer values('{}','{}',{},'{}',{},'{}','{}')".format(c_id,name,age,address,contact,email,passwd1)
        mycursor.execute(qry)
        mydb.commit()
        qry = "insert into bills(bill_id,c_id,status) values('{}','{}','PENDING')".format(bill_id,c_id)
        mycursor.execute(qry)
        qry = "insert into sessions(c_id,bill_id,serial_no,date_of_issue) values('{}','{}',1,'{}')".format(c_id,bill_id,date)
        mycursor.execute(qry)
        mydb.commit()
        print("One new customer added successfully")
        print("+-------------------------------------------------------+")
        print("| Please Note your Customer Id:",c_id,'               |')
        print("| This Customer ID is used for Logging into the Mall    |")
        print("+-------------------------------------------------------+")
    else:
        print("Unexpected Problem Occured...")
        print("Restarting...")
        addcustomer()
    rand = input("Press any key to Continue...")
    clrscreen()
    
def get_titles(table):          #To get the Column Names for Given Table
    qry = "describe {}".format(table)
    mycursor.execute(qry)
    titles = [rec[0] for rec in mycursor]
    return titles


def insertion(table):          #To Add Details in Given Section
    print('',"ADDITION OPERATION",'------------------',sep='\n')
    titles = get_titles(table)
    dicti = dict()
    for i in range(len(titles)):
        stmt = "Enter " + titles[i] + ": "
        value = input(stmt).upper()
        if titles[i] in ('price','PRICE'):
            dicti[titles[i]] = int(value)
        else:
            dicti[titles[i]] = value
    values = tuple(dicti.values())
    qry = "insert into {} values{}".format(table,values)
    mycursor.execute(qry)
    mydb.commit()
    print("One Record Inserted Successfully !!")
    print('*'*65)

def viewer(table):             #To View the available products
    print("-"*65)               
    titles = get_titles(table)
    qry = "select * from {}".format(table)
    mycursor.execute(qry)
    krec = mycursor.fetchall()
    tbl = krec
    if table.lower() == 'textile':
        print('\t\t AVAILABLE DRESSES','\t\t -----------------',sep='\n')
    elif table.lower() == 'movie':
        print('\t MOVIES LIST','\t -----------',sep='\n')
    elif table.lower() == 'purchase':
        print('\t\t\t\t PURCHASE','\t\t\t\t ---------',sep='\n')
    elif table.lower() == 'customer':
        print('\t\t\t\t\t CUSTOMERS','\t\t\t\t\t ---------',sep='\n')
    elif table.lower() == 'electronics':
        print('\t\t ELECTRONICS','\t\t -----------',sep='\n')
    elif table.lower() == 'bills':
        print('\t\t\t\t\t BILLS','\t\t\t\t\t -----',sep='\n')
    elif table.lower() == 'stationary':
        print("\t\t\tSTATIONARY ITEMS","\t\t\t----------------",sep='\n')
    elif table.lower() == 'cosmetics':
        print("\t\t\tCOSMETIC PRODUCTS","\t\t\t-----------------",sep='\n')
    elif table.lower() == 'stock':
        print("\t\t\tSTOCK ORDERS","\t\t\t------------",sep='\n')
    elif table.lower() == 'food':
        print("\t\t\tDISHES AVAILABLE","\t\t\t----------------",sep='\n')
    elif table.lower() == 'game':
        print("\t\t\tAVAILABLE GAMES","\t\t\t---------------",sep='\n')
    elif table.lower() == 'snacks':
        print("\t\t\tAVAILABLE SNACKS","\t\t\t----------------",sep='\n')
    elif table.lower() == 'returned':
        print("\t\t\tRETURNED PRODUCTS","\t\t\t-----------------",sep='\n')
    print(tabulate(krec,headers=titles,tablefmt='pretty'))
    print("-"*65)

def edit(table,id):                #To Edit the products
    print('',"EDITION OPERATION",'-----------------',sep='\n')
    pid = input("Enter the Required ID to be Edited: ").upper()
    titles = get_titles(table)
    qry = "select * from {} where {} = '{}'".format(table,id,pid)
    mycursor.execute(qry)
    edrec = mycursor.fetchone()
    if edrec != None:
        print("The Found Record is: ")
        print(tabulate([edrec],headers=titles,tablefmt='pretty'))
        print("Available Fields: ",titles)
        fld = input("Enter the Field name you want to Edit: ")
        if fld.upper() in titles:
            val = input("Enter the Value you want to Set: ").upper()
            if fld in ('price','PRICE','Price'):
                qry = "update {} set {}={} where {} = '{}'".format(table,fld,int(val),id,pid)
            else:
                qry = "update {} set {}='{}' where {} = '{}'".format(table,fld,val,id,pid)
            mycursor.execute(qry)
            mydb.commit()
            print("Record Updated Successfully !!")
            if fld.upper() in ('P_ID','D_ID','M_ID','C_ID'):
                pid = val
            qry = "select * from {} where {} = '{}'".format(table,id,pid)
            mycursor.execute(qry)
            edrec = mycursor.fetchone()
            mydb.commit()
            print("After Updating Record is: ")
            print(tabulate([edrec],headers=titles,tablefmt='pretty'))
        else:
            print("Wrong Field Name Entered !!")
            print("Editing Aborted...")
    else:
        print("Wrong ID Provided...")
        print("Editing Operation Aborted !!")
def delete(table,id):              #To Delete a product
    print('','DELETION OPERATION','------------------',sep='\n')
    pid = input("Enter the Reqired ID to be Deleted: ")
    qry = "select * from {} where {} = '{}'".format(table,id,pid)
    mycursor.execute(qry)
    dresult = mycursor.fetchone()
    if dresult != None:
        delrec = [dresult]
        titles = get_titles(table)
        print(tabulate(delrec,headers=titles,tablefmt='pretty'))
        print("The Above Record will be Deleted...")
        choi = input("Are you sure to Continue <Y/N>? ")
        if choi in 'Yy':
            qry = "delete from {} where {} = '{}'".format(table,id,pid)
            mycursor.execute(qry)
            mydb.commit()
            print("One Record has been Successfully Deleted !!")
        else:
            print("Deletion Aborted !!")
    else:
        print("Wrong ID Provided...")
        print("Deletion Aborted !!")

def purchase(table,id,search):           #To Purchase a product 
    print("","PRODUCT PURCHASE","----------------",sep='\n')
    if not search:viewer(table)   
    tble = table
    idfld = id
    now = datetime.datetime.now()
    PurchaseID = "P" + str(now.year) + str(now.month) + str(now.day) + str(datetime.datetime.now().microsecond)
    M_ID = input("Enter the Required ID: ").upper()
    qry = "select * from {} where {} = '{}'".format(table,id,M_ID)
    mycursor.execute(qry)
    rec = mycursor.fetchone()
    if rec != None:
        print("Requested Product Is:")
        print(tabulate([rec],headers=get_titles(table),tablefmt='pretty'))
        proceed = input("Proceed Purchase <Y/N>? ")
    else:
        print("Wrong {} Entered...".format(id.upper()))
        print("Purchasing Aborted !!")
        rand = input("Press Any Key to Continue...")
        clrscreen()
        return False
    qry = "select status from bills where c_id = '{}' and bill_id = '{}'".format(c_id,bill_id)
    mycursor.execute(qry)
    pstatus = mycursor.fetchone()[0]
    if proceed.lower()=='y' and pstatus.upper() == 'PENDING':
        msg = {'movie':'Number of Tickets','food':'Quantity of Items','game':'Number of Hours'}
        Qut = int(input("Enter the {}: ".format(msg.get(table,'Quantity'))))
        qry = 'select price from {} where {} = "{}"'.format(table,idfld,M_ID)
        mycursor.execute(qry)
        res = mycursor.fetchone()
        for x in res:
            pri = x
        Tot = pri * Qut
        mnth = now.month
        if mnth <= 9:
            mnth = '0'+str(mnth)
        else:
            mnth = str(mnth)
        day = now.day
        if day <= 9:
            day = '0'+str(day)
        else:
            day = str(day)
        dt = str(now.year) + '-' + str(mnth) + '-' + str(day)
        if table.lower() in ('movie','food','game','snacks'):
            qry ="insert into purchase(pur_id,bill_id,c_id,pid,catagory,price,qut,amount,pur_date) values('{}','{}','{}','{}','{}',{},{},{},'{}')".format(PurchaseID,bill_id,c_id,M_ID,tble.upper(),pri,Qut,Tot,dt)
            mycursor.execute(qry)
            mydb.commit()
            if table.lower() == 'snacks':
                billheader = 'movie'
            else:
                billheader = table
            billnm = billheader + 'bill'
            print('Your Final Amount is:',Tot)
            qry = "select {} from bills where c_id = '{}'".format(billnm,c_id)
            mycursor.execute(qry)
            recd = mycursor.fetchone()
            if None in recd:
                qry = "update bills set {}={} where c_id = '{}' and bill_id = '{}'".format(billnm, Tot,c_id,bill_id)
            else:
                qry = "update bills set {}={}+{} where c_id = '{}' and bill_id = '{}'".format(billnm,billnm,Tot,c_id,bill_id)
            mycursor.execute(qry)
            mydb.commit()
            print("Your",table.capitalize(),"Bill Saved Successfully !!")
        else:
            qry = "select stock from {} where {} = '{}'".format(table,id,M_ID)
            mycursor.execute(qry)
            stock = mycursor.fetchone()[0]
            if stock - Qut >= 0:
                qry = "update {} set stock = stock - {} where {} = '{}'".format(table,Qut,id,M_ID)
                mycursor.execute(qry)
                qry ="insert into purchase(pur_id,bill_id,c_id,pid,catagory,price,qut,amount,pur_date) values('{}','{}','{}','{}','{}',{},{},{},'{}')".format(PurchaseID,bill_id,c_id,M_ID,tble.upper(),pri,Qut,Tot,dt)
                mycursor.execute(qry)
                mydb.commit()
                billnm = table + 'bill'
                print('Your Final Amount is:',Tot)
                qry = "select {} from bills where c_id = '{}' and bill_id = '{}'".format(billnm,c_id,bill_id)
                mycursor.execute(qry)
                recd = mycursor.fetchone()
                if None in recd:
                    qry = "update bills set {}={} where c_id = '{}' and bill_id = '{}'".format(billnm, Tot,c_id,bill_id)
                else:
                    qry = "update bills set {}={}+{} where c_id = '{}' and bill_id = '{}'".format(billnm,billnm,Tot,c_id,bill_id)
                mycursor.execute(qry)
                mydb.commit()
                print("Your",table.capitalize(),"Bill Saved Successfully !!")
            else:
                print('Insuffecient Stock !!')
                print('Please Check the Stock Quantity !!')
    elif pstatus.upper() == 'PAID':
        print("It Seems that your Bill have Closed Already.")
        print("Hence, Your Cant make any further Purchases...")
        print("Purchasing Aborted...")
    else:
        print("Purchasing Aborted...")
    rand = input("Press Any key to Continue...")
    clrscreen()
def searchfield(table):         #To Apply Filters and Find the Product
    print("*"*65)
    print('',"SEARCH OPEARTION",'----------------',sep='\n')
    titles = get_titles(table)
    print("Available Fields: ",titles)
    field = input("Enter the field name you want to Search: ")
    if field.lower() == 'price' or field.lower() == 'age':
        st_range = int(input("Enter Price Starting Range: "))
        end_range = int(input("Enter Price Ending Range: "))
        qry = "select * from {} where price between {} and {}".format(table,st_range,end_range)
        mycursor.execute(qry)
        myrecrd = mycursor.fetchall()
    else:
        value = input("Enter the value to be Searched: ")
        qry = "select * from {} where {}='{}'".format(table,field,value)
        mycursor.execute(qry)
        myrecrd = mycursor.fetchall()
    titles = get_titles(table)
    if myrecrd:
        print(tabulate(myrecrd,headers=titles,tablefmt='pretty'))
        schoi = input("Do you want to Purchase any Products Above <Y/N>: ")
        if schoi.lower() == 'y': 
            mycursor.execute("desc {}".format(table))
            sid = mycursor.fetchall()[0][0]
            purchase(table,sid,True)
    else:
        print("No Products Found !!")
        rand = input("Press Any Key to Continue...")
        print("*"*65)
        clrscreen()

def returnprdct(table,id):      #To Return a Purchased Product
    print('',"PRODUCT RETURN OPERATION",'------------------------',sep='\n')
    print("+------------------------------------------------------------------+")
    print("|                   RETURN OPERATION MESSAGE                       |")
    print("+------------------------------------------------------------------+")
    print("| Your Return Will be Processed if and only if you apply return    |")
    print("|  from 5 days of purchase...                                      |")
    p_id = input("| Enter the Returning Product's id: ").upper()
    qry = "select count(*) from purchase where catagory = '{}' and c_id = '{}' and pid = '{}' and bill_id='{}' ".format(table,c_id,p_id,bill_id)
    mycursor.execute(qry)
    crec =mycursor.fetchone()
    cnt = crec[0]
    if cnt == 1:
        qry = "select pur_date from purchase where catagory = '{}' and c_id='{}' and pid = '{}' and bill_id = '{}' ".format(table,c_id,p_id,bill_id)
        mycursor.execute(qry)
        pur_date = str(mycursor.fetchone()[0])
        print("| Your Purchase Date: ",pur_date)
        qry = "SELECT datediff(curdate(),pur_date) FROM PURCHASE where catagory = '{}' and c_id='{}' and pid = '{}' and bill_id = '{}' ".format(table,c_id,p_id,bill_id)
        mycursor.execute(qry)
        resno = mycursor.fetchone()[0]
        if resno <= 5 :
            print("| You are Eligible for Return !! ")
            inpp = input("| Press Y to Proceed Return Product: ")
            if inpp.lower() == 'y':
                qry = "select qut from purchase where catagory = '{}' and c_id = '{}' and pid = '{}' and bill_id = '{}' ".format(table,c_id,p_id,bill_id)
                mycursor.execute(qry)
                qty = mycursor.fetchone()[0]
                print("| Your Purchased Total Quantity is: ",qty)
                inqut = int(input("| Enter the Quantity of Return: "))
                if inqut < qty and inqut != 0:
                    qry = "select pur_id,price from purchase where catagory = '{}' and c_id = '{}' and pid = '{}' and bill_id = '{}' ".format(table,c_id,p_id,bill_id)
                    mycursor.execute(qry)
                    temprec = mycursor.fetchone()
                    pur_id = temprec[0]
                    price = temprec[1]
                    amount = inqut * price
                    qry = "update purchase set qut = qut - {}, amount = amount - {} where catagory = '{}' and c_id = '{}' and pid = '{}' and bill_id = '{}' ".format(inqut,amount,table,c_id,p_id,bill_id)
                    mycursor.execute(qry)
                    qry = "update bills set {}bill = {}bill - {} where c_id = '{}' and bill_id = '{}'".format(table,table,amount,c_id,bill_id)
                    mycursor.execute(qry)
                    qry = "update {} set stock = stock + {} where p_id = '{}'".format(table,inqut,p_id)
                    mycursor.execute(qry)
                    cur_date = str((datetime.datetime.now()).date())
                    qry = "insert into returned(pur_id,bill_id,c_id,pid,catagory,price,qut,amount,return_date) values('{}','{}','{}','{}','{}',{},{},{},'{}')".format(pur_id,bill_id,c_id,p_id,table.upper(),price,inqut,amount,cur_date)
                    mycursor.execute(qry)
                    mydb.commit()
                    print("| The Product Return Successfull !!")
                elif inqut == qty:
                    qry = "select * from purchase where catagory = '{}' and c_id = '{}' and pid = '{}' and bill_id = '{}' ".format(table,c_id,p_id,bill_id)
                    mycursor.execute(qry)
                    tempr = list(mycursor.fetchone())
                    qry = "select amount from purchase where catagory = '{}' and c_id = '{}' and pid = '{}' and bill_id = '{}' ".format(table,c_id,p_id,bill_id)
                    mycursor.execute(qry)
                    amount = mycursor.fetchone()[0]
                    qry = "update bills set {}bill = {}bill - {} where c_id = '{}' and bill_id = '{}'".format(table,table,amount,c_id,bill_id)
                    mycursor.execute(qry)
                    qry = "update {} set stock = stock + {} where p_id = '{}'".format(table,inqut,p_id)
                    mycursor.execute(qry)
                    tempr.pop()
                    cur_date = str((datetime.datetime.now()).date())
                    tempr.append(cur_date)
                    qry = "insert into returned values{}".format(tuple(tempr))
                    mycursor.execute(qry)
                    qry = "delete from purchase where catagory = '{}' and c_id = '{}' and pid = '{}' and bill_id = '{}' ".format(table,c_id,p_id,bill_id)
                    mycursor.execute(qry)
                    mydb.commit()
                    print("| The Product Return Successfull !!")
                else:
                    print("| Please Cross-Check your Quantity Entered...")
                    print("| Returning Aborted...")
        elif resno > 5:
            print("| Your Date of Purchase is Beyound 5 days")
        else:
            print("| Or Your Product Seem to Returned already")
    elif cnt == 0:
        print("| Wrong Details Provided...")
        print("| Return Aborted !!")
    elif cnt > 1:
        print("| Unable to Process Your Return Request !!")
        print("| It seems that many purchase have done to a Single Product. ")
        print("| So Your Return cannot be processed by the Program.")
        print("| To Proceed your return, contact our Admin !!")
        print("| Return Aborted !!")
    else:
        print("| Unexpected Problem Occured...")
        print("| Return Aborted !!")
    print("+------------------------------------------------------------------+")
    rand = input("Press Any Key to Continue...")
    clrscreen()
def stockorder():              #To Place Stock Order for No stock Items
    mycursor = mydb.cursor()
    tables = ['cosmetics','textile','electronics','stationary']
    for tbl in tables:
        tbl = tbl.capitalize()
        print("Checking Stock for {} Section...".format(tbl))
        qry = "select p_id from {} where stock <= 0".format(tbl)
        mycursor.execute(qry)
        res = mycursor.fetchall()
        if res == []:
            print("All Stocks are Fine in {} Section".format(tbl))
            print(end='\n\n')
            rand = input("Press Any Key to Continue...")
        else:
            for rec in res:
                for p_id in rec:
                    titles = get_titles(tbl)
                    now = datetime.datetime.now()
                    PurchaseID = "S" + str(now.year) + str(now.month) + str(now.day) + str(datetime.datetime.now().microsecond)
                    qry = "select * from {} where p_id = '{}'".format(tbl,p_id)
                    mycursor.execute(qry)
                    rtable = mycursor.fetchone()
                    print(tabulate([rtable],headers=get_titles(tbl),tablefmt='pretty'))
                    qut = input("Enter the Stock Quantity to Place Order: ")
                    qry = "insert into stock values('{}','{}','{}',{},'PENDING')".format(PurchaseID,p_id,tbl.upper(),qut)
                    mycursor.execute(qry)
                    print("Placing Stock Order for {} in the {} Section...".format(p_id,tbl))
                    print("Stock Order Successfull !!")
                    rand = input("Press Any Key to Continue...")
                    clrscreen()
def stkarri():                  #Updating the Arrival of Stock Order
    viewer('stock')
    print('\n',"Stock Updation","--------------",sep='\n')
    StockID = input('Enter Stock ID: ')
    qry = "select * from stock where s_id = '{}'".format(StockID)
    mycursor.execute(qry)
    rtbl = mycursor.fetchone()
    print(tabulate([rtbl],headers=get_titles('stock'),tablefmt='pretty'))
    proceed = input("Enter Y to Continue: ")
    if proceed.lower() == 'y':
        qry = "update stock set status = 'RECEIVED' where s_id = '{}'".format(StockID)
        mycursor.execute(qry)
        qry = "select p_id,catagory,qut from stock where s_id = '{}'".format(StockID)
        mycursor.execute(qry)
        r = mycursor.fetchone()
        p_id = r[0]
        catagory = r[1]
        qut = r[2]
        qry = "update {} set stock = {} where p_id = '{}'".format(catagory,qut,p_id)
        mycursor.execute(qry)
        print("Stock Successfully Added to {} Section !!".format(catagory))
    else:
        print("Updating Stock Order Arrival Aborted !!")
    rand = input("Press Any Key to Continue...")
def purchase_summary(table,id):
    nm = "{} PURCHASE SUMMARY".format(table.upper())
    leng = len(nm)
    print('-'*leng,nm,'-'*leng,sep='\n')
    qry = "select pid,price,qut,amount from purchase where catagory = '{}' and c_id = '{}' and bill_id = '{}'".format(table,c_id,bill_id)
    mycursor.execute(qry)
    prec = mycursor.fetchall()
    rrec = []
    tamt = 0
    if prec != []:
        for rec in prec:
            pid = rec[0]
            ramt = rec[3]
            tamt += ramt
            qry = "select name from {} where {} = '{}'".format(table,id,pid)
            mycursor.execute(qry)
            rname = mycursor.fetchone()[0]
            rec = list(rec)
            rec.insert(1,rname)
            rrec.append(rec)
        print(tabulate(rrec,headers=[id.upper(),'NAME','SINGULAR PRICE','QUANTITY','TOTAL AMOUNT'],tablefmt='pretty'))
        print("\nTotal Amount In this Section:",tamt,'\n')
    else:
        print("No Bill is generated through this Section !!")
    rand = input("Press Any Key to Continue...") 
    clrscreen()
def stores(table):
    while True:
        print("*"*65)
        nm = "{} STORE MENU".format(table.upper())
        leng = len(nm)
        print('-'*leng,nm,'-'*leng,sep='\n')
        print("1: View Available Products")
        print("2: Purchase any Product")
        print("3: Search for a Product")
        print("4: Return a Purchased Product")
        print("5: View Your Purchase in this Store")
        print("6: Exit")
        choi = int(input("Enter Choice: "))
        if choi == 1:
            viewer('{}'.format(table))
            rand = input("Press Any Key to Continue...")
            clrscreen()
        elif choi == 2:
            purchase('{}'.format(table),'p_id',False)
        elif choi == 3:
            searchfield('{}'.format(table))
        elif choi == 4:
            returnprdct('{}'.format(table),'p_id')
        elif choi == 5:
            purchase_summary('{}'.format(table),'p_id')
        elif choi == 6:
            print('Exiting {} Store...'.format(table.capitalize()))
            print("*"*65)
            rand = input("Press Any Key to Continue...")
            clrscreen()
            break
        else:
            print("Invalid Choice")
            print("Redirecting to Menu Again...")
            rand = input("Press Any Key to Continue...")
            clrscreen()
def create_session(c_id):
    print("--------------------","New Session Creation","--------------------",sep='\n')
    b_rand = int(random.random()*(10**9))
    bill_id = 'B'+str(b_rand)
    qry = "select bill_id from sessions"
    mycursor.execute(qry)
    bill_ids = [b[0] for b in mycursor.fetchall()]
    if bill_id in bill_ids:
        create_session()
    else:
        inp = input("Press Y to Initiate Session Creation: ")
        if inp.lower() == 'y':
            qry = "select max(serial_no) from sessions where c_id = '{}'".format(c_id)
            mycursor.execute(qry)
            mses = mycursor.fetchone()[0]
            date = (datetime.datetime.now()).date()
            qry = "insert into sessions values('{}','{}',{},'{}')".format(c_id,bill_id,mses+1,date)
            mycursor.execute(qry)
            qry = "insert into bills(c_id,bill_id,status) values('{}','{}','PENDING')".format(c_id,bill_id)
            mycursor.execute(qry)
            mydb.commit()
            print("One New Session Created for C_ID -> {} !!".format(c_id))
            return bill_id
        return None
def login(catagory):
    a_id, c_id, bill_id,e_id  = None, None, None, None
    if catagory.lower() == 'customer':
        print("+-----------------------------------------+")
        print("|            LOGIN OPERATION              |")
        print("+-----------------------------------------+")
        c_id = input("| Enter Customer ID: ")
        passwd = input("| Enter Password: ")
        qry = "select passwd from customer where c_id = '{}'".format(c_id)
        mycursor.execute(qry)
        rpass = mycursor.fetchone()
    if catagory.lower() == 'cashier':
        print("+-----------------------------------------+")
        print("|             CASHIER LOGIN               |")
        print("+-----------------------------------------+")
        e_id = input("| Enter Employee ID: ")
        passwd = input("| Enter Password: ")
        qry = "select passwd from cashier where e_id = '{}'".format(e_id)
        mycursor.execute(qry)
        rpass = mycursor.fetchone()
    elif catagory.lower() == 'admin':
        print("+-----------------------------------------+")
        print("|              ADMIN LOGIN                |")
        print("+-----------------------------------------+")
        a_id = input("| Enter Admin Id: ")
        passwd = input("| Enter Password: ")
        qry = "select passwd from admin where a_id = '{}'".format(a_id,passwd)
        mycursor.execute(qry)
        rpass = mycursor.fetchone()
    if rpass == None:
        print("| Wrong Id !!")
        print("| Login Failed...")
        print("+-----------------------------------------+")
        return None,None,None,None,None
    elif rpass[0] != passwd:
        print("| Wrong Password !!")
        print("| Login Failed...")
        print("+-----------------------------------------+")
        print("Redirecting to Main Menu...\n")
        return None,None,None,None,None
    elif rpass[0] == passwd and catagory.lower() in ('admin','cashier'):
        print("| Login Successful !!")
        print("+-----------------------------------------+")
        return True,c_id,a_id,None,e_id
    elif rpass[0] == passwd and catagory.lower() == 'customer':
        print("| Login Successful !!")
        print("+-----------------------------------------+")
        qry = "select count(serial_no) from sessions where c_id = '{}'".format(c_id)
        mycursor.execute(qry)
        nos = mycursor.fetchone()[0]
        if nos>1:
            qry = "select name from customer where c_id = '{}'".format(c_id)
            mycursor.execute(qry)
            print("+-------------------------------------------------------+")
            print("|                MALL MANAGEMENT PROGRAM                |")
            print("+-------------------------------------------------------+")
            print("| Welcome Again dear {} !!   ".format(mycursor.fetchone()[0]))
            print("| We Fount Multiple Sessions of your Login...           |")
            print("| Please Select your Session to Login !!                |")
            print("+-------------------------------------------------------+")
            print("Menu Options","------------",sep='\n')
            print("1: To Log on to any Avalable Sessions")
            print("2: To Create a New Session")
            print("3: Exit")
            lchoi = int(input("Enter Choice: "))
            if lchoi == 1:
                print("-------------","Session Login","-------------",sep='\n')
                qry = "select * from sessions where c_id = '{}'".format(c_id)
                mycursor.execute(qry)
                print(tabulate(mycursor.fetchall(),headers=get_titles('sessions'),tablefmt='pretty'))
                while True:
                            try:
                                print("Enter any Negative Number to Exit...")
                                s_no = int(input("Enter your Session Serial Number: "))
                                qry = "select bill_id from sessions where serial_no = {} and c_id = '{}'".format(s_no,c_id)
                                mycursor.execute(qry)
                                resulted = mycursor.fetchone()
                                if s_no<0:
                                    print("Your Exit Request Executed !!")
                                    break
                                elif resulted == None:
                                    print("Wrong Serial Number Provided...")
                                elif resulted != None:
                                    print("Logging on to Session {} is Successful !!".format(s_no))
                                    bill_id = resulted[0]
                                    return True,c_id,a_id,bill_id,e_id
                            except:
                                print("Unexpected Error Occured...")
                                print("Please Cross-Check the Serial Number Provided !!")
                                print("To exit the program, enter any negative number\n")
            elif lchoi == 2:
                bill_id = create_session(c_id)
                if bill_id == None:
                    print("Session Creation Aborted !!")
                    return False,c_id,a_id,bill_id,e_id
                print("Logged Onto the Created Session Successfully !!")
                return True,c_id,a_id,bill_id,e_id
            elif lchoi == 3:
                return False,c_id,a_id,bill_id,e_id
            else:
                print("Invalid Choice Given !!")
                print("Login Aborted...")
        elif nos == 1:
            qry = "select name from customer where c_id = '{}'".format(c_id)
            mycursor.execute(qry)
            print("+-------------------------------------------------------+")
            print("|                MALL MANAGEMENT PROGRAM                |")
            print("+-------------------------------------------------------+")
            print("| Welcome  {} !!   ".format(mycursor.fetchone()[0]))
            print("| You have only one Session of your Login...           |")
            print("+-------------------------------------------------------+")
            print("Menu Options","------------",sep='\n')
            print("1: To Log on to that Session which is Available")
            print("2: To Create a New Session")
            print("3: Exit")
            lchoi = int(input("Enter Choice: "))
            if lchoi == 1:
                qry = "select bill_id from sessions where c_id  = '{}'".format(c_id)
                mycursor.execute(qry)
                bill_id = mycursor.fetchone()[0]
                print("Current Session Loging In Successful !!")
                return True,c_id,a_id,bill_id,e_id
            elif lchoi == 2:
                create_session(c_id)
                if bill_id:
                    print("Session Creation Aborted !!")
                    return False,c_id,a_id,bill_id,e_id
                print("Logged Onto the Created Session Successfully !!")
                return True,c_id,a_id,bill_id,e_id
            elif lchoi == 3:
                return False,c_id,a_id,bill_id,e_id
            else:
                print("Invalid Choice Given !!")
                print("Login Aborted...")
        return None,None,None,None
    return None,None,None,None
def adminworks():
    def sectiondisplay(section):
        while True:
            nm = "{} SECTION MENU".format(section.upper())
            leng = len(nm)
            print('-'*leng,nm,'-'*leng,sep='\n')
            print("1: View Details")
            print("2: Add Product")
            print("3: Edit Details")
            print("4: Delete Details")
            print("5: Exit")
            operation = int(input("Enter Choice: "))
            if operation == 1:
                viewer('{}'.format(section))
            elif operation == 2:
                insertion('{}'.format(section))
            elif operation == 3:
                if section.lower() == "game":
                    edit('{}'.format(section),'g_id')
                else:
                    edit('{}'.format(section),'p_id')
            elif operation == 4:
                if section.lower() == "game":
                    delete('{}'.format(section),'g_id')
                else:
                    delete('{}'.format(section),'p_id')
            elif operation == 5:
                break
            else:
                print("Invalid Choice !!")
                print("Redirecting to Mend Again...")
                break
            rand = input("Press Any Key to Continue...")
            clrscreen()
    while True:
        print("*"*65)
        print("+-------------------------------------------------+")
        print("|                   ADMIN WORKS                   |")
        print("+-------------------------------------------------+")
        print("| 1: Admin Section")
        print("| 2: Cashier Section")
        print("| 3: Customer Section")
        print("| 4: Stock Section")
        print("| 5: Purchase Section")
        print("| 6: Bill Section")
        print("| 7: Textile Section")
        print("| 8: Movie Section")
        print("| 9: Food Section")
        print("| 10: Electronics Section")
        print("| 11: Cosmetics Section")
        print("| 12: Game Zone Section")
        print("| 13: Retruned Product Details")
        print("| 14: Exit")
        print("+-------------------------------------------------+")
        c = int(input("Enter Choice: "))
        print()
        if c == 1:
            while True:
                print('',"ADMIN SECTION OPERATIONS","------------------------",sep='\n')
                print("1: Add Another Admin")
                print("2: View Details Admins")
                print("3: Edit Details of an Admin")
                print("4: Delete Details of an Admin")
                print("5: Exit")
                operation = int(input("Enter Choice: "))
                if operation == 1:
                    print("+-----------------------------------------+")
                    print("|            ADMIN REGISTRATION           |")
                    print("+-----------------------------------------+")
                    aname = input("| Enter Admin Name: ")
                    aid = input("| Enter Admin Id: ")
                    print("-----------------","Password Creation","-----------------",sep='\n')
                    passwd1=input("| Create Password: ")
                    passwd2 = input("| Enter Password Again: ")
                    if passwd1 != passwd2:
                        print("| Password Does Not Match !!")
                        print("| Please Try Again...")
                    elif passwd1 == passwd2:
                        print("| Password Set Successfully !!")
                        qry = "insert into admin values('{}','{}','{}')".format(aname,aid,passwd1)
                        mycursor.execute(qry)
                        print("One Admin with Name",aname,"added Successfully !!")
                    else:
                        print("| Unexpected Problem Occured !!")
                    print("+-----------------------------------------+")
                elif operation == 2:
                    viewer('admin')
                elif operation == 3:
                    edit('admin','a_id')
                elif operation == 4:
                    delete('admin','a_id')
                elif operation == 5:
                    print("Exiting Admin Section !!")
                    print("Redirecting to Admin Works...")
                    break
                else:
                    print("Invalid Choice !!")
                    print("Redirecting to Menu Again...")
                rand = input("Press Any Key to Continue...")
                clrscreen()
        elif c == 2:
            while True:
                print("CASHIER SECTION OPERATIONS","---------------------------",sep='\n')
                print("1: View Data of All Cashiers")
                print("2: Hire a Casiher")
                print("3: Fire a Cashier")
                print("4: Edit Details of a Cashier")
                print("5: Exit")
                operation = int(input("Enter Choice: "))
                if operation == 1:
                    viewer('cashier')
                elif operation == 2:
                    insertion('cashier')
                elif operation == 3:
                    delete('cashier','e_id')
                elif operation == 4:
                    edit('cashier','e_id')
                elif operation == 5:
                    print("Exiting Cashier Section...")
                    break
                else:
                    print("Invalid Choice !!")
                    print("Redirecting to Cahier Section Menu...")
                    break
                rand = input("Press Any Key to Continue...") 
                clrscreen()
        elif c == 3:
            while True:
                print("CUSTOMER SECTION OPERATIONS","---------------------------",sep='\n')
                print("1: Add Cusomer")
                print("2: View Details Customers")
                print("3: Edit Details of a Customer")
                print("4: Delete Details of a Customer")
                print("5: Exit")
                operation = int(input("Enter Choice: "))
                if operation == 1:
                    addcustomer()
                elif operation == 2:
                    viewer('customer')
                    rand = input("Press Any Key to Continue...")
                    clrscreen()
                elif operation == 3:
                    edit('customer','c_id')
                elif operation == 4:
                    table = 'customer'
                    id = 'c_id'
                    print('','DELETION OPERATION','------------------',sep='\n')
                    pid = input("Enter the Reqired ID to be Deleted: ")
                    qry = "select * from {} where {} = '{}'".format(table,id,pid)
                    mycursor.execute(qry)
                    delrec = [mycursor.fetchone()]
                    titles = get_titles(table)
                    print(tabulate(delrec,headers=titles,tablefmt='pretty'))
                    print("The Above Customer Detail will be Deleted...")
                    choi = input("Are you sure to continue <Y/N>? ")
                    if choi in 'Yy':
                        qry = "delete from {} where {} = '{}'".format(table,id,pid)
                        mycursor.execute(qry)
                        qry = "delete from bills where c_id = '{}' and bill_id = '{}'".format(pid,bill_id)
                        mycursor.execute(qry)
                        mydb.commit()
                        print("One Customer Detail has been Successfully Deleted !!")
                    else:
                        print("Deletion Aborted !!")
                    rand = input("Press Any Key to Continue...")
                    clrscreen()
                elif operation == 5:
                    print("Exiting Customer Section !!")
                    print("Redirecting to Admin Works...")
                    rand = input("Press Any Key to Continue...")
                    clrscreen()
                    break
                else:
                    print("Invalid Choice !!")
                    print("Redirecting to Menu Again...")
                rand = input("Press Any Key to Continue...")
                clrscreen()
        elif c == 4:
            while True:
                print("STOCK SECTION OPERATIONS","------------------------",sep='\n')
                print("1: View Stock Orders")
                print("2: Place Stock Orders")
                print("3: Update Stock Order Arrival")
                print("4: Exit")
                operation = int(input("Enter Choice: "))
                if operation == 1:
                    viewer('stock')
                elif operation == 2:
                    stockorder()
                elif operation == 3:
                    stkarri()
                elif operation == 4:
                    print("Exiting Stock Section !!")
                    print("Redirecting to Admin Works...")
                    rand = input("Press Any Key to Continue...")
                    clrscreen()
                    break
                else:
                    print("Invalid Choice !!")
                    print("Redirecting to Menu Again...")
                    rand = input("Press Any Key to Continue...")
                    clrscreen()
        elif c == 5:
            while True:
                print("PURCHASE SECTION OPERATIONS","---------------------------",sep='\n')
                print("1: View Purchases Done")
                print("2: Delete a Purchase")
                print("3: Exit")
                operation = int(input("Enter Choice: "))
                if operation == 1:
                    viewer('purchase')
                elif operation == 2:
                    delete('purchase','pur_id')
                elif operation == 3:
                    print("Exiting Purchase Section !!")
                    print("Redirecting to Admin Works...")
                    break
                else:
                    print("Invalid Choice !!")
                    print("Redirecting to Menu Again...")
                rand = input("Press Any Key to Continue...")
                clrscreen()
        elif c == 6:
            while True:
                print("BILL SECTION OPERATIONS","------------------------",sep='\n')
                print("1: View Overall Bill Data")
                print("2: Exit")
                operation = int(input("Enter Choice: "))
                if operation == 1:
                    viewer('bills')
                elif operation == 2:
                    print("Exiting Bill Section !!")
                    print("Redirecting to Admin Works...")
                    break
                else:
                    print("Invalid Choice !!")
                    print("Redirecting to Menu Again...")
                rand = input("Press Any Key to Continue...")
                clrscreen()
        elif c == 7:
            sectiondisplay('Textile')
        elif c == 8:
            while True:
                print("MOVIE SECTION OPERATIONS","------------------------",sep='\n')
                print("1: View Available Movies")
                print("2: Add a Movie")
                print("3: Edit Details of a Movie")
                print("4: Delete Details of a Movie")
                print("5: Cancel Movie for a Customer")
                print("6: Exit")
                operation = int(input("Enter Choice: "))
                if operation == 1:
                    viewer('movie')
                elif operation == 2:
                    insertion('movie')
                elif operation == 3:
                    edit('movie','m_id')
                elif operation == 4:
                    delete('movie','m_id')
                elif operation == 5:
                    print('',"Movie Cancellation","------------------",sep ='\n')
                    c_id = input("Enter C_ID: ")
                    bill_id = input("Enter BILL_ID: ")
                    m_id = input("Enter Movie ID: ")
                    quty = int(input("Enter Cancellation Quantity: "))
                    qry = "select pid,qut from purchase where catagory = 'movie' and  c_id = '{}' and pid='{}' and bill_id = '{}'".format(c_id,m_id,bill_id)
                    mycursor.execute(qry)
                    recds = mycursor.fetchone()
                    qut = recds[1] - quty
                    if qut >= 0:
                        qry = "update purchase set qut = {} where CATAGORY = 'movie' and c_id = '{}' and pid = '{}' and bill_id = '{}'".format(qut,c_id,m_id,bill_id)
                        mycursor.execute(qry)
                        qry = "update purchase set amount = price * qut where CATAGORY = 'movie' and c_id = '{}' and pid = '{}' and bill_id = '{}'".format(c_id,m_id,bill_id)
                        mycursor.execute(qry)
                        qry = "select price from movie where m_id = '{}'".format(m_id)
                        mycursor.execute(qry)
                        recs = mycursor.fetchone()
                        price = recs[0]
                        famt = price * qut
                        qry = "select moviebill from bills where c_id ='{}' and bill_id = '{}'".format(c_id,bill_id)
                        mycursor.execute(qry)
                        bamt = mycursor.fetchone()
                        print("+--------------------------------------------+")
                        print('|            CANCELLATION DETAILS            |')
                        print("+--------------------------------------------+")
                        print("| The Billed amount before Cancellation:",bamt[0])
                        print("| Amount that should be reduced        :",quty*price)
                        print("| The Final Amount is                  :",bamt[0]-(quty*price))
                        print("+--------------------------------------------+")
                        qry = "update bills set moviebill = moviebill - {} where c_id ='{}'".format(quty*price,c_id)
                        mycursor.execute(qry)
                        print("Cancellation Completed Successfully !!")
                    elif qut < 0:
                        print("Invalid Operation...")
                        print("Please Check your Cancelling Quantity...")
                    qry = 'delete from purchase where qut=0 and amount=0'
                    mycursor.execute(qry)
                    mydb.commit()
                    rand = input("Press Any Key to Continue...")
                    clrscreen()

                elif operation == 6:
                    print("Exiting Movie Section !!")
                    print("Redirecting to Admin Works...")
                    break
                else:
                    print("Invalid Choice !!")
                    print("Redirecting to Menu Again...")
                rand = input("Press Any Key to Continue...")
                clrscreen()
        elif c == 9:
            while True:
                print("FOOD SECTION OPERATIONS","------------------------",sep='\n')
                print("1: View All Dishes")
                print("2: Add a Dish")
                print("3: Edit Details of a Dish")
                print("4: Delete Details of a Dish")
                print("5: Exit")
                operation = int(input("Enter Choice: "))
                if operation == 1:
                    viewer('food')
                elif operation == 2:
                    insertion('food')
                elif operation == 3:
                    edit('food','d_id')
                    print("1 Dish details modified Successfully !!")
                elif operation == 4:
                    delete('food','d_id')
                elif operation == 5:
                    print("Exiting Food Section !!")
                    print("Redirecting to Admin Works...")
                    break
                else:
                    print("Invalid Choice !!")
                    print("Redirecting to Menu Again...")
                rand = input("Press Any Key to Continue...")
                clrscreen()

        elif c == 10:
            sectiondisplay('Electronics')
        elif c == 11:
            sectiondisplay('Cosmetics')
        elif c == 12:
            sectiondisplay('game')
        elif c == 13:
             while True:
                print("RETURNED PRODUCT DETAILS","------------------------",sep='\n')
                print("1: View Returned Products")
                print("2: Delete a Returned Product Detail")
                print("3: Exit")
                operation = int(input("Enter Choice: "))
                if operation == 1:
                    viewer('returned')
                elif operation == 2:
                    delete('returned','pur_id')
                elif operation == 3:
                    print("Exiting Purchase Section !!")
                    print("Redirecting to Admin Works...")
                    break
                else:
                    print("Invalid Choice !!")
                    print("Redirecting to Menu Again...")
                rand = input("Press Any Key to Continue...")
                clrscreen()
        elif c == 14:
            print("Exiting Admin Works...")
            break
        else:
            print("Invalid Choice !!")
            print("Redirecting to Menu Again...")
def cashierworks():
    while True:
        print("*"*65)
        print("+-------------------------------------------------+")
        print("|                 CASHIER WORKS                   |")
        print("+-------------------------------------------------+")
        print("| 1: Close Bill of a Customer                     |")
        print("| 2: Exit                                         |")
        print("+-------------------------------------------------+")
        cchoi = int(input("Enter Choice: "))
        if cchoi == 1:
            print("---------------------","CUSTOMER BILL CLOSING","---------------------",sep='\n')
            c_id = input("Enter C_ID: ")
            bill_id = input("Enter BILL_ID: ")
            qry = "select * from bills where c_id = '{}' and bill_id = '{}'".format(c_id,bill_id)
            mycursor.execute(qry)
            brec = mycursor.fetchall()
            if brec != []:
                print(tabulate(brec,headers=get_titles('bills'),tablefmt='pretty'))
                amount = sum(brec[0][2:10])
                gamt = None
                while brec[0][-1].lower() == 'pending':
                    print("Total Amount that Should be Paid:",amount)
                    print("Enter Negative Values to Cancel...")
                    if gamt == None:
                        gamt = int(input("Enter the Given Amount: "))
                    if gamt < 0:
                        print("Bill Closing Cancelled !!")
                        break
                    elif gamt < amount:
                        print("\n\nMoney Received is Less than the Original Amount !!")
                        while gamt<amount:
                            print("Money Difference:",amount-gamt)
                            got = int(input("Enter the Balance Given Again: "))
                            gamt += got
                    elif gamt == amount:
                        qry = "update bills set status = 'PAID' where c_id = '{}' and bill_id = '{}'".format(c_id,bill_id)
                        mycursor.execute(qry)
                        mydb.commit()
                        print("Bill Closed Successfully !!")
                        break
                    elif gamt > amount:
                        while True:
                            diff = gamt - amount
                            print("Return Amount:",diff)
                            ret = input("Press Y to Confirm that Amount Returned: ")
                            if ret.lower() == 'y':
                                qry = "update bills set status = 'PAID' where c_id = '{}' and bill_id = '{}'".format(c_id,bill_id)
                                mycursor.execute(qry)
                                mydb.commit()
                                print("Bill Closed Successfully !!")
                                break
                            elif ret.lower() == 'n':
                                print("Bill Closing Cancelled !!")
                                break
                            else:
                                print("Please Return the Balance Amount To Continue !!")
                                print("Press N to Cancel Bill Closing...")
                        break
                else:
                    print("Bill Already Closed !!")
            else:
                print("Wrong Details Entered !!")
        elif cchoi == 2:
            print("Exiting Cashier Works...")
            break
        else:
            print("Invalid Choice !!")
        rand = input("Press Any Key to Continue...") 
        clrscreen()
try:
    if database_check():
        mydb = mysql.connector.connect(host = 'localhost',user='Kishore',passwd='Kishore@2008',database='mall_management')
        if mydb.is_connected:
            print("\t\tCONNECTIVITY SUCCESSFULLY ESTABLISHED")
            mycursor = mydb.cursor()
            print("*"*65)
            print('*'*21,'Welcome to Mega Mall','*'*22)
            print("*"*65)
            qry = "show tables"
            mycursor.execute(qry)
            tbls = mycursor.fetchall()
            f = False
            for tbl in tbls:
                if tbl[0].lower() == 'admin':
                    f = True
            while not f:
                print("WELCOME TO NEW ADMIN !!")
                print("+-----------------------------------------+")
                print("|            ADMIN REGISTRATION           |")
                print("+-----------------------------------------+")
                aname = input("| Enter Admin Name: ").upper()
                aid = input("| Enter Admin Id: ").upper()
                print("| Password Creation","| -----------------",sep='\n')
                passwd1=input("| Create Password: ")
                passwd2 = input("| Enter Password Again: ")
                if passwd1 != passwd2:
                    print("| ","| Password Does Not Match !!",sep='\n')
                    print("| Please Try Again...")
                elif passwd1 == passwd2:
                    qry = "create table ADMIN(NAME VARCHAR(20),A_ID VARCHAR(8),PASSWD VARCHAR(20))"
                    mycursor.execute(qry)
                    qry = "insert into admin values('{}','{}','{}')".format(aname,aid,passwd1)
                    mycursor.execute(qry)
                    print("| Password Set Successfully !!")
                    print("| Admin Details Added Successfully !!")
                    f = True
                else:
                    print("| Unexpected Problem Occured !!")
                print("+-----------------------------------------+")
                rand = input("Press Any Key to Continue...")
                clrscreen()
            while f:
                print("+---------------------------------------------+")
                print("|                Main Menu                    |")
                print("+---------------------------------------------+")
                print("| 1. Signup (For New Customer)                |")
                print("| 2. Login  (For Existing Customer)           |")
                print("| 3. Admin Login                              |")
                print("| 4. Cashier Login                            |")
                print("| 5. Exit                                     |")
                print("+---------------------------------------------+")
                c = int(input("Enter Choice: "))
                clrscreen()
                if c == 1:
                    addcustomer()
                elif c == 2:
                    result = login('customer')
                    rand = input("Press Any Key to Continue...")
                    clrscreen()
                    c_id = result[1]
                    bill_id = result[3]
                    while result[0]:
                        print("--------------","Mall Main Menu","--------------",sep='\n')
                        print("1: Textile")
                        print("2: Movie Theatre")
                        print("3: Food Court")
                        print("4: Game Zone")
                        print("5: Electronics Store")
                        print("6: Stationary Store")
                        print("7: Cosmetic Store")
                        print("8: Total Bill")
                        print("9: Exit")
                        ch = int(input("Enter your choice: "))
                        if ch == 1:
                            stores('textile')
                        elif ch == 2:
                            while True:
                                print("*"*65)
                                print('-----------------',"MOVIE THEATRE MENU",'-----------------',sep='\n')
                                print("1: To View the Available Movies")
                                print("2: To Book a Movie")
                                print("3: Snacks")
                                print("4: To View All the Booked Movies")
                                print("5: To Cancell a Booked Movie")
                                print("6: To Exit")
                                cho = int(input("Enter Choice: "))
                                if cho == 1:
                                    viewer('movie')
                                    rand = input("Press Any Key to Continue...")
                                    clrscreen()
                                elif cho == 2:
                                    purchase('movie','m_id',False)
                                elif cho == 3:
                                    qry = "select count(*) from purchase where catagory = 'movie' and c_id ='{}' and bill_id = '{}'".format(c_id,bill_id)
                                    mycursor.execute(qry)
                                    mnos = mycursor.fetchone()[0]
                                    if mnos >= 1:
                                        while True:
                                            print("\tSnacks")
                                            print("\t------")
                                            print("1: View Available Snacks")
                                            print("2: Purchase a Snack")
                                            print("3: Exit")
                                            schoi = int(input("Enter Choice: "))
                                            if schoi == 1:
                                                viewer('snacks')
                                            elif schoi == 2:
                                                purchase('snacks','s_id',False)
                                            elif schoi == 3:
                                                print("Exiting Snacks Section...")
                                                break
                                            else:
                                                print("Invalid Choice !!")
                                                print("Redirecting to Snacks Menu...")
                                    else:
                                        print("To Enter into Snack Section, at least one Movie should be Booked...")
                                        print("Snack Section Entry Failed !!")
                                    rand = input("Press Any Key to Continue...")
                                    clrscreen()
                                    print("*"*65)
                                elif cho == 4:
                                    purchase_summary('movie','m_id')
                                elif cho == 5:
                                    print("Movie Cancellation Cannot be Processed Directly.")
                                    print("Please Contact Admin to Preceed your Movie Cancellation...")
                                    rand = input("Press Any Key to Continue...") 
                                    clrscreen()
                                elif cho == 6:
                                    print('Exiting Movie Theatre...')
                                    print('*'*65)
                                    break
                                else:
                                    print("Invalid Choice")
                                    print("Redirecting to Menu Again...")
                                    rand = input("Press Any Key to Continue...")
                                    clrscreen()
                        elif ch == 3:
                            while True:
                                print("*"*65)
                                print('---------------',"FOOD COURT MENU",'---------------',sep='\n')
                                print("1: To View Available Dishes")
                                print("2: To Order Item")
                                print("3: To Search a Dish")
                                print("4: To View All the Dishes Purchased")
                                print("5: To Exit")
                                cho = int(input("Enter Choice: "))
                                if cho == 1:
                                    dtype = input("Fiter by <Veg/Non-Veg/Both>?? ")
                                    if dtype.lower() == 'veg':
                                        qry = "select * from food where d_id like 'v%'"
                                    elif dtype.lower() in ('nonveg','non-veg'):
                                        qry = "select * from food where d_id like 'nv%'"
                                    elif dtype.lower() == 'both':
                                        qry = "select * from food"
                                    else:
                                        print("Invalid Choice! Redrirecting to Main Menu...")
                                        print('*'*65)
                                        break
                                    mycursor.execute(qry)
                                    dres = mycursor.fetchall()
                                    print(tabulate(dres,headers=get_titles('food'),tablefmt='pretty'))
                                    rand = input("Press Any Key to Continue...")
                                    clrscreen()
                                elif cho == 2:
                                    purchase('food','d_id',False)
                                elif cho == 3:
                                    searchfield('food')
                                elif cho == 4:
                                    purchase_summary('food','d_id')
                                elif cho == 5:
                                    print('Exiting Food Court...')
                                    print("*"*65)
                                    break
                                else:
                                    print("Invalid Choice")
                                    print("Redirecting to Menu Again...")
                                    rand = input("Press Any Key to Continue...")
                                    clrscreen()
                        elif ch == 4:
                            while True:
                                print("*"*65)
                                print('---------------',"GAME ZONE MENU",'---------------',sep='\n')
                                print("1: View Available Games")
                                print("2: Book a Game")
                                print("3: View All the Games Played")
                                print("4: Exit")
                                choice = int(input("Enter Choice: "))
                                if choice == 1:
                                    viewer('game')
                                    rand = input("Press Any Key to Continue...")
                                    clrscreen()
                                elif choice == 2:
                                    purchase('game','g_id',False)
                                    mydb.commit()
                                    print("*"*65)
                                elif choice == 3:
                                    purchase_summary('game','g_id')
                                elif choice == 4: 
                                    print('Exiting Game Court...')
                                    rand = input("Press Any Key to Continue...")
                                    clrscreen()
                                    break
                                else:
                                    print("Invalid Choice, Please check the Option you choosed !!")
                                    rand = input("Press Any Key to Continue...")
                                    clrscreen()
                                    continue
                        elif ch == 5:
                            stores('electronics')
                        elif ch == 6:
                            stores('stationary')
                        elif ch == 7:
                            stores('cosmetics')
                        elif ch == 8:
                            print("*"*65)
                            qry1 = "select textilebill,foodbill,moviebill,gme_bill,electronicsbill,stationarybill,cosmeticsbill,gamebill from bills where c_id = '{}' and bill_id = '{}'".format(c_id,bill_id)
                            mycursor.execute(qry1)
                            recs = mycursor.fetchone()
                            amt = 0
                            qry = "select name from customer where c_id = '{}'".format(c_id)
                            mycursor.execute(qry)
                            res = mycursor.fetchone()
                            for bil in recs:
                                if bil != None:
                                    amt = amt + bil
                            qry = "select serial_no,date_of_issue from sessions where c_id = '{}' and bill_id = '{}'".format(c_id,bill_id)
                            mycursor.execute(qry)
                            sres = mycursor.fetchall()
                            print('+---------------------------------+')
                            print("|     Mega Mall Total Bill        |")
                            print('+---------------------------------+')
                            print("| Customer Name    : ",res[0])
                            print("| Session Number   : ",sres[0][0])
                            print("| Session Issued On: ",str(sres[0][1]))
                            print("| Textile Bill     : ",recs[0])
                            print("| Food Court Bill  : ",recs[1])
                            print("| Movie Bill       : ",recs[2])
                            print("| Game Court Bill  : ",recs[3])
                            print("| Electronics Bill : ",recs[4])
                            print("| Stationary Bill  : ",recs[5])
                            print("| Cosmetics  Bill  : ",recs[6])
                            print("| Game Zone Bill   : ",recs[7])
                            print('+------------------+--------------+')
                            print("|   Grand Total    : ",amt,)
                            print('+------------------+--------------+')
                            qry = "select status from bills where c_id = '{}' and bill_id = '{}'".format(c_id,bill_id)
                            mycursor.execute(qry)
                            resrec = mycursor.fetchone()
                            rand = input("Press Any Key to Continue...")
                            clrscreen()
                            print("*"*65)
                        elif ch == 9:
                            print("Checking your Bill Payment Status...")
                            print("Your Bill Payment Status: ",end='')
                            qry = "select status from bills where c_id = '{}' and bill_id = '{}'".format(c_id,bill_id)
                            mycursor.execute(qry)
                            estatus = mycursor.fetchone()[0]
                            if estatus.upper() == 'PENDING':
                                qry1 = "select textilebill,foodbill,moviebill,gme_bill,electronicsbill,stationarybill,cosmeticsbill,gamebill from bills where c_id = '{}' and bill_id = '{}'".format(c_id,bill_id)
                                mycursor.execute(qry1)
                                recs = mycursor.fetchone()
                                amt = 0
                                qry = "select name from customer where c_id = '{}'".format(c_id)
                                mycursor.execute(qry)
                                res = mycursor.fetchone()
                                for bil in recs:
                                    if bil != None:
                                        amt = amt + bil
                                if amt == 0:
                                    print("NOT REQUIRED (No Purchase have made)")
                                    rand = input("Press Any Key to Continue...") 
                                    clrscreen()
                                    break
                                else:
                                    print("NOT PAID (Pending)")
                                    print("Please Pay your Bill to Exit !!")
                                    rand = input("Press Any Key to Continue...") 
                                    clrscreen()
                            else:
                                print("DONE")
                                print("Processing Your Exit Request...")
                                print("*"*65)
                                rand = input("Press Any Key to Continue...") 
                                clrscreen()
                                break
                        else:
                            print('Invalid Choice Entered !!')
                            print('Redirecting to Menu Again...')   
                            rand = input("Press Any Key to Continue...") 
                            clrscreen()
                elif c == 3:
                    result = login('admin')
                    a_id = result[2]
                    if result[0]:
                        adminworks()
                elif c == 4:
                    result = login('cashier')
                    e_id = result[-1]
                    if result[0]:
                        cashierworks()
                elif c == 5:
                    print('\n','Thanks for Visiting MEGA MALL and Visit Again !!',sep='')
                    print('Exiting Mega Mall...\n\n\n\n\n')
                    print("+----------------------------------------------+")
                    print("| This Project is Done By |                    |")
                    print("| -------------------------                    |")
                    print("| Name        : Aakash Raj S                   |")
                    print("| Grade       : 12 CBSE                        |")
                    print("| Institution : SRV Public School, Samayapuram |")
                    print("+----------------------------------------------+")
                    break  
        else:
            print('Please Check your Connection and Try Again !!')
except Exception as error:
    print("\n\n\n\n\nError Occured: ",error)
    print("Exiting The Program !!")
