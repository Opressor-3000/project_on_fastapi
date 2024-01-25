"""create agency table migrations

Revision ID: 9b900de74df9
Revises: 1434c88c23f7
Create Date: 2024-01-19 14:04:00.259990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b900de74df9'
down_revision: Union[str, None] = '1434c88c23f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agency',
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('creater_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['creater_id'], ['permission.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agency')
    # ### end Alembic commands ###