CREATE TABLE todos (
  id SERIAL PRIMARY KEY,
  content TEXT NOT NULL,
  complete BOOLEAN NOT NULL,
  created_at INTEGER NOT NULL,
  updated_at INTEGER
);
