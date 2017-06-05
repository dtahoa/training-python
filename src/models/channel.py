"""
src/models/channel.py: Channel Mapping Object
Copyright 2017-2018 LinhHo Training.
"""

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from db import Base


class Channel_Model(Base):
    __tablename__ = 'channels'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    owner = Column(Integer, ForeignKey('users.id'), nullable=False)
    org_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    is_private = Column(Boolean, unique=True)
    state = Column(String(120), unique=True)
    status = Column(String(120), unique=True)
    shared_with = Column(String(120), unique=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    def __init__(self,
                 id,
                 name,
                 owner,
                 org_id,
                 is_private,
                 state,
                 status,
                 shared_with,
                 created_at,
                 updated_at):
        self.id = id
        self.name = name
        self.owner = owner
        self.org_id = org_id
        self.is_private = is_private
        self.state = state
        self.status = status
        self.shared_with = shared_with
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<Name %r>' % self.name
