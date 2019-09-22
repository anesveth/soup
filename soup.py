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
            print(phase1.portal())
        if choice[1]=="2":
            print(myname())
            phase2.estudios()
        if choice[1]=="3":
            print(myname())
            phase3.cs()
        if choice[1]=="4":
            print(myname())
            phase4.directorio()
    except:
        print(myname())
        print(phase1.portal())
        print(phase2.estudios())
        print(phase3.cs())
        print(phase4.directorio())

main()