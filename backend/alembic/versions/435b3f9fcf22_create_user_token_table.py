"""Create user_tokens table

Revision ID: 435b3f9fcf22
Revises: ffdbbc8c9084
Create Date: 2025-01-08 01:39:36.002742

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '435b3f9fcf22'
down_revision: Union[str, None] = 'ffdbbc8c9084'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user_tokens",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), unique=True),
        sa.Column("access_token", sa.String(255)),
        sa.Column("refresh_token", sa.String(255)),
        sa.Column("token_type", sa.Integer),
        sa.Column("expires_in", sa.Integer)
    )
    pass


def downgrade() -> None:
    op.drop_table("user_tokens")
    pass
