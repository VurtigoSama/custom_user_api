"""Add interest table

Revision ID: 76b0b1fc865a
Revises: acc063010021
Create Date: 2022-05-13 08:02:27.571699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76b0b1fc865a'
down_revision = 'acc063010021'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('interests', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default='now()', nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_interest_id'), 'interest', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_interest_id'), table_name='interest')
    op.drop_table('interest')
    # ### end Alembic commands ###