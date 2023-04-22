
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberry-test-f7ea7-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
ref = db.reference('/mfrc')
print(ref.get())

ref.set(
    {
    'id': '112233'
    }
)
