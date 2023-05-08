-- creates a stored procedure ComputeAverageScoreForUser that computes and
-- store the average score for a student:
    -- procedure ComputeAverageScoreForUser is taking 1 input
    -- user_id, a users.id value (you can assume user_id is linked to an existing users)
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER ++
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
    DECLARE total_score INT DEFAULT 0;
    DECLARE projects_count INT DEFAULT 0;

    SELECT SUM(score)
        INTO total_score
        FROM corrections
        WHERE corrections.user_id = user_id;
    SELECT COUNT(*)
        INTO projects_count
        FROM corrections
        WHERE corrections.user_id = user_id;

    UPDATE users
        SET users.average_score = CASE
            WHEN projects_count = 0 THEN 0
            ELSE total_score / projects_count
            END
        WHERE users.id = user_id;
END ++
DELIMITER ;
