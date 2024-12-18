"""lagt till tabeller och seed data

Revision ID: b7d78d2e99f1
Revises: 
Create Date: 2024-09-01 11:51:44.092313

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b7d78d2e99f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('persons', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('personnummer',
               existing_type=mysql.VARCHAR(length=12),
               nullable=False)
        batch_op.alter_column('city',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('country',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('profession',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('phone_number',
               existing_type=mysql.VARCHAR(length=15),
               nullable=False)
        batch_op.create_unique_constraint(None, ['personnummer'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('persons', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('phone_number',
               existing_type=mysql.VARCHAR(length=15),
               nullable=True)
        batch_op.alter_column('profession',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('country',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('city',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('personnummer',
               existing_type=mysql.VARCHAR(length=12),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###
