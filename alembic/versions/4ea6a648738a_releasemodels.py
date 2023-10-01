"""ReleaseModels

Revision ID: 4ea6a648738a
Revises: 4efc8579bfde
Create Date: 2023-10-01 16:02:56.313278

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ea6a648738a'
down_revision: Union[str, None] = '4efc8579bfde'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('question', sa.String(), nullable=True))
    op.add_column('questions', sa.Column('answer', sa.String(), nullable=True))
    op.drop_column('questions', 'answer_text')
    op.drop_column('questions', 'question_text')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('question_text', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('questions', sa.Column('answer_text', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('questions', 'answer')
    op.drop_column('questions', 'question')
    # ### end Alembic commands ###
