CREATE TABLE todos (
  id SERIAL PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  content TEXT NOT NULL,
  complete BOOLEAN NOT NULL,
  created_at INTEGER NOT NULL,
  updated_at INTEGER
);
