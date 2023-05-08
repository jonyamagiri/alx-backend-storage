-- creates a stored procedure AddBonus that adds a new correction for a student
-- procedure AddBonus is taking 3 inputs:
    -- user_id, a users.id value
    -- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
    -- score, the score value for the correction
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus (
  IN user_id INT,
  IN project_name VARCHAR(255),
  IN score FLOAT
)
BEGIN
  DECLARE project_id INT DEFAULT 0;

  IF NOT EXISTS (SELECT id FROM projects WHERE name = project_name) THEN
    INSERT INTO projects (name) VALUES (project_name);
  END IF;

  SELECT id INTO project_id FROM projects WHERE name = project_name;

  INSERT INTO corrections (user_id, project_id, score)
  VALUES (user_id, project_id, score);
END $$
DELIMITER ;
