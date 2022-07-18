from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # telling passlib what hashing algorithm we want to use - bcrypt in this case

def hash(password: str):
    return pwd_context.hash(password)
