-- MySQL dump 10.13  Distrib 5.1.34, for Win32 (ia32)
--
-- Host: localhost    Database: bluebox
-- ------------------------------------------------------
-- Server version	5.1.34-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `documents_doc`
--

DROP TABLE IF EXISTS `documents_doc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `documents_doc` (
  `id_doc` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name_doc` varchar(45) NOT NULL,
  `file_doc` varchar(45) DEFAULT NULL,
  `idprj_doc` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id_doc`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documents_doc`
--

LOCK TABLES `documents_doc` WRITE;
/*!40000 ALTER TABLE `documents_doc` DISABLE KEYS */;
INSERT INTO `documents_doc` VALUES (1,'test document','testdoc.docx',1);
/*!40000 ALTER TABLE `documents_doc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meetings_met`
--

DROP TABLE IF EXISTS `meetings_met`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meetings_met` (
  `id_met` int(5) NOT NULL AUTO_INCREMENT,
  `subject_met` varchar(255) NOT NULL,
  `participants_met` varchar(255) NOT NULL,
  `location_met` varchar(255) DEFAULT NULL,
  `owner_met` int(5) NOT NULL,
  `notes_met` text,
  `start_met` datetime NOT NULL,
  `end_met` datetime DEFAULT NULL,
  PRIMARY KEY (`id_met`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meetings_met`
--

LOCK TABLES `meetings_met` WRITE;
/*!40000 ALTER TABLE `meetings_met` DISABLE KEYS */;
/*!40000 ALTER TABLE `meetings_met` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages_msg`
--

DROP TABLE IF EXISTS `messages_msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages_msg` (
  `id_msg` int(5) NOT NULL AUTO_INCREMENT,
  `from_msg` int(5) NOT NULL,
  `to_msg` int(5) NOT NULL,
  `title_msg` varchar(255) NOT NULL,
  `body_msg` text NOT NULL,
  `read_msg` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_msg`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages_msg`
--

LOCK TABLES `messages_msg` WRITE;
/*!40000 ALTER TABLE `messages_msg` DISABLE KEYS */;
INSERT INTO `messages_msg` VALUES (2,1,3,'Hi mom!','Really Hi.',0);
/*!40000 ALTER TABLE `messages_msg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_prj`
--

DROP TABLE IF EXISTS `projects_prj`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects_prj` (
  `id_prj` int(5) NOT NULL AUTO_INCREMENT,
  `name_prj` varchar(255) NOT NULL,
  `status_prj` int(1) NOT NULL,
  `added_by_prj` int(5) NOT NULL,
  `owned_by_prj` int(5) DEFAULT NULL,
  `startdate_prj` datetime DEFAULT NULL,
  `enddate_prj` datetime DEFAULT NULL,
  `cost_prj` float DEFAULT NULL,
  PRIMARY KEY (`id_prj`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_prj`
--

LOCK TABLES `projects_prj` WRITE;
/*!40000 ALTER TABLE `projects_prj` DISABLE KEYS */;
INSERT INTO `projects_prj` VALUES (1,'sample_project',0,1,2,NULL,NULL,NULL),(2,'sample_project3',0,1,3,NULL,NULL,NULL);
/*!40000 ALTER TABLE `projects_prj` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tasks_tsk`
--

DROP TABLE IF EXISTS `tasks_tsk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tasks_tsk` (
  `id_tsk` int(5) NOT NULL AUTO_INCREMENT,
  `idprj_tsk` int(5) NOT NULL,
  `title_tsk` varchar(255) NOT NULL,
  `description_tsk` text,
  `added_by_tsk` int(5) NOT NULL,
  `assignedto_tsk` int(5) DEFAULT NULL,
  `timeleft_tsk` int(5) DEFAULT '0',
  `status_tsk` int(1) NOT NULL,
  `starton_tsk` datetime DEFAULT NULL,
  `endon_tsk` datetime DEFAULT NULL,
  PRIMARY KEY (`id_tsk`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks_tsk`
--

LOCK TABLES `tasks_tsk` WRITE;
/*!40000 ALTER TABLE `tasks_tsk` DISABLE KEYS */;
INSERT INTO `tasks_tsk` VALUES (2,1,'some_data',NULL,3,1,NULL,0,NULL,NULL);
/*!40000 ALTER TABLE `tasks_tsk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams_tms`
--

DROP TABLE IF EXISTS `teams_tms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teams_tms` (
  `id_tms` int(5) NOT NULL AUTO_INCREMENT,
  `name_tms` varchar(255) NOT NULL,
  `managerid_tms` int(5) unsigned NOT NULL,
  PRIMARY KEY (`id_tms`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams_tms`
--

LOCK TABLES `teams_tms` WRITE;
/*!40000 ALTER TABLE `teams_tms` DISABLE KEYS */;
INSERT INTO `teams_tms` VALUES (2,'bigboss',1),(3,'otherteam',1),(4,'tiger team',3);
/*!40000 ALTER TABLE `teams_tms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_usr`
--

DROP TABLE IF EXISTS `users_usr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_usr` (
  `id_usr` int(5) unsigned NOT NULL AUTO_INCREMENT,
  `name_usr` varchar(255) NOT NULL,
  `email_usr` varchar(255) NOT NULL,
  `password_usr` varchar(255) NOT NULL,
  `status_usr` int(1) unsigned NOT NULL,
  `address_usr` text,
  `phone_usr` varchar(30) DEFAULT NULL,
  `salary_usr` float DEFAULT NULL,
  `teamid_usr` int(5) DEFAULT NULL,
  `managerid_usr` int(5) DEFAULT NULL,
  `notes_usr` text,
  PRIMARY KEY (`id_usr`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COMMENT='Table storing the users in the ERP';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_usr`
--

LOCK TABLES `users_usr` WRITE;
/*!40000 ALTER TABLE `users_usr` DISABLE KEYS */;
INSERT INTO `users_usr` VALUES (1,'john doe','jdoe@bbox.com','123456',0,NULL,NULL,NULL,NULL,NULL,NULL),(3,'bebebebebe','asdasd','123',2,NULL,NULL,NULL,4,NULL,NULL);
/*!40000 ALTER TABLE `users_usr` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2009-05-04 18:15:31
