import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/postgres"
db = SQLAlchemy(app)

class ClubsModel(db.Model):
    __tablename__ = 'epl'
    name = db.Column(db.String(40), primary_key=True)
    city = db.Column(db.String(40))
    coach = db.Column(db.String)
    captain = db.Column(db.String)
    kit = db.Column(db.String)
    sponsor = db.Column(db.String)

    def __init__(self, name, city, coach, captain, kit, sponsor):
        self.name = name
        self.city = city
        self.coach = coach
        self.captain = captain
        self.kit = kit
        self.sponsor = sponsor

@app.route('/', methods=['GET'])
def home():
    return '''<h1>2020/2021 English Premier League clubs database</h1>
<p>A prototype API for database of 2020/2021 EPL season clubs.</p>'''

@app.route('/api/v1/resources/clubs/epl', methods=['GET'])
def epl():
    clubs = ClubsModel.query.all()
    results = [
        {
            "name": club.name,
            "city": club.city,
            "coach": club.coach,
            "captain": club.captain,
            "kit": club.kit,
            "sponsor": club.sponsor
        } for club in clubs]
    return {"clubs": results}

if __name__ == '__main__':
     app.run()
