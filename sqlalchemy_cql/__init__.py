__author__ = 'Wojciech Bederski'
__email__ = 'github@wuub.net'
__version__ = '0.1.0'


from sqlalchemy.engine import default
import cql

class CQLCursor(object):

    @property
    def description(self):
        return [('count'),]

    def execute(self, query, parameters=None):
        pass

    def fetchone(self):
        return (12, )

    def close(self):
        pass


class CQLDupsko(object):
    paramstyle = cql.paramstyle
    Error = cql.Error

    @classmethod
    def connect(cls, host, port, database=None, username=None, password=None):

        connection = cql.connect(host, port, cql_version="3.0.0")
        connection.rollback = lambda: 0

        return connection


class CQLDialect(default.DefaultDialect):
    name = "cql"
    default_schema_name = 'system'

    def initialize(self, connection):
        pass

    @classmethod
    def dbapi(cls):
        return CQLDupsko

    def  get_table_names(self, connection, schema=None, **kw):
        return ['.'.join(row) for row in connection.execute("SELECT keyspace_name, columnfamily_name FROM system.schema_columnfamilies")]
