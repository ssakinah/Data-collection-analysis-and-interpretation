# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:11:05 2020

@author: Aqilah Syahirah, Sin Yee, Siti Sakinah
@question: part iv, CPT115 Assignment 2
"""
import datetime 
from os import system
import matplotlib.pyplot as plta
import matplotlib.pyplot as pltb
import matplotlib.pyplot as pltc
from scipy import stats
#######################################

currentDT = datetime.datetime.now()
print ("\n\t\t\t     ",currentDT.strftime("%a-%Y-%m-%d %H:%M:%S"))
print("\t\t\t____________________________________")


while(True):
        
    print("\n\t\t\t    Part IV: Regression Analysis  ")
    print("\t\t\t____________________________________")
    print("\n\t\t\t1. the correlation between calories \n\t\t\t   intake and weight of students\n ")
    print("\t\t\t2. the correlation between physical \n\t\t\t   activities and weight of students\n")
    print("\t\t\t3. the correlation between physical \n\t\t\t   activities and calorie intakes\n")
    print("\t\t\t4. Exit");
    choice= int(input ("\t\t\t\t       >Enter choice :") )
    
    if choice==1: 
        # the correlation between calories intake and weight of students
        xa = [9069.5, 7703, 6866, 6332, 7519]
        ya= [58, 50, 82, 54, 79]

        slope, intercept, r, p, std_err = stats.linregress(xa, ya)
        def myfunction1(xa):return slope * xa + intercept
        mymodel1 = list(map(myfunction1, xa))

        plta.title("Total calories intake vs Weight")
        plta.xlabel("Total calories intake (cal)")
        plta.ylabel("Weight (kg)")
        plta.scatter(xa, ya)
        plta.plot(xa, mymodel1)
        plta.show()
        print ("\t____________________________________________________________________________________")
               
    elif choice==2:
        # the correlation between physical activities and weight of students
        xb=[1,1,2,1,1]
        yb=[50,54,58,79,82]
    
        slope, intercept, r, p, std_err = stats.linregress(xb, yb)
        def myfunction2(xb):return slope * xb + intercept
        mymodel2 = list(map(myfunction2, xb))

        pltb.title("Physical activities vs Weight")
        pltb.xlabel("Physical activities (level)")
        pltb.ylabel("Weight (kg)")
        pltb.scatter(xb,yb)
        pltb.plot(xb, mymodel2)
        pltb.show()
        
        print ("\t_____________________________________________________________________________________")
                
    elif choice==3:
        # the correlation between physical activities and calorie intakes
        xc=[1,1,1,1,2]
        yc=[6332,6866,7519,7703,9069.5]

        slope, intercept, r, p, std_err = stats.linregress(xc, yc)
        def myfunction3(xc):return slope * xc + intercept
        mymodel3 = list(map(myfunction3, xc))

        pltc.title("Physical Activities vs Calorie Intakes")
        pltc.xlabel("Physical activities (level)")
        pltc.ylabel("Calorie Intakes")
        pltc.scatter(xc,yc)
        pltc.plot(xc, mymodel3)
        pltc.show()
        
        print ("\t____________________________________________________________________________________")
        
    elif choice==4:
        break
        
    else:  
        print("\n\tInvalid choice. Enter 1-4.")
        print ("\t_____________________________________________________________________________________")



    
