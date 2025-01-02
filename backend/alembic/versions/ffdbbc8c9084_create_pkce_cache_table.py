"""create pkce_cache table

Revision ID: ffdbbc8c9084
Revises: a2cfe1535ac0
Create Date: 2024-12-30 13:00:22.586984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ffdbbc8c9084'
down_revision: Union[str, None] = 'a2cfe1535ac0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pkce_cache",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("email", sa.String(255), index=True),
        sa.Column("code_verifier", sa.String(255), nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("pkce_cache")
    pass
