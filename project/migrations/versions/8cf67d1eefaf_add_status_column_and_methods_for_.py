"""Add status column and methods for confirming and cancelling the appointment

Revision ID: 8cf67d1eefaf
Revises: d86905783178
Create Date: 2025-03-31 00:11:59.872913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cf67d1eefaf'
down_revision = 'd86905783178'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointment', schema=None) as batch_op:
        # Add the 'status' column with a default value of 'pending' for existing rows
        batch_op.add_column(sa.Column('status', sa.String(length=20), nullable=False, server_default='pending'))

    # Remove the server_default after the column is added (optional)
    with op.batch_alter_table('appointment', schema=None) as batch_op:
        batch_op.alter_column('status', server_default=None)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointment', schema=None) as batch_op:
        batch_op.drop_column('status')
    # ### end Alembic commands ###
