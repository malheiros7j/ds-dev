import sqlite3

query_showroom_schema = """
	
	CREATE TABLE showroom(
		product_id				TEXT,
		fit						TEXT,
		product_name			TEXT,
		product_price			REAL,
		color_name				TEXT,	
		style_id				INTEGER,
		color_id				INTEGER,
		scrapy_datetime			TEXT,
		size_number				INTEGER,
		size_model				TEXT,
		cotton					REAL,
		polyester				REAL,
		elastane				REAL,
		elasterell				REAL)"""

# Connect do DB
conn = sqlite3.connect('h&m_db.sqlite')
cursor = conn.execute(query_showroom_schema)
conn.commit()
conn.close()

from sqlalchemy import create_engine

create_engine('sqlite:///h&m_db.sqlite')