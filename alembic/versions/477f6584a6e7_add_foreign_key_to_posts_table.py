"""add foreign key to posts table

Revision ID: 477f6584a6e7
Revises: b8fac7d6da96
Create Date: 2022-08-30 21:36:35.308916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '477f6584a6e7'
down_revision = 'b8fac7d6da96'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users',
    local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')

    pass
