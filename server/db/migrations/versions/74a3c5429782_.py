"""empty message

Revision ID: 74a3c5429782
Revises: d8b433f4b38c
Create Date: 2018-12-05 23:41:54.595368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74a3c5429782'
down_revision = 'd8b433f4b38c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=40), nullable=False),
    sa.Column('position', sa.VARCHAR(length=40), nullable=False),
    sa.Column('employment_date', sa.DateTime(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=False),
    sa.Column('chief', sa.Integer(), nullable=False),
    sa.Column('login', sa.VARCHAR(length=40), nullable=False),
    sa.Column('pwd', sa.VARCHAR(length=80), nullable=False),
    sa.Column('user_pic', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###
