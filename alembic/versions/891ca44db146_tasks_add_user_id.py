"""tasks_add_user_id

Revision ID: 891ca44db146
Revises: ecdb12c5cffe
Create Date: 2024-09-27 09:40:20.128560

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '891ca44db146'
down_revision: Union[str, None] = 'ecdb12c5cffe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Tasks', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Tasks', 'UserProfile', ['user_id'], ['id'])
    op.drop_column('Tasks', 'asd')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Tasks', sa.Column('asd', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'Tasks', type_='foreignkey')
    op.drop_column('Tasks', 'user_id')
    # ### end Alembic commands ###
