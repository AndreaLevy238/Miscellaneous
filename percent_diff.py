import math

def avg(v1, v2):
    return (v1 + v2)/2

def difference(v1, v2):
    return math.fabs(v1 - v2)/ avg(v1,v2)

def main():
    e_val = float(raw_input("Experimen0tal value:"))
    t_val = float(raw_input("Theoretical value:"))
    print 100 * difference(t_val, e_val)



if __name__ == '__main__':
    main()