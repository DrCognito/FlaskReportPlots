"""empty message

Revision ID: 7edba2483aed
Revises: 8615c1cf6161
Create Date: 2017-12-14 16:08:28.054578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7edba2483aed'
down_revision = '8615c1cf6161'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team_status',
    sa.Column('teamID', sa.Integer(), nullable=False),
    sa.Column('teamName', sa.String(), nullable=False),
    sa.Column('validTimeStart', sa.DateTime(), nullable=True),
    sa.Column('validTimeEnd', sa.DateTime(), nullable=True),
    sa.Column('lastLeagueUpdate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('teamID', 'teamName')
    )
    op.create_table('team_leagues',
    sa.Column('teamID', sa.Integer(), nullable=False),
    sa.Column('leagueID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['teamID'], ['team_status.teamID'], ),
    sa.PrimaryKeyConstraint('teamID', 'leagueID')
    )
    op.drop_index('ix_matches_direID', table_name='matches')
    op.drop_index('ix_matches_leagueID', table_name='matches')
    op.drop_index('ix_matches_radiantID', table_name='matches')
    op.create_index(op.f('ix_matches_direID'), 'matches', ['direID'], unique=False)
    op.create_index(op.f('ix_matches_leagueID'), 'matches', ['leagueID'], unique=False)
    op.create_index(op.f('ix_matches_radiantID'), 'matches', ['radiantID'], unique=False)
    op.drop_index('ix_player_heroes_playerID', table_name='player_heroes')
    op.create_index(op.f('ix_player_heroes_playerID'), 'player_heroes', ['playerID'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_player_heroes_playerID'), table_name='player_heroes')
    op.drop_index(op.f('ix_matches_radiantID'), table_name='matches')
    op.drop_index(op.f('ix_matches_leagueID'), table_name='matches')
    op.drop_index(op.f('ix_matches_direID'), table_name='matches')
    op.create_index('ix_player_heroes_playerID', 'player_heroes', ['playerID'], unique=False)
    op.create_index('ix_matches_radiantID', 'matches', ['radiantID'], unique=False)
    op.create_index('ix_matches_leagueID', 'matches', ['leagueID'], unique=False)
    op.create_index('ix_matches_direID', 'matches', ['direID'], unique=False)
    op.drop_table('team_leagues')
    op.drop_table('team_status')
    # ### end Alembic commands ###