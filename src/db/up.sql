CREATE TABLE todos (
  id SERIAL PRIMARY KEY,
  content TEXT NOT NULL,
  complete BOOLEAN NOT NULL,
  created_at INTEGER NOT NULL,
  updated_at INTEGER
);

INSERT INTO todos (id, content, complete, created_at, updated_at) VALUES
  (1, 'clean kitchen', false, 0, 0),
  (2, 'wash car', false, 0, 0),
  (3, 'walk dog', false, 0, 0);