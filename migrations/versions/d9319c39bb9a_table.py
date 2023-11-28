"""table 

Revision ID: d9319c39bb9a
Revises: 84641ed3020f
Create Date: 2023-11-28 09:56:29.251510

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9319c39bb9a'
down_revision: Union[str, None] = '84641ed3020f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'link_short', ['short_link'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'link_short', type_='unique')
    # ### end Alembic commands ###
