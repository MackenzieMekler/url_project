create database urlshorten;
use urlshorten;

CREATE TABLE urlsh (
  id INT unsigned NOT NULL AUTO_INCREMENT,
  code VARCHAR(20),
  url VARCHAR(400),
  day VARCHAR(20),
  primary key (id)
);
