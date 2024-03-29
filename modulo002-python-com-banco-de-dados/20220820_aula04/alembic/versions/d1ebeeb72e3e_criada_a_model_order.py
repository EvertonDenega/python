"""Criada a model Order

Revision ID: d1ebeeb72e3e
Revises: 9b4f748f696e
Create Date: 2022-08-20 17:38:56.875236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1ebeeb72e3e'
down_revision = '9b4f748f696e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['tb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_orders')
    # ### end Alembic commands ###
