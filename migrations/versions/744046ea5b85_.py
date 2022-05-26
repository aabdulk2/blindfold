"""empty message

Revision ID: 744046ea5b85
Revises: abf589d5e904
Create Date: 2022-05-26 14:58:07.756000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '744046ea5b85'
down_revision = 'abf589d5e904'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'gender')
    op.drop_column('Users', 'preference')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('preference', sa.VARCHAR(length=1), autoincrement=False, nullable=False))
    op.add_column('Users', sa.Column('gender', sa.VARCHAR(length=1), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
