"""Initial clean migration

Revision ID: 152b8bd023ed
Revises: 
Create Date: 2025-04-30 01:08:23.347615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '152b8bd023ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cab',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('make', sa.String(length=100), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('seating_capacity', sa.Integer(), nullable=False),
    sa.Column('ac', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('car',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('make', sa.String(length=50), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('year', sa.String(length=10), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('kilometers_driven', sa.String(length=20), nullable=True),
    sa.Column('fuel_type', sa.String(length=20), nullable=True),
    sa.Column('transmission', sa.String(length=20), nullable=True),
    sa.Column('color', sa.String(length=20), nullable=True),
    sa.Column('owner_number', sa.String(length=10), nullable=True),
    sa.Column('manufacturing_year', sa.String(length=10), nullable=True),
    sa.Column('registration_year', sa.String(length=10), nullable=True),
    sa.Column('registration_type', sa.String(length=50), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('seller_name', sa.String(length=100), nullable=True),
    sa.Column('seller_contact', sa.String(length=100), nullable=True),
    sa.Column('specifications', sa.Text(), nullable=True),
    sa.Column('features', sa.Text(), nullable=True),
    sa.Column('image_filenames', sa.Text(), nullable=True),
    sa.Column('last_updated', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cab_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=255), nullable=False),
    sa.Column('cab_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cab_id'], ['cab.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cab_image')
    op.drop_table('car')
    op.drop_table('cab')
    # ### end Alembic commands ###
