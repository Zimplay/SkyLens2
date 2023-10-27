from scipy import *
from math import *
from sqlite3 import *

connection = connect('testDB2.db')
curs = connection.cursor()
def input_d(tec_id):
    global L1, L2, B1, B2, exentz, malpolz, bolpolz, roz1, x1, y1, z1, roz2, x2, y2, z2, ras1, az1, zen1, ras2, az2, zen2
#    a=float(input())
#    e=float(input())
#    E=float(input())
#    B = float(input())
#    L = float(input())
    curs.execute('SELECT B1 FROM Orders WHERE id = '+str(tec_id))
    B1 = int(curs.fetchall()[0][0])
    curs.execute('SELECT B2 FROM Orders WHERE id = '+str(tec_id))
    B2 = int(curs.fetchall()[0][0])
    curs.execute('SELECT L1 FROM Orders WHERE id = '+str(tec_id))
    L1 = int(curs.fetchall()[0][0])
    curs.execute('SELECT L2 FROM Orders WHERE id = '+str(tec_id))
    L2 = int(curs.fetchall()[0][0])
    malpolz = 6356.777
    bolpolz = 6378.160
    exentz = 0.0167
    roz1 = malpolz/(1-exentz**2*sin(B1)**2)
    x1 = roz1*cos(B1)*cos(L1)
    y1 = roz1*cos(B1)*sin(L1)
    z1 = (bolpolz**2/malpolz**2)*roz1*sin(B1)
    roz2 = malpolz/(1-exentz**2*sin(B2)**2)
    x2 = roz2*cos(B2)*cos(L2)
    y2 = roz2*cos(B2)*sin(L2)
    z2 = (bolpolz**2/malpolz**2)*roz2*sin(B2)
    ras1 = (x1 ** 2 + y1 ** 2 + z1 ** 2) ** 0.5
    ras2 = (x2 ** 2 + y2 ** 2 + z2 ** 2) ** 0.5
    az1 = atan(y1 / x1)
    az2 = atan(y2 / x2)
    zen1 = atan((x1 ** 2 + y1 ** 2) ** 0.5 / z1)
    zen2 = atan((x2 ** 2 + y2 ** 2) ** 0.5 / z2)
if __name__ == '__main__' :
    input_d(1)
 #   M = E - e * sin(e)
    print(x1,y1,z1,x2,y2,z2)