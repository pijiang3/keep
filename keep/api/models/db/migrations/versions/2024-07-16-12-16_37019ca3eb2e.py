"""Incident related tables

Revision ID: 37019ca3eb2e
Revises: c37ec8f6db3e
Create Date: 2024-07-16 12:16:01.837477

"""

import sqlalchemy as sa
import sqlmodel
from alembic import op
from sqlalchemy_utils import UUIDType

# revision identifiers, used by Alembic.
revision = "37019ca3eb2e"
down_revision = "c37ec8f6db3e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "incident",
        sa.Column("id", sqlmodel.sql.sqltypes.types.Uuid(), nullable=False),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("assignee", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("creation_time", sa.DateTime(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=True),
        sa.Column("end_time", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["tenant_id"],
            ["tenant.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "alerttoincident",
        sa.Column(
            "incident_id",
            UUIDType(binary=False),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("alert_id", sqlmodel.sql.sqltypes.types.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["alert_id"],
            ["alert.id"],
        ),
        sa.ForeignKeyConstraint(["incident_id"], ["incident.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["tenant_id"],
            ["tenant.id"],
        ),
        sa.PrimaryKeyConstraint("incident_id", "alert_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("alerttoincident")
    op.drop_table("incident")
    # ### end Alembic commands ###
