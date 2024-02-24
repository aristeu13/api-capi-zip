"""add table click

Revision ID: 38d48c01fdc2
Revises: bb402029887b
Create Date: 2024-02-24 09:23:43.978410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38d48c01fdc2'
down_revision: Union[str, None] = 'bb402029887b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('click',
    sa.Column('link_short_id', sa.String(), nullable=False),
    sa.Column('user_agend', sa.String(), nullable=False),
    sa.Column('ip', sa.String(), nullable=False),
    sa.Column('localization', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['link_short_id'], ['link_short.short_link'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('link_short_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('click')
    # ### end Alembic commands ###
