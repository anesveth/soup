#!/usr/bin/env python3
import sys
import phase1,phase2,phase3,phase4

def myname():
    '''prints out my name'''
    return ("""\n<Sharon Anesveth Alvarado Maatens>""")

def main():
    choice=(sys.argv)
    try:
        if choice[1]=="1":
            print(myname())
            phase1.portal()
        elif choice[1]=="2":
            print(myname())
            phase2.estudios()
        elif choice[1]=="3":
            print(myname())
            phase3.cs()
        elif choice[1]=="4"or " 4" or "4 ":
            print(myname())
            phase4.directorio()
        print("se ejecuto correctamente")
    except:
        print("se escogio todo")
        print(myname())
        phase1.portal()
        phase2.estudios()
        phase3.cs()
        phase4.directorio()

main()