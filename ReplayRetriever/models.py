from ReplayRetriever import db
import enum


class Matches(db.Model):
    """Main table for replay info."""
    replayID = db.Column(db.Integer, primary_key=True)

    direID = db.Column(db.Integer)
    radiantID = db.Column(db.Integer)
    leagueID = db.Column(db.Integer)

    startTime = db.Column(db.DateTime)

    radiantWin = db.Column(db.Boolean)
    # Replay api retrieval attempts.
    retrievalAttempts = db.Column(db.Integer)


class TeamStatus(db.Model):
    """Table for storing last update for a team"""
    teamID = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String, primary_key=True)
    validTimeStart = db.Column(db.DateTime)
    validTimeEnd = db.Column(db.DateTime)
    lastLeagueUpdate = db.Column(db.DateTime)


class TeamLeagues(db.Model):
    """Table for assosciating leagues with teams."""
    teamID = db.Column(db.Integer, db.ForeignKey(TeamStatus.teamID),
                       primary_key=True)
    leagueID = db.Column(db.Integer, primary_key=True)


class MatchRetrieval(db.Model):
    """Table for replay retrieval information."""
    replayID = db.Column(db.Integer, db.ForeignKey(Matches.replayID),
                         primary_key=True)

    clusterID = db.Column(db.Integer)
    salt = db.Column(db.Integer)
    # Salt retrieval attempts
    retrievalAttempts = db.Column(db.Integer)
    # Replay download attempts.
    downloadAttempts = db.Column(db.Integer)


class PnBTeam(enum.Enum):
    """Number corresponds to the pickban team numbering which is radiant 0
    dire 1.
    """
    Radiant = 0
    Dire = 1


class PlayerHeroes(db.Model):
    replayID = db.Column(db.Integer, db.ForeignKey(Matches.replayID),
                         primary_key=True)
    side = db.Column(db.Enum(PnBTeam), primary_key=True)
    order = db.Column(db.Integer, primary_key=True)

    playerID = db.Column(db.Integer)
    hero = db.Column(db.String)

    idPick = db.Column(db.Boolean)
