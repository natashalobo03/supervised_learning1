import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("traffic_analysis_dataset.csv")
weather_categories=["Clear","Rainy","Foggy","Cloudy"]
time_categories=["Morning","Afternoon","Evening","Night"]

weather_encoder=LabelEncoder()
time_encoder=LabelEncoder()

weather_encoder.fit(weather_categories)
time_encoder.fit(time_categories)

df['Weather Conditions']=weather_encoder.transform(df['Weather Conditions'])
df['Time of the Day']=time_encoder.transform(df['Time of the Day'])
X=df[["Vehicle Count","Average Speed (km/hr)","Weather Conditions","Time of the Day"]]
y=df["Accident Reported"].map({"No":0,"Yes":1})

X_train,X_text,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

vehicle_count=int(input("Enter the vehicle count:"))
avg_speed=int(input("Enter the average speed:"))
weather_raw=input("Enter the weather conditions(Rainy,Foggy,Cloudy,Clear):")
time_raw=input("Enter the time of the day(Morning ,Afternoon,Evening,Night):")

weather_encoded=weather_encoder.transform([weather_raw])[0]
time_encoded=time_encoder.transform([time_raw])[0]
input_data=np.array([[vehicle_count,avg_speed,weather_encoded,time_encoded]])
prediction=model.predict(input_data)
result="Accident Likely" if prediction[0]==1 else "No Accident"
print("Prediction Result:",result)