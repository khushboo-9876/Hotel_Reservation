from tkinter import *  
import tkinter

#form to be submitted
def  submit():
    print("your booking details are")
    
#booking form is generated by tkinter module    
def main():
    root=tkinter.Tk()
    root.geometry("500x500")
    root.title("Booking.com")
    label_0=tkinter.Label(root,text="Booking.com",width=20,font=("arial bold",20))
    label_0.place(x=90,y=53)

    label_1=tkinter.Label(root,text="Name",width=20,font=("bold",10))
    label_1.place(x=80,y=130)
    entry_1=tkinter.Entry(root)
    entry_1.place(x=240,y=130)
    
    label_2=tkinter.Label(root,text="booking date",width=20,font=("bold",10))
    label_2.place(x=68,y=180)
    entry_2=tkinter.Entry(root)
    entry_2.place(x=240,y=180)
    
    label_3=tkinter.Label(root,text="check-in-date",width=20,font=("bold",10))
    label_3.place(x=70,y=230)
    entry_3=tkinter.Entry(root)
    entry_3.place(x=240,y=230)
    
    label_4=tkinter.Label(root,text="check-out-date",width=20,font=("bold",10))
    label_4.place(x=72,y=280)
    entry_4=tkinter.Entry(root)
    entry_4.place(x=240,y=280)
    
    label_5=tkinter.Label(root,text="rooms",width=20,font=("bold",10))
    label_5.place(x=74,y=330)
    entry_5=tkinter.Entry(root)
    entry_5.place(x=240,y=330)
    
    tkinter.Button(root,text='submit',command=submit,width=20,bg='brown',fg='white').place(x=180,y=430)
    root.mainloop()
 
#creating a connection to pyhon shell    
if __name__=="__main__":
    main() 
 
#creating a five star hotels list    
def  star5(ch):
    tamt=0
    print("five star Hotels Name :  price in rupees")
    print('\n')
    print("1. radisson blu udaiur lace resort and spa:9,185")
    print("ABOUT US: as one of the words top hospitality companies,radisson blu udaiur lace resort committed to caring for people so they can be their best.")
    print('\n')
    print("2.savera hotel:4,302")
    print("ABOUT US: as one of the words top hospitality companies,savera hotels committed to caring for people so they can be their best.")
    print('\n')
    print("3.umaid bhawan heritage house hotel:6,480 ")
    print("ABOUT US: as one of the words top hospitality companies,umaid bhawan heritage house hotel committed to caring for people so they can be their best.")
    print('\n')
    print("4.lemon tree premiar hotel:8,328")
    print("ABOUT US: as one of the words top hospitality companies,lemon tree premiar hotel committed to caring for people so they can be their best.")
    print('\n')
    print("5.Hotel The Ambassador:8,029")
    print("ABOUT US: as one of the words top hospitality companies,hotel the ambassador committed to caring for people so they can be their best.")
    print('\n')
    print("6.the golkonda hotel:4,577")
    print("ABOUT US: as one of the words top hospitality companies,the golkonda hotels committed to caring for people so they can be their best.")
    print('\n')
    print("7.umaid a herityage site hotel:8,902")
    print("ABOUT US: as one of the words top hospitality companies,umaid a herityage site hotel committed to caring for people so they can be their best.")
    print('\n')
    print("8. Hotel Mirage:7,844")
    print("ABOUT US: as one of the words top hospitality companies,hotel mirage committed to caring for people so they can be their best.")
    print('\n')
    print("9. della adventure resorts:15,930")
    print("ABOUT US: as one of the words top hospitality companies,della adventure resorts committed to caring for people so they can be their best.")
    print('\n')
    print("10.Sun-n-Sand Mumbai:11,017")
    print("ABOUT US: as one of the words top hospitality companies,sun-n-sand committed to caring for people so they can be their best.")
    print('\n')
    print("members can save upto:20%")
    print("\n")         
    print("above prices with your choice of day/night")
    while  ch==1:
        a=int(input("Enter Your choice of H otels from above list: "))
        b=int(input("How Many no. of Days/Night:"))
        for  i in range(1,11):
           if a==1:
               c=b*9185
               d=math.fabs(c)
           elif a==2:
               c=b*4302
               d=math.fabs(c)
           elif a==3:
               c=b*64800
               d=math.fabs(c)
           elif a==4:
               c=b*8328
               d=math.fabs(c)
           elif a==5:
               c=b* 8029
               d=math.fabs(c)
           elif a==6:
               c=b*4577
               d=math.fabs(c)
           elif a==7:
               c=b*8902
               d=math.fabs(c)
           elif a==8:
               c=b*7844
               d=math.fabs(c)
           elif a==9:
               c=b*15930
               d=math.fabs(c)
           elif a==10:
               c=b*11017
               d=math.fabs(c)
           else:
               print("sorry you have entered no choice")
        tamt=tamt+c
        ch=input("do you want to book more hotels from above list:")
        print('\n')
        return tamt

