"""update

Revision ID: e160edff3827
Revises: 3504f017a671
Create Date: 2021-12-18 19:37:18.412357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e160edff3827'
down_revision = '3504f017a671'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('flasklogin-users_country_key', 'flasklogin-users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('flasklogin-users_country_key', 'flasklogin-users', ['country'])
    # ### end Alembic commands ###