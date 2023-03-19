import datetime
import sqlalchemy as sa
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    team_leader = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    job = sa.Column(sa.String)
    work_size = sa.Column(sa.Integer)
    collaborators = sa.Column(sa.String)
    start_date = sa.Column(sa.DateTime, default=datetime.datetime.now())
    end_date = sa.Column(sa.DateTime, default=datetime.datetime.now())
    is_finished = sa.Column(sa.Boolean)