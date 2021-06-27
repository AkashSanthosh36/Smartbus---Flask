"""bus table

Revision ID: c6c0dfe0dce4
Revises: f072044e4eb6
Create Date: 2019-12-25 07:54:26.882861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6c0dfe0dce4'
down_revision = 'f072044e4eb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bus',
    sa.Column('bid', sa.Integer(), nullable=False),
    sa.Column('tname', sa.String(length=100), nullable=True),
    sa.Column('max_seats', sa.Integer(), nullable=True),
    sa.Column('type_ac', sa.String(length=10), nullable=True),
    sa.Column('type_sleeper', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('bid')
    )
    op.create_index(op.f('ix_bus_tname'), 'bus', ['tname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bus_tname'), table_name='bus')
    op.drop_table('bus')
    # ### end Alembic commands ###
