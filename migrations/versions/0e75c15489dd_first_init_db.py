"""first init db

Revision ID: 0e75c15489dd
Revises: b8c49e02f21c
Create Date: 2017-09-03 14:38:57.294000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e75c15489dd'
down_revision = 'b8c49e02f21c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('arrange',
    sa.Column('card_id', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('arrange', sa.String(length=64), nullable=True),
    sa.Column('term', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('card_id')
    )
    op.create_table('exam',
    sa.Column('Qid', sa.Integer(), nullable=False),
    sa.Column('Stem', sa.Text(), nullable=True),
    sa.Column('Select_1', sa.Text(), nullable=True),
    sa.Column('Select_2', sa.Text(), nullable=True),
    sa.Column('Select_3', sa.Text(), nullable=True),
    sa.Column('Select_4', sa.Text(), nullable=True),
    sa.Column('Select_Right', sa.Integer(), nullable=True),
    sa.Column('lv', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('Qid')
    )
    op.create_table('finance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('pm', sa.Integer(), nullable=True),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('tip', sa.Text(), nullable=True),
    sa.Column('remain', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info',
    sa.Column('card_id', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('tel', sa.String(length=64), nullable=True),
    sa.Column('arrangewant', sa.String(length=64), nullable=True),
    sa.Column('arrange', sa.String(length=64), nullable=True),
    sa.Column('premission', sa.Integer(), nullable=True),
    sa.Column('group', sa.Integer(), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('exam', sa.Text(), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('card_id')
    )
    op.create_table('marks_record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('time', sa.DATETIME(), nullable=True),
    sa.Column('Q_ID', sa.Integer(), nullable=True),
    sa.Column('Select', sa.String(length=64), nullable=True),
    sa.Column('mark', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('marks_record')
    op.drop_table('info')
    op.drop_table('finance')
    op.drop_table('exam')
    op.drop_table('arrange')
    # ### end Alembic commands ###
