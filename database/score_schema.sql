

CREATE TABLE IF NOT EXISTS `ScoreInformation` 
(
    `user_id` INT NOT NULL AUTO_INCREMENT,
    `experience_score` float NOT NULL,
    `engagement_score` float NOT NULL,
    `satisfaction_score` INT NOT NULL,
    PRIMARY KEY (`user_id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;

