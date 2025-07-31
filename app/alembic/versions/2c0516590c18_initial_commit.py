"""initial commit

Revision ID: 2c0516590c18
Revises:
Create Date: 2024-11-11 13:59:36.474238

"""
from typing import Sequence, Union

from alembic import op
import sqlmodel
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c0516590c18'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False, server_default=sa.text('gen_random_uuid()')),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('comment',
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('owner_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], name='comments_owner_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='comments_pkey')
    )


def downgrade() -> None:
    op.drop_table('comment')
    op.drop_table('user')