#creating a  four star hotels list
def  star4(ch):
    tamt=0
    print("four star hotels Name:  price in rupees")
    print('\n')
    print("1. FabHotel Adlon International:2,759")
    print("ABOUT US:our hotel FabHotel Adlon International  are suitable both for business trips and for holidays. whether you visit us to relax, eat,work or find yourself,facilities are entirely at your service") 
    print('\n')
    print("2.Treebo Trend Olive Nest:2,687")
    print("ABOUT US:our hotel treebo trend olive  are suitable both for business trips and for holidays. whether you visit us to relax, eat,work or find yourself,facilities are entirely at your service") 
    print('\n')
    print("3.FabHotel urban Court DN Nagar:3,068 ")
    print("ABOUT US:our hotel FabHotel urban Court DN Nagar  are suitable both for business trips and for holidays. whether you visit us to relax, eat,work or find yourself,facilities are entirely at your service") 
    print('\n')
    print("4.Hotel Sharda:4,827")
    print("ABOUT US:our hotel hotel sharda  are suitable both for business trips and for holidays. whether you visit us to relax, eat,work or find yourself,facilities are entirely at your service") 
    print('\n')
    print("5.shahura house:4249")
    print("ABOUT US:our hotel shahura house  are suitable both for business trips and for holidays. whether you visit us to relax, eat,work or find yourself,facilities are entirely at your service") 
    print('\n')
    print("6.FabHotel Vinamra Residency:2,119")
    print("ABOUT US:our hotel fabhotel vinamara residency  are suitable both for business trips and for holidays. whether you visit us to relax, eat,work or find yourself,facilities are entirely at your service") 
    print('\n')
    print("7.Ramada Plaza Palm Grove:7,399")
    print("ABOUT US:our hotel ramada plaza plam grove  are suitable both for business trips and for holidays. whether you visit us to relax, eat,work or find yourself,facilities are entirely at your service") 
    print('\n')
    print("8. Hotel Mirage:7,844")
    print("ABOUT US:our hotel hotel mirage  are suitable both for business trips and for holidays. whether you visit us to relax, eat,work or find yourself,facilities are entirely at your service") 
    print('\n')
    print("9. Z Luxary Residences:5,907")
    print("ABOUT US:our hotel luxary residences  are suitable both for business trips and for holidays. whether you visit us to relax, eat,work or find yourself,facilities are entirely at your service") 
    print('\n')
    print("10.hotel express inn:2,562")
    print("ABOUT US:our hotel hotel express  are suitable both for business trips and for holidays. whether you visit us to relax, eat,work or find yourself,facilities are entirely at your service") 
    print('\n')
    print("\n")
    print("members can save upto:15%")
    print("\n") 
    print("above prices with your choice of day/night")
    while ch==2:
        a=int(input("Enter Your choice of Hotels from above list:"))
        b=int(input("How Many no. of Days/Night:"))
        for  i in range(1,11):
           if a==1:
               c=b*2759
               d=math.fabs(c)
           elif a==2:
               c=b*2687
               d=math.fabs(c)
           elif a==3:
               c=b*3068
               d=math.fabs(c)
           elif a==4:
               c=b*4827
               d=math.fabs(c)
           elif a==5:
               c=b* 3249
               d=math.fabs(c)
           elif a==6:
               c=b*2119
               d=math.fabs(c)
           elif a==7:
               c=b*7399
               d=math.fabs(c)
           elif a==8:
               c=b*7844
               d=math.fabs(c)
           elif a==9:
               c=b*5907
               d=math.fabs(c)
           elif a==10:
               c=b*2562
               d=math.fabs(c)
           else:
               print("sorry you have entered no choice")
        tamt=tamt+c
        ch=input("do you want to book more hotels from above list:")
        print('\n')
        return tamt

