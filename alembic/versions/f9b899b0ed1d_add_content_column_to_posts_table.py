"""add content column to posts table

Revision ID: f9b899b0ed1d
Revises: 1057bbbc3649
Create Date: 2022-08-30 21:15:57.711159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9b899b0ed1d'
down_revision = '1057bbbc3649'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
