"""create gender table migrations

Revision ID: 41eb561b3733
Revises: ec22ccc3dc54
Create Date: 2024-01-19 13:48:11.188169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41eb561b3733'
down_revision: Union[str, None] = 'ec22ccc3dc54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gender',
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('creater_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['creater_id'], ['permission.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('creater_id'),
    sa.UniqueConstraint('title')
    )
    op.add_column('permission', sa.Column('group_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'permission', 'group', ['group_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'permission', type_='foreignkey')
    op.drop_column('permission', 'group_id')
    op.drop_table('gender')
    # ### end Alembic commands ###