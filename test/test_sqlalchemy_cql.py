"""
Tests for `sqlalchemy-cql` module.
"""
import pytest

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
)

def test_create_engine():
    eng = create_engine("cql://user:password@localhost:49154/system")
    assert eng.execute("select * from system.schema_keyspaces")


def test_table_names():
    eng = create_engine("cql://user:password@localhost:49154/system")
    eng.table_names()


def test_create_all():
    eng = create_engine("cql://user:password@localhost:49154/system")
    metadata.create_all(eng)