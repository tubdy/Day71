import hashlib
def get_gravatar_url(email, size=100):
    email_encoded = email.lower().strip().encode('utf-8')
    gravatar_hash = hashlib.md5(email_encoded).hexdigest()
    return f"https://www.gravatar.com/avatar/{gravatar_hash}?s={size}&d=retro"
print(get_gravatar_url("purves@gmail.com"))