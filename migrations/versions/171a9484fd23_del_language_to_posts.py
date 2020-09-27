"""del language to posts

Revision ID: 171a9484fd23
Revises: cc2e657f22cf
Create Date: 2020-09-27 17:11:45.738177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '171a9484fd23'
down_revision = 'cc2e657f22cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.VARCHAR(length=5), nullable=True))
    # ### end Alembic commands ###
