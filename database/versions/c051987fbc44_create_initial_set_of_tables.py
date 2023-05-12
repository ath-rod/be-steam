"""create_initial_set_of_tables

Revision ID: c051987fbc44
Revises:
Create Date: 2023-04-10 16:03:40.883730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c051987fbc44"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    sql = """
    -- https://www.postgresql.org/docs/10/uuid-ossp.html
    CREATE EXTENSION "uuid-ossp";

    -- https://www.postgresql.org/docs/current/pgcrypto.html
    CREATE EXTENSION "pgcrypto";

    CREATE TABLE IF NOT EXISTS users (
        uuid UUID DEFAULT uuid_generate_v1() PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        deleted_at TIMESTAMPTZ
    );
    """
    op.execute(sql)


def downgrade() -> None:
    pass
