import sqlite3
from datetime import datetime

def viewDB():
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    query = """
    SELECT name from sqlite_master WHERE type='table';
    """
    c.execute(query)
    tables =  c.fetchall()
    print(f"""here are all the tables in GoBusBus.db  :""")
    for table in tables:
        print(table[0])
    print()
    conn.close()

def viewTable(table):
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    query = f"""
    SELECT rowid,* FROM {table};
    """
    print(f"table {table}")
    c.execute(query)
    rows = c.fetchall()
    for row  in rows:
        print(row)
    print()
    conn.commit()
    conn.close()

def createTable(table,columns):
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    columns= ', '.join(columns)
    query = f"""
    CREATE TABLE IF NOT EXISTS {table} ({columns});
    """
    c.execute(query)
    print(f"table {table} created successfully")
    conn.commit()
    conn.close()

def dropTable(table):
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    query = f"""
    DROP TABLE IF EXISTS {table};
    """
    c.execute(query)
    print(f"table {table} has been deleted..")
    conn.commit()
    conn.close()

def insertVal(table,data):
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    data = ','.join(f"'{_}'" for _ in data)
    query = f"""
    INSERT INTO {table} 
    VALUES ({data});
    """
    c.execute(query)
    print(f"data inserted in table {table}")
    conn.commit()
    conn.close()



def getWeekday(date):
    date_format = "%d-%m-%Y"
    date_obj = datetime.strptime(date, date_format)
    day_name = date_obj.strftime('%A')
    return day_name

def getCityID(name):
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    query = f"""
    SELECT ID from City WHERE Name = '{name}';
    """
    c.execute(query)
    id = c.fetchone()[0]
    conn.commit()
    conn.close()
    return id

def getOperator(busID):
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    opID = busID[0]
    query = f"""
    SELECT Name, PhoneNumber from Operator WHERE ID = '{opID}';
    """
    c.execute(query)
    operator = c.fetchone()
    conn.commit()
    conn.close()
    return operator


def checkSeatAvailability(date, busID, srcID, destID):
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    query = f"""
    SELECT BoardPoint, DropPoint
    FROM BookingLog
    WHERE Date = '{date}' AND BusID = '{busID}'  
    """
    c.execute(query)
    bookings = c.fetchall()
    print(bookings)
    query = f"""
    SELECT RouteID 
    FROM BusDetails
    WHERE ID = '{busID}'
    """
    c.execute(query)
    routeID = c.fetchone()[0]
    print(routeID)
    
    n = len(routeID)
    arr = [0]*(n+1)
    ind = {}
    for i in range(n):
        ind[routeID[i]] = i;
    for s,d in bookings:
        arr[ind[s]] += 1;
        arr[ind[d]+1] -= 1;
    for i in range(1,n+1):
        arr[i] += arr[i-1]
    mx = 0
    for i in range(ind[srcID], ind[destID]+1):
        mx = max(mx,arr[i])
    if(mx==42):
        return 0
    else:
        return 1

def fillBookingLog(date, busID, boardPoint, dropPoint ):
    insertVal('BookingLog', (date, busID, boardPoint, dropPoint))

def fillPassengerDetails(ticketID, name, age, sex, phoneNumber):
    insertVal('PassengerDetails', (ticketID, name, age, sex, phoneNumber))

def findBusDetails(date, src, dest):
    srcID = getCityID(src)
    destID = getCityID(dest)
    weekday = getWeekday(date)
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    query = f"""
    SELECT ID
    FROM BusDetails
    WHERE BusDetails.RouteID IN (
        SELECT RouteID
        FROM RouteDetails
        WHERE {srcID} != 0 AND {destID} != 0 AND {srcID} < {destID}
    ) AND {weekday} = 1;
    """
    c.execute(query)
    busList = c.fetchall()
    busDetails = []
    for bus in busList:
        flag = checkSeatAvailability(date, bus[0], srcID, destID)
        busDetails.append((bus[0], getOperator(bus[0]), flag))
    return busDetails
    conn.commit()
    conn.close()

def rando():
    conn = sqlite3.connect('GoBusBus.db')
    c = conn.cursor()
    query = """
    SELECT SUM(":X:") from 'RouteDetails';
    """
    c.execute(query)
    res = c.fetchone()[0]
    print(f"heres the sum, {res}")
    conn.commit()
    conn.close()