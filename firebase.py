import pyrebase
import firebase_admin
from firebase_admin import credentials

config = {
  "apiKey": "AAAATN-ZpOw:APA91bFdXet6yxNzAnifpZ4resbb66YERmgP-vAADNA_Knn2bHLVO-aDeQQuL9q2ibMD9PYP-Hyk3-TaKPiZKZiFlC-SiJWY_bBliNq-AoyoiPM9KVvmuk-uve4-zKwAntbJTEVnblOQ",
  "authDomain": "motion-sensor-39267.firebaseapp.com",
  "databaseURL": "https://motion-sensor-39267.firebaseio.com",
  "storageBucket": "motion-sensor-39267.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
db.child("users").child("Morty")

data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)
