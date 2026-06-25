import hashlib
from flask import Flask
from dotenv import load_dotenv
import os
def get_gravatar_url(email, size=100):
    email_encoded = email.lower().strip().encode('utf-8')
    gravatar_hash = hashlib.md5(email_encoded).hexdigest()
    return f"https://www.gravatar.com/avatar/{gravatar_hash}?s={size}&d=retro"

#FLASK_SECRET_KEY='8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
#DATABASE_URL='sqlite:///posts.db'
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] =  os.environ.get('FLASK_KEY')

print(os.environ['FLASK_SECRET_KEY'])
print(os.environ['DATABASE_URL'])


