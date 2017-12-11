from ReplayRetriever import db
import enum

class Matches(db.Model):
    """Main table for replay info."""
    replayID = db.Column(db.Integer, primary_key=True)

    direID = db.Column(db.Integer, index=True)
    radiantID = db.Column(db.Integer, index=True)
    leagueID = db.Column(db.Integer, index=True)

    startTime = db.Column(db.Integer)
    
    radiantWin = db.Column(db.Boolean)

class MatchRetrieval(db.Model):
    """Main table for replay info."""
    replayID = db.Column(db.Integer, primary_key=True)

    clusterID = db.Column(db.Integer)
    salt = db.Column(db.Integer)
    downloadAttempts = db.Column(db.Integer)

class PlayerHeroes(db.Model):
    replayID = db.Column(db.Integer, primary_key=True)
    side = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, primary_key=True)

    playerID = db.Column(db.Integer, index=True)
    hero = db.Column(db.String, index=True)

    idPick = db.Column(db.Boolean)