#creating a three star hotels list
def  star3(ch):
    tamt=0
    print("three star Hotels Name:  price in rupees")
    print('\n')
    print("1. FabHotel Adlon International:2,759")
    print("ABOUT US:THE Fabhotel provide best facilities to our customers with reasonable price. ") 
    print('\n')
    print("2.Treebo Trend Olive Nest:2,687")
    print("ABOUT US:THE treebo  trend provide best facilities to our customers with reasonable price. ") 
    print('\n')
    print("3.FabHotel urban Court DN Nagar:3,068 ")
    print("ABOUT US:THE fabhotelhotel urban court provide best facilities to our customers with reasonable price. ") 
    print('\n')
    print("4.Hotel Sharda:4,827")
    print("ABOUT US:THE hotel sharda provide best facilities to our customers with reasonable price. ") 
    print('\n')
    print("5.shahura house:4249")
    print("ABOUT US:THE shahura provide best facilities to our customers with reasonable price. ") 
    print('\n')
    print("6.FabHotel Vinamra Residency:2,119")
    print("ABOUT US:THE Fabhotel vinamara residancy provide best facilities to our customers with reasonable price. ") 
    print('\n')
    print("7.Ramada Plaza Palm Grove:7,399")
    print("ABOUT US:THE ramada laza alm graver provide best facilities to our customers with reasonable price. ") 
    print('\n')
    print("8. Hotel Mirage:7,844")
    print("ABOUT US:THE hotel mirage provide best facilities to our customers with reasonable price. ") 
    print('\n')
    print("9. Z Luxary Residences:5,907")
    print("ABOUT US:THE luxary residancy provide best facilities to our customers with reasonable price. ") 
    print('\n')
    print("10.hotel express inn:2,562")
    print("ABOUT US:THE hotel exress provide best facilities to our customers with reasonable price. ") 
    print('\n')
    print("\n")
    print("members can save upto:10%")
    print("\n") 
    print("above prices with your choice of day/night")
    while ch==3:
        a=int(input("Enter Your choice of Hotels from above list: "))
        b=int(input("How Many no. of Days/Night:"))
        for i in range(1,11):
           if a==1:
               c=b*2759
               d=math.fabs(c)
           elif a==2:
               c=b*2687
               d=math.fabs(c)
           elif a==3:
               c=b*3068
               d=math.fabs(c)
           elif a==4:
               c=b*4827
               d=math.fabs(c)
           elif a==5:
               c=b* 3249
               d=math.fabs(c)
           elif a==6:
               c=b*2119
               d=math.fabs(c)
           elif a==7:
               c=b*7399
               d=math.fabs(c)
           elif a==8:
               c=b*7844
               d=math.fabs(c)
           elif a==9:
               c=b*5907
               d=math.fabs(c)
           elif a==10:
               c=b*2562
               d=math.fabs(c)
           else:
                print("sorry you have entered no choice")
        tamt=tamt+c
        ch=input("do you want to book more hotels from above list:")
        print('\n')
        return tamt

#creatin a two star hotel list
def  star2(ch):
        tamt=0
        print("two star  Hotels Name:  price in rupees")
        print('\n')
        print("1. FabHotel Adlon International:2,759")
        print("ABOUT US:FabHotel Adlon International best facilities") 
        print('\n')
        print("2.Treebo Trend Olive Nest:2,687")
        print("ABOUT US:Treebo Trend Olive Nest best facilities") 
        print('\n')
        print("3.FabHotel urban Court DN Nagar:3,068 ")
        print("ABOUT US:FabHotel urban Court DN Nagar best facilities")
        print('\n')
        print("4.Hotel Sharda:4,827")
        print("ABOUT US:Hotel Sharda best facilities ")
        print('\n')
        print("5.shahura house:4249")
        print("ABOUT US:shahura house best facilities ") 
        print('\n')
        print("6.FabHotel Vinamra Residency:2,119")
        print("ABOUT US:FabHotel Vinamra Residency best facilities ") 
        print('\n')
        print("7.Ramada Plaza Palm Grove:7,399")
        print("ABOUT US:Ramada Plaza Palm Grove best facilities ") 
        print('\n')
        print("8. Hotel Mirage:7,844")
        print("ABOUT US:Hotel Mirage best facilities ") 
        print('\n')
        print("9. Z Luxary Residences:5,907")
        print("ABOUT US: Z Luxary Residences best facilities ") 
        print('\n')
        print("10.hotel express inn:2,562")
        print("ABOUT US:hotel express inn best facilities ")
        print('\n')
        print("\n")
        print("members can save upto:5%")
        print("\n") 
        print("above prices with your choice of day/night")
        while ch==4:
                a=int(input("Enter Your choice of Hotels from above list: "))
                b=int(input("How Many no. of Days/Night:"))
                for  i in range(1,11):
                    if a==1:
                         c=b*2759
                         d=math.fabs(c)
                    elif a==2:
                         c=b*2687
                         d=math.fabs(c)
                    elif a==3:
                          c=b*3068
                          d=math.fabs(c)
                    elif a==4:
                          c=b*4827
                          d=math.fabs(c)
                    elif a==5:
                          c=b* 3249
                          d=math.fabs(c)
                    elif a==6:
                          c=b*2119
                          d=math.fabs(c)
                    elif a==7:
                          c=b*7399
                          d=math.fabs(c)
                    elif a==8:
                           c=b*7844
                           d=math.fabs(c)
                    elif a==9:
                           c=b*5907
                           d=math.fabs(c)
                    elif a==10:
                            c=b*2562
                            d=math.fabs(c)
                    else:
                            print("sorry you have entered no choice")
                    tamt=tamt+c
                    ch=input("do you want to book more hotels from above list:")
                    print('\n')
                    return tamt

