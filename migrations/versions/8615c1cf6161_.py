"""empty message

Revision ID: 8615c1cf6161
Revises: ecbf36aa175d
Create Date: 2017-12-14 15:29:17.519656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8615c1cf6161'
down_revision = 'ecbf36aa175d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('match_retrieval', sa.Column('retrievalAttempts', sa.Integer(), nullable=True))
    op.add_column('matches', sa.Column('retrievalAttempts', sa.Integer(), nullable=True))
    # op.create_index(op.f('ix_matches_direID'), 'matches', ['direID'], unique=False)
    # op.create_index(op.f('ix_matches_leagueID'), 'matches', ['leagueID'], unique=False)
    # op.create_index(op.f('ix_matches_radiantID'), 'matches', ['radiantID'], unique=False)
    # op.drop_index('ix_matches_direID', table_name='matches')
    # op.drop_index('ix_matches_leagueID', table_name='matches')
    # op.drop_index('ix_matches_radiantID', table_name='matches')
    # op.create_index(op.f('ix_player_heroes_playerID'), 'player_heroes', ['playerID'], unique=False)
    # op.drop_index('ix_player_heroes_playerID', table_name='player_heroes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_index('ix_player_heroes_playerID', 'player_heroes', ['playerID'], unique=False)
    # op.drop_index(op.f('ix_player_heroes_playerID'), table_name='player_heroes')
    # op.create_index('ix_matches_radiantID', 'matches', ['radiantID'], unique=False)
    # op.create_index('ix_matches_leagueID', 'matches', ['leagueID'], unique=False)
    # op.create_index('ix_matches_direID', 'matches', ['direID'], unique=False)
    # op.drop_index(op.f('ix_matches_radiantID'), table_name='matches')
    # op.drop_index(op.f('ix_matches_leagueID'), table_name='matches')
    # op.drop_index(op.f('ix_matches_direID'), table_name='matches')
    op.drop_column('matches', 'retrievalAttempts')
    op.drop_column('match_retrieval', 'retrievalAttempts')
    # ### end Alembic commands ###
