""" create foreignkeys and relationships in  tables

Revision ID: afbf41009fa5
Revises: 77ef04c4350e
Create Date: 2024-02-13 10:55:01.158847

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'afbf41009fa5'
down_revision: Union[str, None] = '77ef04c4350e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('doctor_id', sa.Integer(), nullable=False))
    op.create_foreign_key('account_doctor_fk', 'account', 'doctor', ['doctor_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.add_column('certificate', sa.Column('doctor_id', sa.Integer(), nullable=False))
    op.add_column('certificate', sa.Column('creater_id', sa.Integer(), nullable=False))
    op.create_foreign_key('cretificate_creater_id', 'certificate', 'account', ['creater_id'], ['id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key('cretificate_doctor_id', 'certificate', 'doctor', ['doctor_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.add_column('chat', sa.Column('doctor_id', sa.Integer(), nullable=True))
    op.add_column('chat', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('chat_user_fk', 'chat', 'user', ['user_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.create_foreign_key('chat_doctor_fk', 'chat', 'doctor', ['doctor_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.add_column('chatuser', sa.Column('chat_id', sa.Integer(), nullable=False))
    op.create_foreign_key('chatuser_chat_fk', 'chatuser', 'chat', ['chat_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.add_column('diagnosis', sa.Column('doctor_id', sa.Integer(), nullable=False))
    op.create_foreign_key('diagnosis_doc_fk', 'diagnosis', 'doctor', ['doctor_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.add_column('feedback', sa.Column('doctor_id', sa.Integer(), nullable=False))
    op.add_column('feedback', sa.Column('chatuser_id', sa.Integer(), nullable=False))
    op.add_column('feedback', sa.Column('creater_id', sa.Integer(), nullable=False))
    op.create_foreign_key('feedback_doctor_fk', 'feedback', 'doctor', ['doctor_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.create_foreign_key(None, 'feedback', 'chatuser', ['chatuser_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.create_foreign_key('feedback_creater_fk', 'feedback', 'account', ['creater_id'], ['id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.add_column('message', sa.Column('chatuser_id', sa.Integer(), nullable=False))
    op.add_column('message', sa.Column('creater_id', sa.Integer(), nullable=False))
    op.create_foreign_key('message_creater_id', 'message', 'account', ['creater_id'], ['id'], onupdate='RESTRICT', ondelete='RESTRICT')
    op.create_foreign_key(None, 'message', 'chatuser', ['chatuser_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.add_column('messagestatus', sa.Column('chatuser_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'messagestatus', 'chatuser', ['chatuser_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.add_column('rating', sa.Column('chat_id', sa.Integer(), nullable=False))
    op.add_column('rating', sa.Column('doctor_id', sa.Integer(), nullable=False))
    op.add_column('rating', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('rating_user_fk', 'rating', 'user', ['user_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.create_foreign_key('rating_doctor_fk', 'rating', 'doctor', ['doctor_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    op.create_foreign_key('rating_chat_fk', 'rating', 'chat', ['chat_id'], ['id'], onupdate='CASCADE', ondelete='RESTRICT')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('rating_chat_fk', 'rating', type_='foreignkey')
    op.drop_constraint('rating_doctor_fk', 'rating', type_='foreignkey')
    op.drop_constraint('rating_user_fk', 'rating', type_='foreignkey')
    op.drop_column('rating', 'user_id')
    op.drop_column('rating', 'doctor_id')
    op.drop_column('rating', 'chat_id')
    op.drop_constraint(None, 'messagestatus', type_='foreignkey')
    op.drop_column('messagestatus', 'chatuser_id')
    op.drop_constraint(None, 'message', type_='foreignkey')
    op.drop_constraint('message_creater_id', 'message', type_='foreignkey')
    op.drop_column('message', 'creater_id')
    op.drop_column('message', 'chatuser_id')
    op.drop_constraint('feedback_creater_fk', 'feedback', type_='foreignkey')
    op.drop_constraint(None, 'feedback', type_='foreignkey')
    op.drop_constraint('feedback_doctor_fk', 'feedback', type_='foreignkey')
    op.drop_column('feedback', 'creater_id')
    op.drop_column('feedback', 'chatuser_id')
    op.drop_column('feedback', 'doctor_id')
    op.drop_constraint('diagnosis_doc_fk', 'diagnosis', type_='foreignkey')
    op.drop_column('diagnosis', 'doctor_id')
    op.drop_constraint('chatuser_chat_fk', 'chatuser', type_='foreignkey')
    op.drop_column('chatuser', 'chat_id')
    op.drop_constraint('chat_doctor_fk', 'chat', type_='foreignkey')
    op.drop_constraint('chat_user_fk', 'chat', type_='foreignkey')
    op.drop_column('chat', 'user_id')
    op.drop_column('chat', 'doctor_id')
    op.drop_constraint('cretificate_doctor_id', 'certificate', type_='foreignkey')
    op.drop_constraint('cretificate_creater_id', 'certificate', type_='foreignkey')
    op.drop_column('certificate', 'creater_id')
    op.drop_column('certificate', 'doctor_id')
    op.drop_constraint('account_doctor_fk', 'account', type_='foreignkey')
    op.drop_column('account', 'doctor_id')
    # ### end Alembic commands ###