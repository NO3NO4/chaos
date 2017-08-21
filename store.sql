# -*- coding:utf-8 -*-

CREATE TABLE subject (
  id int(11) PRIMARY KEY AUTO_INCREMENT,
  title varchar(32),
  intro varchar(256),
  create_time timestamp
) AUTO_INCREMENT = 10000;
