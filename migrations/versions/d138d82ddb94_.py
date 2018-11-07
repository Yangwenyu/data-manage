"""empty message

Revision ID: d138d82ddb94
Revises: 
Create Date: 2018-11-07 13:49:17.179527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd138d82ddb94'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_admin',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('rules', sa.Text(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('remark', sa.String(length=255), nullable=False),
    sa.Column('login_time', sa.Integer(), nullable=False),
    sa.Column('login_ip', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('auth_rule',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('rule', sa.String(length=100), nullable=False),
    sa.Column('auth_check', sa.Boolean(), nullable=False),
    sa.Column('only_root', sa.Boolean(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('listorder', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_auth_rule_pid'), 'auth_rule', ['pid'], unique=False)
    op.create_index(op.f('ix_auth_rule_rule'), 'auth_rule', ['rule'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_auth_rule_rule'), table_name='auth_rule')
    op.drop_index(op.f('ix_auth_rule_pid'), table_name='auth_rule')
    op.drop_table('auth_rule')
    op.drop_table('auth_admin')
    # ### end Alembic commands ###
