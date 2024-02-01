import sqlalchemy
import sys
import os

def get_wells(depth, gradient):
    connect = os.getenv('WELL_DB')
    engine = sqlalchemy.create_engine(connect)
    conn = engine.connect()
    
    query = """SELECT latitude, longitude, depth, gradient
                FROM wells
                WHERE depth > :dep AND gradient > :grad;"""
    
    q = sqlalchemy.text(query)
    
    return conn.execute(q, {'dep': depth, 'grad': gradient}).fetchall()

if __name__ == '__main__':
    depth = float(sys.argv[1])
    grad = float(sys.argv[2])
    
    print(get_wells(depth, grad))