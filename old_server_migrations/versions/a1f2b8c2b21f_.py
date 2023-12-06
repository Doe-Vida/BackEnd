"""empty message

Revision ID: a1f2b8c2b21f
Revises: 430b9b965ce7
Create Date: 2023-12-02 14:40:47.048812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1f2b8c2b21f'
down_revision = '430b9b965ce7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donation_order', schema=None) as batch_op:
        batch_op.alter_column('blood_type',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=3),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_reset_token', sa.String(length=6), nullable=True))
        batch_op.add_column(sa.Column('photo', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('photo')
        batch_op.drop_column('password_reset_token')

    with op.batch_alter_table('donation_order', schema=None) as batch_op:
        batch_op.alter_column('blood_type',
               existing_type=sa.String(length=3),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###