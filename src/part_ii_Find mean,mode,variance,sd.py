# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:48:32 2020
 
@author: (Syahirah) 
    (Nadhirah) 
    	    (Hashim)
"""
import numpy 
import datetime 
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
 
#######################################
 
currentDT = datetime.datetime.now()
print ("\n\t\t\t   ",currentDT.strftime("%a-%Y-%m-%d %H:%M:%S"))
print("\t\t\t____________________________________")
 
 
while(True):
        
    print("\n\t\t   Descriptive Analysis and Display Data Section ")
    print("\t\t\t____________________________________")
    print("\n\t\t\t1. Calculate min,max,mode,mean ")
    print("\t\t\t2. Calculate varience and standard devision")
    print("\t\t\t3. Display graph")
    print("\t\t\t4. Exit");
    choice= int(input ("\t\t\t\t       >Enter choice :") )
    
    if choice==1: #Calculate min,max,mode,mean
        list1 = [23.8,21.4,33.7,20.3,26.9]
        list2 = [1294,1195,1539,1298,1880]
        list3 = [6332,6866,7519,7703,9069.5]
        
        #Validation for mode. If every data has same frequency,
        #Mode is not existed
        for n in list1:
            if list1.count(n)==1:
                a=0
        for n in list2:
            if list2.count(n)==1:
                b=0
        for n in list3:
            if list3.count(n)==1:
                c=0
        #Calculate mean
        bmi = numpy.mean(list1)
        bmr = numpy.mean(list2)
        calories = numpy.mean(list3)
        
        #Calculate mode
        Bmi = stats.mode(list1)
        Bmr = stats.mode(list2)
        Calories = stats.mode(list3)
        
        print ("\n\t\t\tmin value for BMI : ", min(list1))
        print ("\t\t\tmax value for BMI : ", max(list1))
        print ("\t\t\tmean value for BMI : ", bmi)
        if a==0:
            print("\t\t\tmode value for BMI : Not existed ")
        else :
            print ("\n\tmode value for BMI : ", Bmi)    
        
        print ("\n\t\t\tmin value for BMR : ", min(list2))
        print ("\t\t\tmax value for BMR : ", max(list2))
        print ("\t\t\tmean value for BMR : ", bmr)
        if b==0:
            print("\t\t\tmode value for BMR : Not existed ")
        else :
            print ("\tmode value for BMR : ", Bmr)
            
        print ("\n\t\t\tmin value for calories : ", min(list3))              
        print ("\t\t\tmax value for calories : ", max(list3))
        print ("\t\t\tmean value for calories : ", calories)
        if c==0:
            print("\t\t\tmode value for calories : Not existed ")
        else :
            print ("\tmode value for calories : ", Calories)
        
 
        
        print ("\t____________________________________________________________________________________")
               
    elif choice==2:
        vbmi=[23.8,21.4,33.7,20.3,26.9]
        vbmr=[1294,1195,1539,1298,1880]
        vcalo=[6332,6866,7519,7703,9069.5]
        
        #Calculate variance
        x=numpy.var(vbmi)
        y=numpy.var(vbmr)
        z=numpy.var(vcalo)
        #Calculate standard deviation
        X=numpy.std(vbmi)
        Y=numpy.std(vbmr)
        Z=numpy.std(vcalo)
        
        print("\n\t\t\tThe Variance for BMI : ",x)
        print("\t\t\tThe Standard Deviation for BMI : ",X)
        
        print("\n\t\t\tThe Variance for BMR : ",y)
        print("\t\t\tThe Standard Deviation for BMR : ",Y)
        
        print("\n\t\t\tThe Variance for CALORIES : ",z)
        print("\t\t\tThe Standard Deviation for CALORIES : ",Z)
        
        print("\n")
        
        print ("\t_____________________________________________________________________________________")
                
    elif choice==3:
        data = [[23.8,21.4,33.7,20.3,26.9],
                [1294,1195,1539,1298,1880],
                [9069.5,7703,6866,6332,7519]]
        name = ["Sin Yee","Sakinah","Nadhirah","Syahirah","Hashim"]
        x = np.arange(5)
        
        
        plt.subplot(3,1,1)
        bmi=plt.bar(x,data[0], color='b',width=0.5)
        plt.ylabel('BMI')
        plt.title('Graph Calories, Body Mass Index and Basal Metabolic Rate')
        plt.xticks([],[])
        
        plt.subplot(3,1,2)
        bmr=plt.bar(x,data[1], color='r',width=0.5)
        plt.ylabel('BMR')
        plt.xticks([],[])
        
        plt.subplot(3,1,3)
        cal=plt.bar(x,data[2], color='g',width=0.5)
        plt.ylabel('Calories')
        plt.xticks(x,name,rotation='vertical')
        plt.show()
        
        print ("\t____________________________________________________________________________________")
        
    elif choice==4:
        break
        
    else:  
        print("\n\tInvalid choice. Enter 1-4.")
        print ("\t_____________________________________________________________________________________")
