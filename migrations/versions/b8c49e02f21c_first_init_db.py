"""first init db

Revision ID: b8c49e02f21c
Revises: 
Create Date: 2017-09-03 14:10:15.710000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8c49e02f21c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('verify', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('erecord',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.Column('random_id', sa.Integer(), nullable=True),
    sa.Column('user', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.Column('problem', sa.Text(), nullable=True),
    sa.Column('ele_type', sa.String(length=64), nullable=True),
    sa.Column('solve', sa.Boolean(), nullable=True),
    sa.Column('mender', sa.String(length=64), nullable=True),
    sa.Column('verify', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('random_id')
    )
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.Column('random_id', sa.Integer(), nullable=True),
    sa.Column('user', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.Column('problem', sa.Text(), nullable=True),
    sa.Column('computer_type', sa.String(length=64), nullable=True),
    sa.Column('computer_password', sa.String(length=64), nullable=True),
    sa.Column('split', sa.Boolean(), nullable=True),
    sa.Column('solve', sa.Boolean(), nullable=True),
    sa.Column('mender', sa.String(length=64), nullable=True),
    sa.Column('verify', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('random_id')
    )
    op.create_table('unid',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('random_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('random_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('body_html', sa.Text(), nullable=True),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categorys.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('articles')
    op.drop_table('users')
    op.drop_table('unid')
    op.drop_table('record')
    op.drop_table('erecord')
    op.drop_table('comment')
    op.drop_table('categorys')
    # ### end Alembic commands ###
