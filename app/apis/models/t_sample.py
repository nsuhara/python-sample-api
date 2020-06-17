"""app/apis/models/t_sample.py
"""
from datetime import datetime, timezone

from sqlalchemy.dialects.postgresql import insert

from apis.models import db


class Sample(db.Model):
    """sample model
    """
    __tablename__ = 't_sample'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transaction = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=created_at.default)

    def __init__(self, payload):
        self.transaction = payload.get('transaction')

    def set_attrs(self, payload):
        """set_attrs
        """
        for name, value in payload.items():
            if name in self.__dict__:
                setattr(self, name, value)
        setattr(self, 'updated_at', datetime.now(timezone.utc))

    def to_dict(self):
        """to_dict
        """
        return {
            'id': self.id,
            'transaction': self.transaction,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


def upsert_stmt():
    """upsert_stmt
    """
    stmt = insert(Sample)
    return stmt.on_conflict_do_update(
        index_elements=['id'],
        set_={
            'transaction': stmt.excluded.transaction,
            'updated_at': stmt.excluded.updated_at
        })
