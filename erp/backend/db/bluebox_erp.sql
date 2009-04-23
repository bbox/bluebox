-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.0.67-0ubuntu6


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema bluebox
--

CREATE DATABASE IF NOT EXISTS bluebox;
USE bluebox;

--
-- Definition of table `bluebox`.`meetings_met`
--

DROP TABLE IF EXISTS `bluebox`.`meetings_met`;
CREATE TABLE  `bluebox`.`meetings_met` (
  `id_met` int(5) NOT NULL auto_increment,
  `subject_met` varchar(255) NOT NULL,
  `participants_met` varchar(255) NOT NULL,
  `location_met` varchar(255) NOT NULL,
  `owner_met` int(5) NOT NULL,
  `notes_met` text NOT NULL,
  `start_met` datetime NOT NULL,
  `end_met` datetime NOT NULL,
  PRIMARY KEY  (`id_met`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bluebox`.`meetings_met`
--

/*!40000 ALTER TABLE `meetings_met` DISABLE KEYS */;
LOCK TABLES `meetings_met` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `meetings_met` ENABLE KEYS */;


--
-- Definition of table `bluebox`.`messages_msg`
--

DROP TABLE IF EXISTS `bluebox`.`messages_msg`;
CREATE TABLE  `bluebox`.`messages_msg` (
  `id_msg` int(5) NOT NULL auto_increment,
  `from_msg` int(5) NOT NULL,
  `to_msg` int(5) NOT NULL,
  `title_msg` varchar(255) NOT NULL,
  `body_msg` text NOT NULL,
  PRIMARY KEY  (`id_msg`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bluebox`.`messages_msg`
--

/*!40000 ALTER TABLE `messages_msg` DISABLE KEYS */;
LOCK TABLES `messages_msg` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `messages_msg` ENABLE KEYS */;


--
-- Definition of table `bluebox`.`projects_prj`
--

DROP TABLE IF EXISTS `bluebox`.`projects_prj`;
CREATE TABLE  `bluebox`.`projects_prj` (
  `id_prj` int(5) NOT NULL auto_increment,
  `name_prj` varchar(255) NOT NULL,
  `status_prj` int(1) NOT NULL,
  `added_by_prj` int(5) NOT NULL,
  `owned_by_prj` int(5) NOT NULL,
  `startdate_prj` datetime NOT NULL,
  `enddate_prj` datetime NOT NULL,
  `cost_prj` float NOT NULL,
  PRIMARY KEY  (`id_prj`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bluebox`.`projects_prj`
--

/*!40000 ALTER TABLE `projects_prj` DISABLE KEYS */;
LOCK TABLES `projects_prj` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `projects_prj` ENABLE KEYS */;


--
-- Definition of table `bluebox`.`tasks_tsk`
--

DROP TABLE IF EXISTS `bluebox`.`tasks_tsk`;
CREATE TABLE  `bluebox`.`tasks_tsk` (
  `id_tsk` int(5) NOT NULL auto_increment,
  `id_prj_tsk` int(5) NOT NULL,
  `title_tsk` varchar(5) NOT NULL,
  `description_tsk` text,
  `added_by_tsk` int(5) NOT NULL,
  `assignedto_tsk` int(5) default NULL,
  `timeleft_tsk` int(5) default '0',
  `status_tsk` int(1) NOT NULL,
  `starton_tsk` datetime NOT NULL,
  `endon_tsk` datetime NOT NULL,
  PRIMARY KEY  (`id_tsk`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bluebox`.`tasks_tsk`
--

/*!40000 ALTER TABLE `tasks_tsk` DISABLE KEYS */;
LOCK TABLES `tasks_tsk` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `tasks_tsk` ENABLE KEYS */;


--
-- Definition of table `bluebox`.`teams_tms`
--

DROP TABLE IF EXISTS `bluebox`.`teams_tms`;
CREATE TABLE  `bluebox`.`teams_tms` (
  `id_tms` int(5) NOT NULL auto_increment,
  `name_tms` varchar(255) NOT NULL,
  `managerid_tms` int(5) unsigned NOT NULL,
  PRIMARY KEY  (`id_tms`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bluebox`.`teams_tms`
--

/*!40000 ALTER TABLE `teams_tms` DISABLE KEYS */;
LOCK TABLES `teams_tms` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `teams_tms` ENABLE KEYS */;


--
-- Definition of table `bluebox`.`users_usr`
--

DROP TABLE IF EXISTS `bluebox`.`users_usr`;
CREATE TABLE  `bluebox`.`users_usr` (
  `id_usr` int(5) unsigned NOT NULL auto_increment,
  `name_usr` varchar(255) NOT NULL,
  `email_usr` varchar(255) NOT NULL,
  `password_usr` varchar(255) NOT NULL,
  `status_usr` int(1) unsigned NOT NULL,
  `address_usr` text,
  `phone_usr` varchar(30) default NULL,
  `salary_usr` float default NULL,
  `teamid_usr` int(5) default NULL,
  `managerid_usr` int(5) default NULL,
  `notes_usr` text,
  PRIMARY KEY  (`id_usr`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='Table storing the users in the ERP';

--
-- Dumping data for table `bluebox`.`users_usr`
--

/*!40000 ALTER TABLE `users_usr` DISABLE KEYS */;
LOCK TABLES `users_usr` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `users_usr` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
