/*
Navicat MySQL Data Transfer

Source Server         : testdb
Source Server Version : 50714
Source Host           : 127.0.0.1:3306
Source Database       : teachsystem

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2019-05-09 00:34:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `classrooms`
-- ----------------------------
DROP TABLE IF EXISTS `classrooms`;
CREATE TABLE `classrooms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of classrooms
-- ----------------------------
INSERT INTO `classrooms` VALUES ('1', '软件工程1702班');

-- ----------------------------
-- Table structure for `courses`
-- ----------------------------
DROP TABLE IF EXISTS `courses`;
CREATE TABLE `courses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `teacher_name` varchar(255) DEFAULT NULL,
  `classroom_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `teacher_name` (`teacher_name`),
  KEY `classroom_id` (`classroom_id`),
  CONSTRAINT `courses_ibfk_1` FOREIGN KEY (`teacher_name`) REFERENCES `teachers` (`username`),
  CONSTRAINT `courses_ibfk_2` FOREIGN KEY (`classroom_id`) REFERENCES `classrooms` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of courses
-- ----------------------------
INSERT INTO `courses` VALUES ('5', '计算机网络', 'sss', '1');
INSERT INTO `courses` VALUES ('6', '编译原理', 'sss', '1');
INSERT INTO `courses` VALUES ('8', '软件工程基础', 'sss', '1');

-- ----------------------------
-- Table structure for `debates`
-- ----------------------------
DROP TABLE IF EXISTS `debates`;
CREATE TABLE `debates` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `time` varchar(255) NOT NULL,
  `discuss_count` int(11) NOT NULL,
  `course_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `debates_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of debates
-- ----------------------------
INSERT INTO `debates` VALUES ('1', '孙晨为什么这么帅', '2019-05-07 00:06:18', '3', '5');

-- ----------------------------
-- Table structure for `discusses`
-- ----------------------------
DROP TABLE IF EXISTS `discusses`;
CREATE TABLE `discusses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` text NOT NULL,
  `time` varchar(255) NOT NULL,
  `good_count` int(11) NOT NULL,
  `student_name` varchar(255) DEFAULT NULL,
  `debate_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_name` (`student_name`),
  KEY `debate_id` (`debate_id`),
  CONSTRAINT `discusses_ibfk_1` FOREIGN KEY (`student_name`) REFERENCES `students` (`username`),
  CONSTRAINT `discusses_ibfk_2` FOREIGN KEY (`debate_id`) REFERENCES `debates` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of discusses
-- ----------------------------
INSERT INTO `discusses` VALUES ('1', '因为他是我爸爸', '2019-05-08 23:20:30', '2', 'jsfnsc', '1');
INSERT INTO `discusses` VALUES ('2', '牛逼\n', '2019-05-08 23:23:12', '2', 'jsfnsc', '1');
INSERT INTO `discusses` VALUES ('3', '哈哈哈哈', '2019-05-09 00:17:13', '2', 'jsfnsc', '1');

-- ----------------------------
-- Table structure for `films`
-- ----------------------------
DROP TABLE IF EXISTS `films`;
CREATE TABLE `films` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(255) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `films_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of films
-- ----------------------------
INSERT INTO `films` VALUES ('1', 'Gai_.mp4', '5');

-- ----------------------------
-- Table structure for `goods`
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_name` varchar(255) DEFAULT NULL,
  `discuss_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_name` (`student_name`),
  KEY `discuss_id` (`discuss_id`),
  CONSTRAINT `goods_ibfk_1` FOREIGN KEY (`student_name`) REFERENCES `students` (`username`),
  CONSTRAINT `goods_ibfk_2` FOREIGN KEY (`discuss_id`) REFERENCES `discusses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES ('4', 'jsfnsc', '1');
INSERT INTO `goods` VALUES ('5', 'jsfnsc', '2');
INSERT INTO `goods` VALUES ('6', 'jsfnsc', '3');
INSERT INTO `goods` VALUES ('7', 'swingc', '1');
INSERT INTO `goods` VALUES ('8', 'swingc', '2');
INSERT INTO `goods` VALUES ('9', 'swingc', '3');

-- ----------------------------
-- Table structure for `homework`
-- ----------------------------
DROP TABLE IF EXISTS `homework`;
CREATE TABLE `homework` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(255) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `homework_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of homework
-- ----------------------------
INSERT INTO `homework` VALUES ('1', 'homework-1.doc', '5');
INSERT INTO `homework` VALUES ('2', 'test-1.doc', '5');

-- ----------------------------
-- Table structure for `ppts`
-- ----------------------------
DROP TABLE IF EXISTS `ppts`;
CREATE TABLE `ppts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(255) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `ppts_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ppts
-- ----------------------------
INSERT INTO `ppts` VALUES ('1', 'computer_network_ch1-2019.ppt', '5');
INSERT INTO `ppts` VALUES ('3', 'computer_network_ch2-2019.ppt', '5');

-- ----------------------------
-- Table structure for `results`
-- ----------------------------
DROP TABLE IF EXISTS `results`;
CREATE TABLE `results` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(255) NOT NULL,
  `student_name` varchar(255) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `homework_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_name` (`student_name`),
  KEY `course_id` (`course_id`),
  KEY `homework_id` (`homework_id`),
  CONSTRAINT `results_ibfk_1` FOREIGN KEY (`student_name`) REFERENCES `students` (`username`),
  CONSTRAINT `results_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`),
  CONSTRAINT `results_ibfk_3` FOREIGN KEY (`homework_id`) REFERENCES `homework` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of results
-- ----------------------------
INSERT INTO `results` VALUES ('1', '3901170204_sunchen.docx', 'jsfnsc', '5', '1');

-- ----------------------------
-- Table structure for `reviews`
-- ----------------------------
DROP TABLE IF EXISTS `reviews`;
CREATE TABLE `reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` text NOT NULL,
  `time` varchar(255) NOT NULL,
  `student_name` varchar(255) DEFAULT NULL,
  `film_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_name` (`student_name`),
  KEY `film_id` (`film_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`student_name`) REFERENCES `students` (`username`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`film_id`) REFERENCES `films` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of reviews
-- ----------------------------
INSERT INTO `reviews` VALUES ('3', '棒！', '2019-04-27 23:47:50', 'jsfnsc', '1');
INSERT INTO `reviews` VALUES ('4', '棒！', '2019-04-27 23:47:50', 'jsfnsc', '1');
INSERT INTO `reviews` VALUES ('5', '很好', '2019-04-27 23:48:50', 'jsfnsc', '1');
INSERT INTO `reviews` VALUES ('6', '很好', '2019-04-27 23:48:50', 'jsfnsc', '1');
INSERT INTO `reviews` VALUES ('7', '牛逼', '2019-04-27 23:52:27', 'jsfnsc', '1');
INSERT INTO `reviews` VALUES ('8', '牛逼', '2019-04-27 23:52:27', 'jsfnsc', '1');

-- ----------------------------
-- Table structure for `students`
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `username` varchar(255) NOT NULL,
  `password` varchar(16) NOT NULL,
  `telephone` varchar(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `classroom_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`username`),
  KEY `classroom_id` (`classroom_id`),
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`classroom_id`) REFERENCES `classrooms` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES ('jsfnsc', '123456', '110', '1255731468@qq.com', '1');
INSERT INTO `students` VALUES ('swingc', '123456', '120', 'jsfnsc@qq.com', '1');

-- ----------------------------
-- Table structure for `teachers`
-- ----------------------------
DROP TABLE IF EXISTS `teachers`;
CREATE TABLE `teachers` (
  `username` varchar(255) NOT NULL,
  `password` varchar(16) NOT NULL,
  `telephone` varchar(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of teachers
-- ----------------------------
INSERT INTO `teachers` VALUES ('sss', '1', '15351531900', '1255731468@qq.com');
