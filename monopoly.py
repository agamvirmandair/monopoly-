
print()
print()
print()
print()
print(" THE MONOPOLY BOARD MAY NOT BE DISPLAYED ON SMALLER DISPLAYS(LAPTOPS ETC.). TO DISPLAY IT PROPERLY PLEASE ZOOM OUT (CTRL  -) BEFORE RUNNING AND THEN ZOOM BACK IN( CTRL +) WHEN THE CODE STARTS")
print()
print()
print()
print()

from colorama import init ,Fore, Back, Style
from random import randint
init()
parti={}
black_dict={}
jail_time={}
result_flag=0
n=int(input('No. of Participants: '))
for x in range(1,n+1):
      while True:
            name=input('Name of Participant NO.'+str(x)+'(MAX 7 CHARACTER): ').upper()
            if len(name)==7:
                  parti[name]=[1500,0,0,0]
                  #funds,positiom,get out of jail cards,total no. of apartments/hotels
                  black_dict[name]=[]
                  jail_time[name]=0
                  break
            elif len(name)<7:
                   for x in range(7-len(name)):
                          name+=' '
                   parti[name]=[1500,0,0,0]
                   black_dict[name]=[]
                   jail_time[name]=0
                   break
            else:print("Invalid Participant Name")
                  


keys=list(parti.keys())
a0=[]
for key in keys:
       avatar=[key[0]+key[1]]
       a0+=avatar

ut1=ut2=''
rent=[0,60,0,60,200,200,100,0,100,120,0,140,150,140,160,200,180,0,180,200,0,220,0,220,240,200,260,260,150,280,0,300,300,0,320,200,0,350,100,400]
apt=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


community_chestp=['Advance to Go (Collect M200)'
,'Bank error in your favor. Collect M200'
,"Doctor's fee. Pay M50"
,'From sale of stock you get M50'
,'Get Out of Jail Free'
,'Go to Jail. Go directly to jail, do not pass Go, do not collect M200'
,'Holiday fund matures. Receive M100'
,'Income tax refund. Collect M20'
,'It is your birthday. Collect M10 from every player'
,'Life insurance matures. Collect M100'
,'Pay hospital fees of M100'
,'Pay school fees of M50'
,'Receive M25 consultancy fee'
,'You are assessed for street repair. M40 per apartment. M115 per hotel'
,'You have won second prize in a beauty contest. Collect M10'
,'You inherit M100']

chancep=['Advance to Boardwalk'
,'Advance to Go (Collect M200)'
,'Advance to Illinois Avenue. If you pass Go, collect M200'
,'Advance to St. Charles Place. If you pass Go, collect M200'
,'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled'
,'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled'
,'Advance to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.'
,'Bank pays you dividend of M50'
,'Get Out of Jail Free'
,'Go Back 3 Spaces'
,'Go to Jail. Go directly to Jail, do not pass Go, do not collect M200'
,'Make general repairs on all your property. For each apartment pay M25. For each hotel pay M100'
,'Speeding fine M15'
,'Take a trip to Reading Railroad. If you pass Go, collect M200'
,'You have been elected Chairman of the Board. Pay each player M50'
,'Your building loan matures. Collect M150']


a1=a2=a3=a4=a5=a6=a7=a8=a9=a10='[]'
a11=a12=a13=a14=a15=a16=a17=a18=a19=a20='[]'
a21=a22=a23=a24=a25=a26=a27=a28=a29=a30='[]'
a31=a32=a33=a34=a35=a36=a37=a38=a39='[]'
a10j='JAIL'

yellow1=black=cyan1=pink=cyan2=red=yellow2=green=blue=''


o1=o3=o5=o6=o8=o9='UNOWNED'
o11=o12=o13=o14=o15=o16=o18=o19='UNOWNED' 
o21=o23=o24=o25=o26=o27=o28=o29='UNOWNED'
o31=o32=o34=o35=o37=o39='UNOWNED'
o7=o22=o36=' '
o2=o17=o33='  '
o4=o38='TAXINGS'
o10=o20=''
o30='JAIL'


