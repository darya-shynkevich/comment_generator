"""initial commit

Revision ID: 2c0516590c18
Revises:
Create Date: 2024-11-11 13:59:36.474238

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2c0516590c18"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "comment",
        sa.Column(
            "id",
            sa.UUID(),
            nullable=False,
            primary_key=True,
            server_default=sa.text('gen_random_uuid()'),
        ),
        sa.Column("title", sa.VARCHAR(length=255), nullable=False),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.PrimaryKeyConstraint("id", name="comments_pkey"),
    )


def downgrade() -> None:
    op.drop_table("comment")
