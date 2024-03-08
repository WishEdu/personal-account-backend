from backend import app
from backend.modules.database import cursor, db

app.run(debug=True)

cursor.close()
db.close()