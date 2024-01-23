"""url_shortener init

Revision ID: 24bc1a24e10e
Revises: 
Create Date: 2024-01-22 22:48:49.081629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24bc1a24e10e'
down_revision: str = None
branch_labels: None = None
depends_on: None = None


def upgrade() -> None:
    op.create_table(
        'url_shorten',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('url', sa.String, nullable=False),
        sa.Column('shortcode', sa.String(6), unique=True),
        sa.Column('created', sa.DateTime, server_default=sa.func.now()),
        sa.Column('last_redirect', sa.DateTime),
        sa.Column('redirect_count', sa.Integer, server_default='0'),
    )


def downgrade() -> None:
    op.drop_table('url_shorten')
