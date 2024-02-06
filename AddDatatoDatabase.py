
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://criminaleye-realtime-default-rtdb.firebaseio.com/"
})

ref = db.reference('Criminals')
# Jason
data = {
    "Barack Obama":
        {
            # "Key":"Value"
            "Name": "Barack Obama",
            "Crime": "Arson",
            "Gender": "Male",
            "Last Found": "USA",
            "Last Found Time":"01-01-2023 06:54:34"

        },
    "Dawood_Ibrahim":
        {
            # "Key":"Value"
            "Name": "Dawood Ibrahim",
            "Crime": "Mafia",
            "Gender": "Male",
            "Last Found": "Pakistan",
            "Last Found Time":"02-05-2012 00:12:30"

        },
    "Elon Musk":
        {
            # "Key":"Value"
            "Name": " Elon Musk",
            "Crime": "Cybercrime",
            "Gender": "Male",
            "Last Found": "Canada",
            "Last Found Time":"10-01-2022 04:11:34"

        },
    "Harsh":
        {
            # "Key":"Value"
            "Name": "Harsh Shelke",
            "Crime": "Fraud",
            "Gender": "Male",
            "Last Found": "India",
            "Last Found Time":"22-03-2023 19:12:10"

        },
    "Joe Biden":
        {
            # "Key":"Value"
            "Name": "Joe Biden",
            "Crime": "Corruption",
            "Gender": "Male",
            "Last Found": "USA",
            "Last Found Time":"23-06-2022 16:09:10"

        },
    "Keanu Reeves":
        {
            # "Key":"Value"
            "Name": "Keanu Reeves",
            "Crime": "Homicide",
            "Gender": "Male",
            "Last Found": "Australia",
            "Last Found Time":"06-11-2019 09:42:23"

        },
    "Meghraj":
        {
            # "Key":"Value"
            "Name": "Meghraj Padwal",
            "Crime": "Vandalism",
            "Gender": "Male",
            "Last Found": "India",
            "Last Found Time":"02-04-2023 15:03:30"

        },
    "Narendra Modi":
        {
            # "Key":"Value"
            "Name": "Narendra Modi",
            "Crime": "Treason",
            "Gender": "Male",
            "Last Found": "India",
            "Last Found Time": "12-03-2023 20:16:23"

        },
    "Shreyas":
        {
            # "Key":"Value"
            "Name": "Shreyas Revankar",
            "Crime": "Trafficking",
            "Gender": "Male",
            "Last Found": "India",
            "Lat_Found_Time": "09-04-2023 22:30:20"

        },
    "Sonal":
        {
            # "Key":"Value"
            "Name": "Sonal Sonarghare",
            "Crime": "Murder",
            "Gender": "Female",
            "Last Found": "India",
            "Last Found Time": "17-04-2023 15:30:09"

        },
    "Swapnil":
        {
            # "Key":"Value"
            "Name": "Swapnil Rathod",
            "Crime": "Terrorist",
            "Gender": "Male",
            "Last Found": "India",
            "Last Found Time": "10-04-2023 21:35:22"

        },
    "Tanvi":
        {
            # "Key":"Value"
            "Name": "Tanvi Panchal",
            "Crime": "Blackmail",
            "Gender": "Female",
            "Last Found": "India",
            "Last Found Time": "12-04-2023 23:25:11"

        },

    "Vijay Malya":
        {
            # "Key":"Value"
            "Name": "Vijay Malya",
            "Crime": "Money Laundering",
            "Gender": "Male",
            "Last Found": "UK",
            "Last Found Time": "13-07-2022 19:20:01"

        }
}

for key,value in data.items():
    # send data to specific directory child
    ref.child(key).set(value)

