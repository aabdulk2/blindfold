"""empty message

Revision ID: 8b9f7eeacb09
Revises: 
Create Date: 2022-05-26 14:53:49.523929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b9f7eeacb09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=20), nullable=False),
    sa.Column('lastName', sa.String(length=20), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=1), nullable=False),
    sa.Column('preference', sa.String(length=1), nullable=False),
    sa.Column('bio', sa.String(length=600), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('matches',
    sa.Column('userid_Matched', sa.Integer(), nullable=False),
    sa.Column('userid_Matching', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('userid_Matched', 'userid_Matching')
    )
    op.create_table('Messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid_sent', sa.Integer(), nullable=False),
    sa.Column('userid_received', sa.Integer(), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['userid_sent'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Messages')
    op.drop_table('matches')
    op.drop_table('Users')
    # ### end Alembic commands ###