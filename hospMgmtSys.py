import os
import csv

def newPatient():
    print("Add a new Patient Record")
    print("=========================")
    f=open('Patient.csv','a',newline='\r\n')
    s=csv.writer(f)

    Patientid=input('Enter Patient id : ')
    Patientname=input('Enter Patient name : ')
    Disease=input('Enter Disease : ')
    fee=float(input('Enter Fee : '))
    Doctorname=input('Enter name of Doctor : ')
    print("----------------------------------------------------")
    rec=[Patientid,Patientname,Disease,fee,Doctorname]
    s.writerow(rec)
    f.close()
    print("Patient Record Saved")
    input("Press any key to continue..")
    print("=====================================================================")

def editPatient():
    print("Modify a Patient Record")
    print("=========================")
    f=open('Patient.csv','r',newline='\r\n') 
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter Patientid whose record you want to modify : ')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("-------------------------------")
            print("Patient id :",rec[0])
            print("Patient Name :",rec[1])
            print("Disease :",rec[2])
            print("Fee :",rec[3])
            print("Name of Doctor :",rec[4])
            print("-------------------------------")
            
            choice=input("Do you want to modify this Patient Record?(y/n) : ")
            if choice=='y' or choice=='Y':
                print("----------------------------------------------------")
                
                askQ1=input('Do you want to change Patient id?(y/n) : ')
                if askQ1=='y' or askQ1=='Y':
                    Patientid=input('Enter new Patient id : ')
                else:
                    Patientid=rec[0]
                
                askQ2=input('Do you want to change Patient name?(y/n): ')
                if askQ2=='y' or askQ2=='Y':
                    Patientname=input('Enter new Patient name : ')
                else:
                    Patientname=rec[1]
                
                askQ3=input('Do you want to change disease name?(y/n) : ')
                if askQ3=='y' or askQ3=='Y':
                    Disease=input('Enter Disease : ')
                else:
                    Disease=rec[2]
                
                askQ4=input('Do you want to change the fee?(y/n) : ')
                if askQ4=='y' or askQ4=='Y':
                    fee=float(input('Enter Fee : '))
                else:
                    fee=rec[3]
                
                askQ4=input('Do you want to change the name of the doctor? (y/n) : ')
                if askQ3=='y' or askQ3=='Y':
                    Doctorname=input('Enter name of Doctor : ')
                else:
                    Doctorname=rec[4]
                    
                print("----------------------------------------------------")
                rec=[Patientid,Patientname,Disease,fee,Doctorname]
                s1.writerow(rec)
                print("Patient Record Modified")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()   
    f1.close()
    os.remove("Patient.csv")
    os.rename("temp.csv","Patient.csv")
    
    input("Press any key to continue..")
    print("=====================================================================")

def delPatient():
    f=open('Patient.csv','r',newline='\r\n') 
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter Patientid whose record you want to delete : ')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("-------------------------------")
            print("Patient id :",rec[0])
            print("Patient Name :",rec[1])
            print("Disease :",rec[2])
            print("Fee :",rec[3])
            print("Name of Doctor :",rec[4])
            print("-------------------------------")
            choice=input("Do you want to delete this Patient Record? (y/n) : ")
            print("-------------------------------")
            if choice=='y' or choice=='Y':
                pass
                print("Patient Record Deleted....")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("Patient.csv")
    os.rename("temp.csv","Patient.csv")
    
    input("Press any key to continue..")
    print("=====================================================================")

def searchPatient():
    print("Search for a Patient Record")
    print("=====================")
    f=open('Patient.csv','r',newline='\r\n')  
    r=input('Enter Patientid you want to search : ')
    s=csv.reader(f)
    for rec in s:
        if rec[0]==r:
            print("-------------------------------")
            print("Patient id :",rec[0])
            print("Patient Name :",rec[1])
            print("Disease :",rec[2])
            print("Fee :",rec[3])
            print("Name of Doctor :",rec[4])
            print("-------------------------------")
    f.close()
    input("Press any key to continue..")
    print("=====================================================================")

def listofPatients():
    print("=====================================================================")
    print("                 List of All Patients")
    print("=====================================================================")
    f=open('Patient.csv','r',newline='\r\n')  
    s=csv.reader(f)
    i=1
    for rec in s:
        print(rec[0],end="\t\t")
        print(rec[1],end="\t\t")
        print(rec[2],end="\t\t")
        print(rec[3],end="\t\t")
        print(rec[4])
        i+=1
    f.close()
    print("----------------------------------------------------------------------")
    input("Press any key to continue..")
    print("=====================================================================")

def menu():
    choice=0
    while choice!=6:
        print("\n")
        print("|----------------------------|")
        print("| Hospital Management System |")
        print("|============================|")
        print("|            Menu            |")
        print("|----------------------------|")
        print("\n")
        print("1. Add a new Patient Record")
        print("2. Modify an Existing Patient")
        print("3. Delete Existing Patient")
        print("4. Search for a Patient")
        print("5. List all the Patients")
        print("6. Exit")
        print("-------------------------------")
        choice=int(input('Enter your choice -> '))
        print("-------------------------------")
        print("\n")
        if choice==1:
            newPatient()
        elif choice==2:
            editPatient()
        elif choice==3:
            delPatient()
        elif choice==4:
            searchPatient()
        elif choice==5:
            listofPatients()
        elif choice==6:
            print("Software Exited..")
            break
menu()