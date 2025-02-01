"""Add columns to users table

Revision ID: c12cd6974c23
Revises: 435b3f9fcf22
Create Date: 2025-02-01 03:10:55.756433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c12cd6974c23'
down_revision: Union[str, None] = '435b3f9fcf22'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('role', sa.Integer, nullable=False))
    op.add_column('users', sa.Column('email_verified_at', sa.DateTime, nullable=True))
    pass

def downgrade() -> None:
    op.drop_column('users', 'role')
    op.drop_column('users', 'email_verified_at')
    pass
