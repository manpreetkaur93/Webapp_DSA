"""Add is_celebrity column to Person model

Revision ID: f7fb13d9bc7a
Revises: 65385b356e9f
Create Date: 2024-09-02 00:06:32.224917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7fb13d9bc7a'
down_revision = '65385b356e9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('persons', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_celebrity', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('persons', schema=None) as batch_op:
        batch_op.drop_column('is_celebrity')

    # ### end Alembic commands ###