#creating a normal hotels list
def  hotellist(ch):
        tamt=0
        print("top  rated  Hotels  Name  : price in rupees")
        print('\n')
        print("1. Hotel  ramhan  aerocity:1868")
        print('\n')
        print("2.Treebo Trend Olive Nest:2,687")
        print('\n')
        print("3.the danish residancy:1762")
        print('\n')
        print("4.hotel smart plaza:1004")
        print('\n')
        print("5.hotel mint safdarjung:2823")
        print('\n')
        print("6.shreyans inn:2934")
        print('\n')
        print("7.airport hotel mayank:920")
        print('\n')
        print("8.hotel international inn:1766")
        print('\n')
        print("9.hotel toronto:1315")
        print('\n')
        print("10.sawera international:1076")
        print('\n')
        print("above prices with your choice of day/night")
        while  ch==5:
                     a=int(input("Enter Your choice of Hotels from above list: "))
                     b=int(input("How Many no. of Days/Night:"))
                     for  i in range(1,11):
                                if a==1:
                                       c=b*1868
                                       d=math.fabs(c)
                                elif a==2:
                                       c=b*2687
                                       d=math.fabs(c)
                                elif a==3:
                                       c=b*1762
                                       d=math.fabs(c)
                                elif a==4:
                                       c=b*1004
                                       d=math.fabs(c)
                                elif a==5:
                                       c=b*2823
                                       d=math.fabs(c)
                                elif a==6:
                                      c=b*2934
                                      d=math.fabs(c)
                                elif a==7:
                                      c=b*920
                                      d=math.fabs(c)
                                elif a==8:
                                     c=b*1766
                                     d=math.fabs(c)
                                elif a==9:
                                     c=b*1315
                                     d=math.fabs(c)
                                elif a==10:
                                     c=b*1076
                                     d=math.fabs(c)
                                else:
                                     print("sorry you have entered no choice")
                                tamt=tamt+c
                                ch=input("do you want to book more hotels from above list:")
                                print('\n')
                                return tamt

#__main__
import math 
ch=0
import tkinter
while (ch!=6):
        print('\n')
        print("\t")
        print("###########WELCOME TO THE FIVE STAR HOTELS#############")
        print("\t")
        print('\n')
        print("Press  1  Five Star Hotels")
        print("Press  2  Four Star Hotels")
        print("Press  3  Three Star Hotels")
        print("Press  4  Two Star Hotels")
        print("Press  5  Hotels List")
        print("Press  6  Exit")
        ch=int(input("Enter Your choice(1-6):"))
        if ch==1: 
              y=star5(ch)
              print(y)
              input("press enter to continue......")
        elif ch==2:
              r=star4(ch)
              print(r)
              input("press enter to continue......")
        elif ch==3:
              s=star3(ch)
              print(s)
              input("press enter to continue......")
        elif ch==4:
               e=star2(ch)
               print(e)
               input("press enter to continue......")
        elif ch==5:
               d=hotellist(ch)
               print(d)
               input("press enter to continue......")
        elif ch==6:
               break
        else:
               print("invalid choice")
               input("press enter to continue")
