import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognitionrealtime-5fb5b-default-rtdb.firebaseio.com/"
})

ref = db.reference('Criminals')pip install firebase-admin twilio

data = {
    "CR_26":
        {
            "arrested_year": 1977,
            "camera_no": 3,
            "crime":"Bomb Attack",
            "last_seen_time": "2002-12-11 16:47:24",
            "name": "Osama Bin laden",
            "total_crime": 7,
            "years_in_jail": 4

        },
    "CR_33":
        {
            "arrested_year": 2000,
            "camera_no": 11,
            "crime": "German Blast",
            "last_seen_time": "2010-9-9 12:05:10",
            "name": "Iqbal Bhatkal ",
            "total_crime": 3,
            "years_in_jail": 2

        },
    "CR_41":
        {
            "arrested_year": 1980,
            "camera_no": 33,
            "crime": "Domestic Terrorism",
            "last_seen_time": "1990-3-10 03:10:08",
            "name": "nasser",
            "total_crime": 8,
            "years_in_jail": 6

        },

}
for key, value in data.items():
    ref.child(key).set(value)