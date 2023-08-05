from passlib.context import CryptContext
from ..settings import settings





pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")



def find_index_by_id(array, target_id):
    for index, obj in enumerate(array):
        if obj["id"] == target_id:
            return index
    return -1  

def get_hash(text: str):
    return pwd_context.hash(text)


def verify_hash(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



# ----------------------------------------------------------------------------------------------------------


