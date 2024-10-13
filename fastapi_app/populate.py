import psycopg2

conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_user",
    password="your_password",
    host="postgres",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS your_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    value INT
);
""")

cur.execute("""
INSERT INTO your_table (name, value) VALUES
('Item 1', 10),
('Item 2', 20),
('Item 3', 30);
""")

conn.commit()
cur.close()
conn.close()
