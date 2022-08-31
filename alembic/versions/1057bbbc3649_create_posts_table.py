"""create posts table

Revision ID: 1057bbbc3649
Revises: 
Create Date: 2022-08-30 21:02:55.256011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1057bbbc3649'
down_revision = None
branch_labels = None
depends_on = None

# alembic docs: DDL internals
def upgrade() -> None:
    op.create_table('posts', sa.Column("id", sa.Integer(), nullable=False, primary_key=True), sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
