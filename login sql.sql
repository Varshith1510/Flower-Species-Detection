CREATE DATABASE login;
USE login;

CREATE TABLE login_detail(username VARCHAR(30) NOT NULL,
			pwd VARCHAR(30) NOT NULL);

INSERT INTO login_detail VALUES ('Varshith','vps@1510');
INSERT INTO login_detail VALUES ('Varun','vg@0304');
INSERT INTO login_detail VALUES ('Vignesh','vrs@1109');

SELECT * FROM login_detail;
