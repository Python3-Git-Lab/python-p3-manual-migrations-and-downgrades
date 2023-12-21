"""Renaming students to scholars

Revision ID: fa77ae32e96b
Revises: 791279dd0760
Create Date: 2023-12-21 08:12:44.210466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa77ae32e96b'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars','students')