def chance():
      global chance_no
      chance_no=randint(0,15)
      print(chancep[chance_no])
      chance_execute=input('Press ENTER Execute/Collect chance card')
      if chance_no==0:
            globals()['o'+str(parti[key][1])]='[]'
            parti[key][1]=39
      if chance_no==1:
            globals()['o'+str(parti[key][1])]='[]'
            parti[key][1]=40
      if chance_no==2:
            globals()['o'+str(parti[key][1])]='[]'
            if parti[key][1]>=36:
                  
                  parti[key][1]=64
            else:
                  parti[key][1]=24
      if chance_no == 3:
            globals()['o'+str(parti[key][1])]='[]'
            if parti[key][1]>=22:
                  parti[key][1]=51
            else:
                  parti[key][1]=11
      if chance_no == 4:
            globals()['o'+str(parti[key][1])]='[]'
            if parti[key][1]==7:
                  parti[key][1]=15
            if parti[key][1]==22:
                  parti[key][1]=25
            if parti[key][1]==36:
                  parti[key][1]=45
      if chance_no == 5:
            globals()['o'+str(parti[key][1])]='[]'
            if parti[key][1]==7:
                  parti[key][1]=15
            if parti[key][1]==22:
                  parti[key][1]=25
            if parti[key][1]==36:
                  parti[key][1]=45
      if chance_no == 6:
            globals()['o'+str(parti[key][1])]='[]'
            if parti[key][1]==22:parti[key][1]=28
            if parti[key][1]==36 or parti[key][1]==7:parti[key][1]=12
      if chance_no == 7:parti[key][0]+=50
      if chance_no == 8:parti[key][2]+=1
      if chance_no == 9:
            globals()['o'+str(parti[key][1])]='[]'
            parti[key][1]-=3
      if chance_no == 10:
            a10j=' '+key[0]+key[1]+' '
            globals()['o'+str(parti[key][1])]='[]'
            parti[key][1]=101
            jail_time[key]=3
      if chance_no == 11:
            parti[key][0]-=(parti[key][3]*25)
      if chance_no == 12:parti[key][0]-=15
      if chance_no == 13:
            globals()['o'+str(parti[key][1])]='[]'
            parti[key][1]=45
      if chance_no == 14:
            amt=50*(len(parti)-1)
            parti[key][0]-=amt
            for x in keys:
                  if x!=key:
                        parti[x][0]+=50

      if chance_no == 15:parti[key][0]+=150
      if parti[key][1]>39:
            globals()['o'+str(parti[key][1])]='[]'
            parti[key][1]-=40
            parti[key][0]+=200
      
def community_chest():
      chest_no=randint(0,15)
      print(community_chestp[chest_no])
      chest_execute=input('Press ENTER Execute/Collect community chest card')
      if chest_no==0:
            globals()['o'+str(parti[key][1])]='[]'
            parti[key][1]=40
      if chest_no==1:parti[key][0]+=200
      if chest_no==2:parti[key][0]-=50
      if chest_no == 3:parti[key][0]+=50
      if chest_no == 4:parti[key][2]+=1
      if chest_no == 5:
            a10j=' '+key[0]+key[1]+' '
            globals()['o'+str(parti[key][1])]='[]'
            parti[key][1]=101
            jail_time[key]=3
      if chest_no == 6:parti[key][0]+=100
      if chest_no == 7:parti[key][0]+=20
      if chest_no == 8:
            parti[key][2]+=10*len(keys)
            for x in keys:
                  if x!=key:
                        parti[x][0]-=10

      if chest_no == 9:parti[key][0]+=100
      if chest_no == 10:parti[key][0]-=100
      if chest_no == 11:parti[key][0]-=50
      if chest_no == 12:parti[key][0]+=25
      if chest_no == 13:
            if parti[key][3]>4:
                  parti[key][0]-=(115*(parti[key][3]-4))
            else:
                  parti[key][0]-=(40*parti[key][3])

      if chest_no == 14:parti[key][0]+=10

      if chest_no == 15:parti[key][0]+=100

      if parti[key][1]>39:
            globals()['o'+str(parti[key][1])]='[]'
            parti[key][1]-=40
            parti[key][0]+=200
      
