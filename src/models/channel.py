from flask import Flask
from sqlalchemy import Column, Integer, String, Boolean, Date, TIMESTAMP, ForeignKey
from db import Base

class Channel_Model(Base):
    __tablename__ = 'channels'
    id = Column(String(120), primary_key=True)
    name = Column(String(120), unique=True)
    owner = Column(Integer, ForeignKey('user.id'), nullable=False)
    org_id = Column(Integer, ForeignKey('organization.id'), nullable=False)
    is_private = Column(Boolean, unique=True)
    state = Column(String(120), unique=True)
    status = Column(String(120), unique=True)
    jsonb = Column(String(120), unique=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    def __init__(self, id, name, owner, org_id, is_private, state, status, jsonb, created_at, updated_at):
    	self.id = id
        self.name = name
        self.owner = owner
        self.org_id = org_id
        self.is_private = is_private
        self.state = state
        self.status = status
        self.jsonb = jsonb
        self.created_at = created_at
        self.updated_at = updated_at

        def __repr__(self):
            return '<Name %r>' % self.name