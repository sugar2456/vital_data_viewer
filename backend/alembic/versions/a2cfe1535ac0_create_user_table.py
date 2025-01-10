"""create user table

Revision ID: a2cfe1535ac0
Revises: 
Create Date: 2024-12-12 14:52:45.445676

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2cfe1535ac0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # user tableを作成
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String(255), index=True),
        sa.Column("email", sa.String(255), unique=True, index=True),
        sa.Column("hashed_password", sa.String(255)),
        sa.Column("fitbit_user_id", sa.String(255), unique=True, index=True),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # user tableを削除
    op.drop_table("users")
    pass
    # ### end Alembic commands ###
