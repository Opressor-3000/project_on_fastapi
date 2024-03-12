""" create all accountaccess, chat, chatuser tables

Revision ID: 010b33982654
Revises: 448fdfeba81a
Create Date: 2024-02-13 10:33:15.120753

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '010b33982654'
down_revision: Union[str, None] = '448fdfeba81a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accessaccount',
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('access_id', sa.Integer(), nullable=False),
    sa.Column('creater_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['access_id'], ['access.id'], name='accessaccount_access_id', onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], name='accessaccount_account_id', onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['creater_id'], ['account.id'], name='accessgroup_creater_fk', onupdate='RESTRICT', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account_id', 'access_id', name='access_account_uc')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accessaccount')
    # ### end Alembic commands ###