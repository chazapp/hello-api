"""Initial Migration

Revision ID: 363623fe5f9c
Revises: 
Create Date: 2022-08-24 14:09:13.812009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '363623fe5f9c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=25), nullable=False),
    sa.Column('birthday', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
