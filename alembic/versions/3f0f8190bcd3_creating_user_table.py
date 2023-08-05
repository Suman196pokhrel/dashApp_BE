"""creating User table

Revision ID: 3f0f8190bcd3
Revises: 
Create Date: 2023-08-05 15:00:52.067579

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f0f8190bcd3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',

    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
    sa.Column('fName',sa.String(), nullable=False, unique=False),
    sa.Column('lName',sa.String(), nullable=False, unique=False),
    sa.Column('email',sa.String(), nullable=False, unique=True),
    sa.Column('dob',sa.Date(), nullable=False, unique=False),
    sa.Column('mobileNum',sa.String(), nullable=False, unique=True),
    sa.Column('password',sa.String(), nullable=False, unique=False),
    sa.Column('createdAt',sa.TIMESTAMP(timezone=True), nullable=False, unique=False),
    
    
    )


def downgrade() -> None:
    op.drop_table('users')
