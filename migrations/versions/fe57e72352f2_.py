"""empty message

Revision ID: fe57e72352f2
Revises: 
Create Date: 2021-04-08 02:59:48.279193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe57e72352f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('birth_year', sa.String(length=50), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('eye_color', sa.String(length=50), nullable=False),
    sa.Column('hair_color', sa.String(length=50), nullable=False),
    sa.Column('skin_color', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(length=50), nullable=False),
    sa.Column('diameter', sa.Float(), nullable=False),
    sa.Column('climate', sa.String(length=50), nullable=False),
    sa.Column('rotation_period', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('item_type', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    op.drop_table('user')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###