from __future__ import print_function
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import warnings
import csv
warnings.filterwarnings('ignore')
print('''Bot:
Hi! How may I help you today?:''')
a=0
while(a==0):
        print("1. What crop to grow?")
        print("2. What services we provide")
        print("3. Current prices of different crops?")
        print('''4. Need help?
   Contact Us''')
        print("5. Exit")
        ch=int(input("Please choose from above choices ->"))
        if(ch==1):
            PATH = 'C:\\Users\\ASUS\\Desktop\\hackathon\\Crop_recommendation.csv'
            df = pd.read_csv(PATH)
            df['label'].unique()
            features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
            target = df['label']
            labels = df['label']
# Splitting into train and test data
            from sklearn.model_selection import train_test_split
            Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)
#Random Forest
            from sklearn.ensemble import RandomForestClassifier
            RF = RandomForestClassifier(n_estimators=20, random_state=0)
            RF.fit(Xtrain,Ytrain)
            predicted_values = RF.predict(Xtest)
#Saving
            import pickle
            RF_pkl_filename = 'RandomForest.pkl'
            RF_Model_pkl = open(RF_pkl_filename, 'wb')
            pickle.dump(RF, RF_Model_pkl)
            RF_Model_pkl.close()
#MAKING PREDICTION
            N = int(input("Please enter ratio of Nitrogen content in your soil->"))
            P = int(input("Please enter ratio of Phosphorus content in your soil->"))
            K = int(input("Please enter ratio of Potassium content in your soil->"))
            temperature = float(input("Please enter temperature of your area in degree Celcius->"))
            humidity = float(input("Please enter relative humidity in % ->"))
            ph = float(input("Please enter ph value of your soil ->"))
            rainfall = float(input("Please enter rainfall amount in mm ->"))
            data = np.array([[N,P, K, temperature, humidity,ph, rainfall]])
            prediction = RF.predict(data)
            print("Based on your inputs, the most suitable crop for you is -> ",prediction)
            print("\n")
            con=input("Do You want any other help? (y/n) :")
            if con.lower()=='n':
                a=1
                print("Thank You! Have a Nice Day 🙂")
        elif(ch==2):
            print("Bot: Sorry but we are still in development")
            print("\n")
            con=input("Do You want any other help? (y/n) :")
            if con.lower()=='n':
                a=1
                print("Thank You! Have a Nice Day 🙂")
        elif(ch==3):
            import mysql.connector

            d = input("Enter your district in Punjab->")
            c = input("Enter Your Product->")

            try:
                mycon = mysql.connector.connect(user="root", password="bhavya09102005", database="crop")
                cursor = mycon.cursor()
                cursor.execute("SELECT Market, `Min Price`, `Max Price`, `Modal Price` FROM cropprice WHERE District = %s AND Commodity = %s", (d, c))

                records = cursor.fetchall()
                if not records:
                    print("No records found for the given district and product.")
                else:
                    for row in records:
                        print("Market->",row[0],"\n","Min Price->",row[1],"\n","Max Price->",row[2],"\n","Modal Price->",row[3])
            except mysql.connector.Error as e:
                print("Error while executing MySQL query:", e)
            finally:
                if mycon.is_connected():
                    cursor.close()
                    mycon.close()

            print("\n")
            con=input("Do You want any other help? (y/n) :")
            if con.lower()=='n':
                a=1
                print("Thank You! Have a Nice Day 🙂")
        
        elif(ch==4):
            print('''Bot: 
        Email: help.fcube@gmail.com
        Phone: 1234567890''')
            print("\n")
            con=input("Do You want any other help? (y/n) :")
            if con.lower()=='n':
                a=1
                print("Thank You! Have a Nice Day 🙂")
        elif(ch==5):
                print("Thank You! Have a Nice Day 🙂")
                a=1
        else:
                print("Invalid choice try again.")
       