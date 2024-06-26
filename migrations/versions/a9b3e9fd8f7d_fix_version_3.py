"""fix version #3

Revision ID: a9b3e9fd8f7d
Revises: 4e151088ee6f
Create Date: 2024-06-09 12:49:55.623297

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9b3e9fd8f7d'
down_revision: Union[str, None] = '4e151088ee6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hashed_password', sa.String(), nullable=False))
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('user', 'hashed_password')
    # ### end Alembic commands ###