def prnt_board():
            print()
            print()
            print()
            print(Back.WHITE+Fore.RED+' ','FREE PARKING','',Back.RESET+'  ',
                  Back.RED+'KENTUCKY AVENUE',Back.RESET+'  ',
                  Fore.BLUE + Back. WHITE+ Style.BRIGHT+'     CHANCE     ',Back.RESET+'  ',
                  Back.RED+'INDIANA AVENUE',Back.RESET+'  ',
                  Back.RED+'ILLINOIS AVENUE',Back.RESET+'  ',
                  Back.BLACK + Fore.WHITE+ Style.BRIGHT+' B. & O. RAILROADS' ,Back.RESET+' ',
                  Back.YELLOW+'ATLANTIC AVENUE',Back.RESET+'  ',
                  Back.YELLOW+'VENTNOR AVENUE',Back.RESET+'  ',
                  Back.WHITE + Fore.BLACK+ Style.BRIGHT+' WATER WORKS' ,Back.RESET+'  ',
                  Back.YELLOW+'MARVIN GARDENS',Back.RESET+'  ',
                  Fore.WHITE + Back.BLUE+ Style.BRIGHT+'  GO TO JAIL! ',Back.RESET+'')

            print(Back.WHITE+'               ',Back.RESET+'  ',
                  Fore.RED+'|','    M'+str(rent[21]),'    |',Back.RESET+' ',
                  Back.WHITE+ Fore.BLUE+'        ?       ',Back.RESET+'  ',
                  Fore.RED+'|','    M'+str(rent[23]),'   |',Back.RESET+' ',
                  Fore.RED+'|','    M'+str(rent[24]),'    |',Back.RESET+' ',
                  Fore.WHITE+'|','     M'+str(rent[25]),'     |',Back.RESET+' ',
                  Fore.YELLOW+'|','    M'+str(rent[26]),'    |',Back.RESET+' ',
                  Fore.YELLOW+'|','    M'+str(rent[27]),'   |',Back.RESET+' ',
                  Fore.WHITE+'|','   M'+str(rent[28]),'  |',Back.RESET+' ',
                  Fore.YELLOW+'|','    M'+str(rent[29]),'   |',Back.RESET+' ',
                  Back.BLUE+'              ',Back.RESET+'  ')

            print(Back.WHITE+ Fore.RED+'      ',a20,'     ',Back.RESET+'  ',
                  Fore.RED+'|     ',a21,'     |',Back.RESET+' ',
                  Back.WHITE+ Fore.BLUE+'      ',a22,'      ',Back.RESET+'  ',
                  Fore.RED+'|     ', a23,'    |',Back.RESET+' ',
                  Fore.RED+'|     ',a24,'     |',Back.RESET+' ',
                  Fore.WHITE+'|      ',a25,'      |',Back.RESET+' ',
                  Fore.YELLOW+'|     ',a26,'     |',Back.RESET+' ',
                  Fore.YELLOW+'|     ',a27,'    |',Back.RESET+' ',
                  Fore.WHITE+'|    ',a28,'   |',Back.RESET+' ',
                  Fore.YELLOW+'|     ',a29,'    |',Back.RESET+' ',
                  Back.BLUE+'      ',a30,'    ',Back.RESET+'  ')
            
            print(Back.WHITE+ '               ',Back.RESET+'  ',
                  Fore.RED+'|   ',o21,'  |',Back.RESET+' ',
                  Back.WHITE+ Fore.BLUE+'                ',Back.RESET+'  ',
                  Fore.RED+'|   ', o23,' |',Back.RESET+' ',
                  Fore.RED+'|   ',o24,'  |',Back.RESET+' ',
                   Fore.WHITE+'|    ',o25,'   |',Back.RESET+' ',
                   Fore.YELLOW+'|   ',o26,'  |',Back.RESET+' ',
                   Fore.YELLOW+'|   ',o27,' |',Back.RESET+' ',
                   Fore.WHITE+'|  ',o28,'|',Back.RESET+' ',
                   Fore.YELLOW+'|   ',o29,' |',Back.RESET+' ',
                   Back.BLUE+'              ',Back.RESET+'  ')
            
            print()

            print(Fore.WHITE+Back.CYAN+'NEW YORK AVENUE',Back.RESET+'                                                                                                                                                                          ',
                  Back.GREEN+Fore.BLACK+ 'PACIFIC AVENUE',Back.RESET+'')
            
            print(Fore.CYAN+'|','    M'+str(rent[19]),'    |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.GREEN+'|','    M'+str(rent[31]),'   |',Back.RESET+'')
            
            print(Fore.CYAN+'|     ',a19,'     |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.GREEN+'|     ',a31,'    |',Back.RESET+' ')
            
            print(Fore.CYAN+'|   ',o19,'  |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.GREEN+'|   ',o31,' |',Back.RESET+' ')
            
            print()

            print(Fore.WHITE+Back.CYAN+'TENNESSE AVENUE',Back.RESET+'                                                                                                                                                                          ',
                  Back.GREEN+Fore.BLACK+ 'NORTH CAROLINA',Back.RESET+'')
            
            print(Fore.CYAN+'|','    M'+str(rent[18]),'    |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.GREEN+'|','    M'+str(rent[32]),'   |',Back.RESET+'')
            
            print(Fore.CYAN+'|     ',a18,'     |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.GREEN+'|      ',a32,'   |',Back.RESET+' ')
            
            print(Fore.CYAN+'|   ',o18,'  |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.GREEN+'|   ',o32,' |',Back.RESET+' ')
            
            print()
            
            print(Fore.YELLOW+Back.WHITE+'COMMUNITY CHEST',Back.RESET+'                                                                                                                                                                          ',
                  Fore.YELLOW+Back.WHITE+'COMMUNITY CHEST',Back.RESET+'')
            
            print(Fore.YELLOW+Back.WHITE+'===============',Back.RESET+'                                                                                                                                                                          ',
                  Fore.YELLOW+Back.WHITE+'===============',Back.RESET+'')
            
            print(Back.WHITE+'      ',a17,'     ',Back.RESET+'                                                                                                                                                                          ',
                  Back.WHITE+'      ',a33,'     ',Back.RESET+'')
            
            print(Back.WHITE+'               ',Back.RESET+'                                                                                                                                                                          ',
                  Back.WHITE+'               ',Back.RESET+'')
            
            
            
            print()

            print(Fore.WHITE+Back.CYAN+' ST JAMES PLACE',Back.RESET+'                                                                                                                                                                          ',
                  Back.GREEN+Fore.BLACK+ ' PENNS. AVENUE ',Back.RESET+'')
            
            print(Fore.CYAN+'|','    M'+str(rent[16]),'    |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.GREEN+'|','     M'+str(rent[34]),'   |',Back.RESET+'')
            
            print(Fore.CYAN+'|     ',a16,'     |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.GREEN+'|      ',a34,'    |',Back.RESET+' ')
            
            print(Fore.CYAN+'|   ',o16,'  |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.GREEN+'|   ',o34,'  |',Back.RESET+' ')
            
            print('                                                     ',Back.RED+ '                       ____            ____    ____    ____                          ',Back.RESET+'',)

            print(Back.BLACK + Fore.WHITE+ Style.BRIGHT+'PENNS. RAILROAD' ,Back.RESET+'                                     ',
            Back.RED+ '            |\    /|  |    |  |\   |  |    |  |    |  |    |  |    \   /             ',Back.RESET+'                                              ',
            Back.BLACK + Fore.WHITE+ Style.BRIGHT+'   SHORT LINE  ' ,Back.RESET+'')

            print(Fore.WHITE+'|','     M'+str(rent[15]),'   |',Back.RESET+'                                    ',
                  Back.RED+ '            | \  / |  |    |  | \  |  |    |  |____|  |    |  |     \ /              ',Back.RESET+'                                              ',
                  Fore.WHITE+'|','     M'+str(rent[35]),'   |',Back.RESET+'')
            
            print(Fore.WHITE+'|     ',a15,'     |',Back.RESET+'                                    ',
                  Back.RED+ '            |  \/  |  |    |  |  \ |  |    |  |       |    |  |      V               ',Back.RESET+'                                              ',
                  Fore.WHITE+'|      ',a35,'    |',Back.RESET+' ')
            
            print(Fore.WHITE+'|   ',o15,'  |',Back.RESET+'                                    ',
                  Back.RED+ '            |      |  |____|  |   \|  |____|  |       |____|  |____  |               ',Back.RESET+'                                              ',
                  Fore.WHITE+'|   ',o35,'  |',Back.RESET+' ')
            
            print('                                                     ',Back.RED+ '                                                                                     ',Back.RESET+'                                    ',)
            
            print(Fore.WHITE+Back.MAGENTA+'VIRGINIA AVENUE',Back.RESET+'                                                                                                                                                                          ',
                  Back.WHITE+Fore.BLUE+ '     CHANCE    ',Back.RESET+'')
            
            print(Fore.MAGENTA+'|','    M'+str(rent[14]),'    |',Back.RESET+'                                                                                                                                                                         ',
                  Back.WHITE+ Fore.BLUE+'        ?      ',Back.RESET+'')
            
            print(Fore.MAGENTA+'|     ',a14,'     |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.BLUE+Back.WHITE+'      ',a36,'     ',Back.RESET+' ')
            
            print(Fore.MAGENTA+'|   ',o14,'  |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.BLUE+Back.WHITE+'               ',Back.RESET+' ')
            
            print()
            
            print(Fore.WHITE+Back.MAGENTA+' STATES AVENUE ',Back.RESET+'                                                                                                                                                                          ',
                  Back.BLUE+Fore.WHITE+ '  PARK PLACE   ',Back.RESET+'')
            
            print(Fore.MAGENTA+'|','    M'+str(rent[13]),'    |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.BLUE+'|     M'+str(rent[37])+'     |',Back.RESET+'')
            
            print(Fore.MAGENTA+'|     ',a13,'     |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.BLUE+'|     ',a37,'     |',Back.RESET+' ')
            
            print(Fore.MAGENTA+'|   ',o13,'  |',Back.RESET+'                                                                                                                                                                         ',
                  Fore.BLUE+'|   ',o37,'  |',Back.RESET+' ')
            
            print()
 
            print(Fore.BLACK+Back.WHITE+'ELECTRIC COMPANY',Back.RESET+'                                                                                                                                                                         ',
                  Back.WHITE+Fore.BLACK+ '   LUXURY TAX  ',Back.RESET+'')
            
            print(Fore.WHITE+'|','    M'+str(rent[12]),'     |',Back.RESET+'                                                                                                                                                                        ',
                  Fore.RED+'|     M'+str(rent[38])+'     |',Back.RESET+'')
            
            print(Fore.WHITE+'|     ',a12,'      |',Back.RESET+'                                                                                                                                                                        ',
                  Fore.RED+'|     ',a38,'     |',Back.RESET+' ')
            
            print(Fore.WHITE+'|   ',o12,'   |',Back.RESET+'                                                                                                                                                                        ',
                  Fore.RED+'|   ',o38,'  |',Back.RESET+' ')
            
            print()
            
            print(Fore.WHITE+Back.MAGENTA+'ST.CHARLES PLACE',Back.RESET+'                                                                                                                                                                         ',
                  Back.BLUE+Fore.WHITE+ '    BOARDWALK  ',Back.RESET+'')
            
            print(Fore.WHITE+'|','    M'+str(rent[11]),'     |',Back.RESET+'                                                                                                                                                                        ',
                  Fore.BLUE+'|     M'+str(rent[39])+'     |',Back.RESET+'')
            
            print(Fore.WHITE+'|     ',a11,'      |',Back.RESET+'                                                                                                                                                                        ',
                  Fore.BLUE+'|     ',a39,'     |',Back.RESET+' ')
            
            print(Fore.WHITE+'|   ',o11,'   |',Back.RESET+'                                                                                                                                                                        ',
                  Fore.BLUE+'|   ',o39,'  |',Back.RESET+' ')
            
            print()

            print(Back.BLACK + Fore.YELLOW+'     |           ',Back.RESET+'  ',
                  Back.CYAN + Fore.WHITE+ 'CONNECTICUT AVENUE', Back.RESET+'  ',
                  Back.CYAN + Fore.WHITE+ 'VERMONT AVENUE', Back.RESET+'  ',
                  Fore.BLUE + Back. WHITE+ Style.BRIGHT+'    CHANCE    ',Back.RESET+'  ',
                  Back.CYAN + Fore.WHITE+ 'ORIENTAL AVENUE', Back.RESET+'  ',
                  Back.BLACK + Fore.WHITE+ 'READING RAILROAD' ,Back.RESET+' ',
                  Back.WHITE+Fore.BLACK+ '  INCOME TAX  ',Back.RESET+'  ',
                  Back.YELLOW+'BALTIC AVENUE',Back.RESET+'  ',
                  Back.WHITE+'COMMUNITY CHEST',Back.RESET+'  ',
                  Back.YELLOW+'MEDITERRANEAN',Back.RESET+' ',
                  Back.BLACK +Fore.WHITE +'        GO       ', Back.RESET+'')
            

            print(Back.BLACK + Fore.YELLOW+'JUST |    '+a10j+'   ',Back.RESET+'  ',
                  Fore.CYAN+'|','      M'+str(rent[9]),'     |',Back.RESET+' ',
                  Fore.CYAN+'|','    M'+str(rent[8]),'   |',Back.RESET+' ',
                  Back.WHITE+ Fore.BLUE+'      ?       ',Back.RESET+'  ',
                  Fore.CYAN+'|','    M'+str(rent[6]),'    |',Back.RESET+' ',
                  Fore.WHITE+'|','     M'+str(rent[5]),'    |',Back.RESET+'',
                  Fore.RED+'|     M'+str(rent[4])+'    |',Back.RESET+' ',
                  Fore.YELLOW+'| ','   M'+str(rent[3]),'   |',Back.RESET+' ',
                  Fore.YELLOW+Back.WHITE+'===============',Back.RESET+'  ',
                  Fore.YELLOW+'|','   M'+str(rent[1]),'    |',Back.RESET+'',
                   Back.BLACK +Fore.WHITE +'   COLLECT M200  ', Back.RESET+'')


            print(Back.BLACK + Fore.YELLOW+ Style.BRIGHT+' ',a10,'|_ _ _ _ _ _',Back.RESET+'  ',
                  Fore.CYAN+'|       ',a9,'      |',Back.RESET+' ',
                  Fore.CYAN+'|     ',a8,'    |',Back.RESET+' ',
                  Back.WHITE+ Fore.BLUE+'     ',a7,'     ',Back.RESET+'  ',
                  Fore.CYAN+'|     ',a6,'     |',Back.RESET+' ',
                  Fore.WHITE+'|      ',a5,'     |',Back.RESET+'',
                  Fore.RED+'|     ',a4,'    |',Back.RESET+' ',
                  Fore.YELLOW+'|     ',a3,'   |',Back.RESET+' ',
                  Back.WHITE+'      ',a2,'     ',Back.RESET+'  ',
                  Fore.YELLOW+'|   ',a1,'     |',Back.RESET+'',
                  Back.BLACK +Fore.WHITE +'    AS YOU PASS  ', Back.RESET+'')

            print(Back.BLACK + Fore.YELLOW+'   VISITING      ',Back.RESET+'  ',
                  Fore.CYAN+'|    ',o9,'    |',Back.RESET+' ',
                  Fore.CYAN+'|   ',o8,' |',Back.RESET+' ',
                  Back.WHITE+ Fore.BLUE+'              ',Back.RESET+'  ',
                  Fore.CYAN+'|   ',o6,'  |',Back.RESET+' ',
                  Fore.WHITE+'|    ',o5,'  |',Back.RESET+'',
                  Fore.RED+'|   ',o4,' |',Back.RESET+' ',
                  Fore.YELLOW+'|   ',o3,'|',Back.RESET+' ',
                  Back.WHITE+'               ',Back.RESET+'  ',
                  Fore.YELLOW+'|  ',o1,' |',Back.RESET+'',
                  Back.BLACK +Fore.RED +'  <-------',a0, Back.RESET+'',Fore.RESET)

def apt_hot():
      while True:
            print('Current Balance in Account: M'+str(parti[key][0]))
            no=int(input('Enter Property number you want to build a apartment/hotel in (Eg: Go-0, MEDITERRANEAN-1): '))
            color_group=input('Enter Color group of property (yellow1,cyan1,pink,cyan2,red,yellow2,green,blue): ')
            print('Cost of building each apartment/hotel: M105')
            nos=int(input('How many apartments/hotels would you like to create(Max:6, Input 0 to exit ): '))
            if nos*105>parti[key][0]:
                  print('INSUFFICIENT FUNDS')
            elif nos==0:break
            else:
                  for x in range(nos):
                        if apt[no]<=6:
                              if color_group=='black':print('You cant construct apartments/hotels on railway stations')
                              elif globals()[color_group]==key:
                                    parti[key][0]-=105
                                    parti[key][3]+=1
                                    rent[no]=int(rent[no]*1.6)
                                    apt[no]+=1
                                    break
                              
                              else:print("You Don't Have all the properties of this same color group" )
                        else:
                              print('Max Number of buildings reached on this property')
                              break

def trade():
      invalid=0
      while True:
            name=input('Trade with (USERNAME):').upper()
            if len(name)<7:
                  for x in range(7-len(name)):
                              name+=' '
            money_offer=int(input('Money Offering(if not enter 0): '))
            money_rec=int(input('Money Recieving(if not enter 0): '))
            prop_offer=int(input('Property No.(0-39) offering(if not enter any number above 39): '))
            prop_rec=int(input('Property No.(0-39) Recieving(if not enter any number above 39): '))
            gol_offer=int(input('Get Out of Jail free card offering(0 or 1): '))
            gol_rec=int(input('Get Out of Jail free card recieving(0 or 1): '))
            if prop_offer>39:prop_offer='N.A'
            if prop_rec>39:prop_rec='N.A'
            if name not in keys or len(name)>7:
                  print('Invalid username')
                  invalid=1
            if gol_offer not in [0,1]:
                  print('Invalid no. of get out of jail cards')
                  invalid=1
            
            if gol_rec not in [0,1]:
                  print('Invalid no. of get out of jail cards')
                  invalid=1
            
            if invalid==0:
                  
                  break
      print()
      print()
      print()
      print('OFFER TO',name,'BY',key)
      print('Money Offering:',money_offer)
      print('Money Recieving:',money_rec)
      print('Property No.(1-39) offering:',prop_offer)
      print('Property No.(1-39) Recieving:',prop_rec)
      print('Get Out of Jail free card offering(0 or 1):',gol_offer)
      print('Get Out of Jail free card recieving(0 or 1):',gol_rec)
      print()
      while True:
            print('1. Accept Offer')
            print('2. Reject Offer')
            trade_no=int(input(name+"'s Descision(1-2): "))
            print(trade_no)
            if trade_no==1:
                  print('OFFER ACCEPTED!')
                  if money_offer!=0:
                        parti[name][0]+=money_offer
                        parti[key][0]-=money_offer
                  if money_rec!=0:
                        parti[name][0]-=money_rec
                        parti[key][0]+=money_rec
                  
                  if gol_offer!=0:
                        parti[name][2]+=gol_offer
                        parti[key][2]-=gol_offer
                  if gol_rec!=0:
                        parti[name][2]-=gol_rec
                        parti[key][2]+=gol_rec
                  if prop_offer!='N.A':
                        property_desig='o'+str(prop_offer)
                        globals()[property_desig]=name
                        if property_desig=='o5'or'o15'or'o25'or'o35':
                                    black_dict[name]+=[prop_offer]
                                    black_dict[key].remove(prop_offer)
                        elif property_desig=='o12':ut1=name
                        elif property_desig=='o28':ut2=name

                  if prop_rec!='N.A':
                        property_desig='o'+str(prop_rec)
                        globals()[property_desig]=key
                        if property_desig=='o5'or property_desig=='o15'or property_desig=='o25'or property_desig=='o35':
                                    black_dict[key]+=[prop_rec]
                                    black_dict[name].remove(prop_rec)
                        elif property_desig=='o12':ut1=key
                        elif property_desig=='o28':ut2=key
                  break

            elif trade_no==2:
                  print('OFFER REJECTED')
                  break
            else:print('Invalid Request')

def pay_rent():
      if ut1==ut2!=key :
            amt=result*10
            print('YOU LANDED ON A UTILITY, RENT= 10 TIMES NO. ON DICE ')
      elif ut1!=key or ut2!=key:
            amt=result*4
            print('YOU LANDED ON A UTILITY, RENT= 4 TIMES NO. ON DICE ')
      else:
            amt=rent[parti[key][1]]
      while True:
            print('Current Balance in Account: M'+str(parti[key][0]))
            print('1. Pay Rent:','M'+str(amt),'to',globals()[ownership])
            print('2. Declare Bankrupcy')
            no=int(input("Descision(1-2): "))
            if no==1:
                  parti[key][0]-=amt
                  parti[globals()[ownership]][0]+=amt
                  print('Rent Payed')
                  break
            elif no==2:
                  print("Paying",globals()[ownership]," of Remaining Funds ")
                  print(key,'is bankrupt')
                  parti[globals()[ownership]][0]+=parti[key][0]
                  keys.remove(key)
                  del parti[key]
                  break
            else:print("INVALID REQUEST")

def buy_propt():
      global ut1
      global ut2
      amt=rent[parti[key][1]]
      while True:
            print()
            print('Current Balance in Account: M'+str(parti[key][0]))
            print('1. Buy property for','M'+str(amt))
            print("2. Don't Buy the property")
            no=int(input("Descision(1-2): "))
            if no==1:
                  parti[key][0]-=amt
                  if parti[key][0]>0:
                        rent[parti[key][1]]=str(int(rent[parti[key][1]]/10))+' '
                        globals()[ownership]=key
                        if ownership=='o5'or ownership=='o15'or ownership=='o25'or ownership=='o35':
                              black_dict[key]+=[parti[key][1]]
                        elif ownership=='o12':
                              ut1=key
                        elif ownership=='o28':ut2=key
                        print('Property bought!!')
                        break
                  else:print("INSUFFICIENT FUNDS")
            elif no==2:
                  break
            else:print("INVALID REQUEST")
     
def turn():
      for x in (0,len(rent)-1):
          if type(rent[x])==str:
              if len(rent[x])==4:
                  rent[x]=str(int(rent[x]))
      global result 
      global ownership
      if result_flag==0:
            print(key+"'s Turn")
            while True:
                  print("1. Roll dice ")
                  print("2. Build apartments/hotels")
                  print('3. Trade')
                  no=int(input("Decision(1-3) "))
                  if no==2:
                        apt_hot()
                        break
                  elif no==1:
                        aposition='a'+ str(parti[key][1])
                        if aposition=='a0':
                              a0.remove(key[0]+key[1])
                              result=randint(2,12)
                              print()
                              print("DICE RESULT: ",str(result))
                              parti[key][1]+=result
                              break
                        else:
                              globals()[aposition]='[]'
                              result=randint(2,12)
                              print()
                              print("DICE RESULT: ",str(result))
                              parti[key][1]+=result
                              break
                  elif no==3:
                        if parti[key][1]!=0:
                              prnt_board()
                              trade()
                        else:print("You can't trade on your first turn")
                  else:print('INVALID REQUEST')
      
      
      if o1==o3==key and key!='UNOWNED':
            yellow1=key
      elif o6==o8==o9==key and key!='UNOWNED':
            cyan1=key
      elif o11==o13==o14==key and key!='UNOWNED':
            pink=key
      elif o16==o18==o19==key and key!='UNOWNED':
            cyan2=key
      elif o21==o23==o24==key and key!='UNOWNED':
            red=key
      elif o26==o27==o29==key and key!='UNOWNED':
            yellow2=key
      elif o31==o32==o34==key and key!='UNOWNED':
            green=key
      elif o37==o39==key and key!='UNOWNED':
            blue=key
      elif len(black_dict[key])>0:
            for x in black_dict[key]:
                  rent[x]=str(20*len(black_dict[key]))+' '
      
      if parti[key][1]>39:
            parti[key][1]-=40
            parti[key][0]+=200
      
      bposition='a'+ str(parti[key][1])

      globals()[bposition]=key[0]+key[1]
      ownership='o'+ str(parti[key][1])
      
      prnt_board()
      while True:
            if globals()[ownership]=='UNOWNED':
                        buy_propt()
                        break

            elif globals()[ownership]=='':
                  break



            elif globals()[ownership]==' ':
                  chance()
                  ownership='o'+ str(parti[key][1])
                  if chance_no in[2,3,4,5,6,9,13]:
                        print(parti)
                        if globals()[ownership]=='UNOWNED':
                              buy_propt()
                              break
                              
                        elif globals()[ownership]==key:
                              print('You landed on your property')
                              break

                        else:
                              if chance_no in [4,5,6]:
                                    print('Property is owned therefore rent will be twice ')
                                    rent[parti[key][1]]*=2
                                    amt=rent[parti[key][1]]
                                    while True:
                                          print('Current Balance in Account: M'+str(parti[key][0]))
                                          print('1. Pay Rent:','M'+str(amt),'to',globals()[ownership])
                                          print('2. Declare Bankrupcy')
                                          no=int(input("Descision(1-2): "))
                                          if no==1:
                                                parti[key][0]-=amt
                                                parti[globals()[ownership]][0]+=amt
                                                print('Rent Payed')
                                                rent[parti[key][1]]/=2
                                                break
                                          elif no==2:
                                                print("Paying",globals()[ownership]," of Remaining Funds ")
                                                print(key,'is bankrupt')
                                                rent[parti[key][1]]/=2
                                                parti[globals()[ownership]][0]+=parti[key][0]
                                                keys.remove(key)
                                                del parti[key]
                                                break
                                          else:print("INVALID REQUEST")
                              elif chance_no in [2,3,9,13]:
                                    print("You Landed on someone else's property")
                                    pay_rent()
                                    break

                  else:break
                        
            elif globals()[ownership]=='  ':
                  community_chest()
                  break
            elif globals()[ownership]=='JAIL':
                  print()
                  print('GO TO JAIL!!!')
                  a10j=' '+key[0]+key[1]+' '
                  a30='[]'
                  parti[key][1]=101
                  jail_time[key]=3
                  print()
                  break

            elif globals()[ownership]=='TAXINGS':
                  amt=rent[parti[key][1]]
                  while True:
                        print('Current Balance in Account: M'+str(parti[key][0]))
                        print('1. Pay Tax of'+str(amt))
                        print('2. Declare bankrupcy')
                        no=int(input('Descision(1-2): '))
                        if no==1:
                              parti[key][0]-=amt
                              break
                        elif no==2:
                              print(parti[key][0],"has declared bankrupcy!!" )
                              keys.remove(key)
                              del parti[key]
                              break
                        else:
                              print("INVALID REQUEST")
                  break
                              
                              
                        
            elif globals()[ownership]==key:
                  print('Already owned!')
                  print('1. Build apartments/hotels')
                  print('2. End Turn')
                  no=int(input('Descision(1-2): '))
                  if no==1:
                        apt_hot()
                        break
                  else:break
                        
            else:
                  pay_rent()
                  
                  break

def jail_exit():
      while True:
            print(key+"'s Turn")
            print('1. Roll dice & Try your luck')
            print('2. Pay M50 and get out')
            print('3. Use Get out of jail free card')
            no=int(input('Descision(1-3): '))
            if no==1:
                  result1=randint(1,6)
                  result2=randint(1,6)
                  if result1==result2:
                        print('DICE1: '+str(result1))
                        print('DICE2: '+str(result2))
                        print('YOU ARE OUT OF JAIL')
                        result=result1+result2
                        result_flag=1
                        parti[key][1]=result+10
                        print(parti[key][1])
                        a10j='JAIL'
                        jail_time[key]=0
                        turn()
                        break
                  else:
                        print('DICE1: '+str(result1))
                        print('DICE2: '+str(result2))
                        print('Still in jail :( ')
                        jail_time[key]-=1
                        break
            elif no==2:
                  parti[key][0]-=50
                  print('YOU ARE OUT OF JAIL')
                  jail_time[key]=0
                  parti[key][1]=10
                  a10=key[0]+key[1]
                  break
            elif no==3:
                  if parti[key][2]==0:print("You don't have a Get Out of jail free card")
                  else:
                        print('YOU ARE OUT OF JAIL')
                        jail_time[key]=0
                        parti[key][2]-=1
                        parti[key][1]=10
                        a10=key[0]+key[1]
                        break
                        

            else:print('INVALID REQUEST')
prnt_board()
while True:
      if len(keys)==1:
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print(Back.RED+keys[0],'HAS WON THE GAME!! :D',Back.RESET)
             print(Back.RED+'THANKS FOR PLAYING',Back.RESET)
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             print()
             break
      for key in keys:
            print()
            if jail_time[key]<=3 and jail_time[key]!=0:
                  a10j=' '+key[0]+key[1]+' '
                  prnt_board()
                  jail_exit()
                  
            else:
                  turn()
