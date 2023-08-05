"""fix createdAt column

Revision ID: e42d742cdcd4
Revises: 3f0f8190bcd3
Create Date: 2023-08-05 15:35:24.646127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e42d742cdcd4'
down_revision: Union[str, None] = '3f0f8190bcd3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users','createdAt',server_default=sa.text('NOW()'))


def downgrade() -> None:
    pass
