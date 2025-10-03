import sys
from antigravity import geohash

if __name__ == '__main__':
    if len(sys.argv) == 4:
        date_bytes = sys.argv[3]
        dow_jones = "30218.26"
        date = date_bytes + dow_jones
        b_date = date.encode('utf-8')
        if int(sys.argv[1]) > 90 or int(sys.argv[1]) < -90:
            print("Latitude must be between -90 and 90")
            sys.exit(1)
        elif int(sys.argv[2]) > 180 or int(sys.argv[2]) < -180:
            print("Longitude must be between -180 and 180")
        else:
            geohash(int(sys.argv[1]), int(sys.argv[2]), b_date)
    else:
        print("Usage: python3 geohashing.py <latitude> <longitude> <date>")