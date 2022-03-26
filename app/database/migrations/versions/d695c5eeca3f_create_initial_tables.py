"""create initial tables

Revision ID: d695c5eeca3f
Revises:
Create Date: 2022-03-26 23:07:03.717855

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'd695c5eeca3f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "actor",
        sa.Column("id", sa.Integer, unique=True, primary_key=True, autoincrement=True, nullable=False, index=True),
        sa.Column("slug", sa.String(36), nullable=False, unique=True),
        sa.Column("firstname", sa.String(35), nullable=False),
        sa.Column("lastname", sa.String(35), nullable=False)
    )

    op.create_table(
        "media",
        sa.Column("id", sa.Integer, unique=True, primary_key=True, autoincrement=True, nullable=False, index=True),
        sa.Column("slug", sa.String(36), nullable=False, unique=True),
        sa.Column("type", sa.Integer, nullable=False, index=True),
        sa.Column("rating", sa.Integer, nullable=True)
    )

    op.create_table(
        "actor_media",
        sa.Column("actor_id", sa.Integer, sa.ForeignKey("actor.id"), nullable=False, index=True),
        sa.Column("media_id", sa.Integer, sa.ForeignKey("media.id"), nullable=False, index=True)
    )

    op.create_table(
        "media_translation",
        sa.Column("id", sa.Integer, unique=True, primary_key=True, autoincrement=True, nullable=False, index=True),
        sa.Column("language", sa.Integer, nullable=False, index=True),
        sa.Column("name", sa.Integer, nullable=False, index=True),
        sa.Column("value", sa.String(500), nullable=False),
        sa.Column("media_id", sa.Integer, sa.ForeignKey("media.id"), nullable=False)
    )


def downgrade():
    op.drop_table("actor")
    op.drop_table("media")
    op.drop_table("actor_media")
    op.drop_table("media_translation")
