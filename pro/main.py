import models
from models import Session
user = models.User(id=1,username="admin",password="123456")

session = Session()
# session.add(user)
# session.commit()

results = session.query(models.User).all()
for row in results:
    print(row.id, row.username,row.password)