"""empty message

Revision ID: 982791aeea88
Revises: 
Create Date: 2020-09-28 23:23:56.950456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '982791aeea88'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('status',
    sa.Column('id', sa.Float(), nullable=False),
    sa.Column('code', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('status')
    # ### end Alembic commands ###
