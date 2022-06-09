CREATE DATABASE  IF NOT EXISTS `django_planning` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `django_planning`;
-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: django_planning
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `batiments`
--

DROP TABLE IF EXISTS `batiments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `batiments` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `nom` varchar(45) NOT NULL,
  `localisation` varchar(45) DEFAULT NULL,
  `facultes_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `batiments_facultes_id_89dbac6d_fk_facultes_id` (`facultes_id`),
  CONSTRAINT `batiments_facultes_id_89dbac6d_fk_facultes_id` FOREIGN KEY (`facultes_id`) REFERENCES `facultes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `batiments`
--

LOCK TABLES `batiments` WRITE;
/*!40000 ALTER TABLE `batiments` DISABLE KEYS */;
INSERT INTO `batiments` VALUES (1,'Bloc P','Bloc Pedagogique',NULL,1),(2,'Extension1','Departement Math/Info',NULL,1),(3,'Batiment A350','Batiment Amphi 350',NULL,1),(4,'Scolarite','Scolarite',NULL,1);
/*!40000 ALTER TABLE `batiments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classes`
--

DROP TABLE IF EXISTS `classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `effectif` int NOT NULL,
  `departements_id` bigint NOT NULL,
  `specialites_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `classes_specialites_id_d5c8e8cf_fk_specialites_id` (`specialites_id`),
  KEY `classes_departements_id_f1f3ab65_fk_departements_id` (`departements_id`),
  CONSTRAINT `classes_departements_id_f1f3ab65_fk_departements_id` FOREIGN KEY (`departements_id`) REFERENCES `departements` (`id`),
  CONSTRAINT `classes_specialites_id_d5c8e8cf_fk_specialites_id` FOREIGN KEY (`specialites_id`) REFERENCES `specialites` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes`
--

LOCK TABLES `classes` WRITE;
/*!40000 ALTER TABLE `classes` DISABLE KEYS */;
INSERT INTO `classes` VALUES (1,'INFO L1',600,1,NULL),(2,'INFO L2',300,1,NULL),(3,'INFO L3',250,1,NULL),(4,'INFOL3-SIGL',120,1,1),(5,'INFOL3-SR',100,1,2),(6,'INFOL3-DS',90,1,3),(7,'INFOL3-SECU',90,1,4),(8,'INFOM1',300,1,NULL),(9,'INFOM1-SIGL',100,1,1),(10,'INFOM1-SECU',50,1,4),(11,'INFOM1-DS',50,1,3),(12,'INFOM1-SR',50,1,2),(13,'PHYSL1-G1',1000,8,NULL),(14,'PHYSL1-G2',1000,8,NULL),(15,'PHYSL2',1000,8,NULL),(16,'PHYSL3',500,8,NULL),(17,'PHYSL3-EEA',300,8,5),(18,'PHYSL3-FONDA',500,8,7),(19,'PHYSL3-MECA',300,8,6),(20,'MATHL1',1000,2,NULL),(21,'MATHL2',300,2,NULL),(22,'MATHL3',200,2,NULL),(23,'MATHL3-ALGEBRE',150,2,8),(24,'MATHL3-ANALYSE',150,2,9),(25,'CHIML1',1500,6,NULL),(26,'CHIML2',500,6,NULL),(27,'CHIML3',300,6,NULL),(28,'CHIML3-CB',150,6,10),(29,'CHIML3-CM',150,6,11),(30,'CHIML3-CG',150,6,12);
/*!40000 ALTER TABLE `classes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classes_groupes`
--

DROP TABLE IF EXISTS `classes_groupes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classes_groupes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `classes_id` bigint NOT NULL,
  `groupes_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classes_groupes_classes_id_3bd5b09b_fk_classes_id` (`classes_id`),
  KEY `classes_groupes_groupes_id_69645dc3_fk_groupes_id` (`groupes_id`),
  CONSTRAINT `classes_groupes_classes_id_3bd5b09b_fk_classes_id` FOREIGN KEY (`classes_id`) REFERENCES `classes` (`id`),
  CONSTRAINT `classes_groupes_groupes_id_69645dc3_fk_groupes_id` FOREIGN KEY (`groupes_id`) REFERENCES `groupes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes_groupes`
--

LOCK TABLES `classes_groupes` WRITE;
/*!40000 ALTER TABLE `classes_groupes` DISABLE KEYS */;
INSERT INTO `classes_groupes` VALUES (1,13,1),(2,13,2);
/*!40000 ALTER TABLE `classes_groupes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cours_programmes`
--

DROP TABLE IF EXISTS `cours_programmes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cours_programmes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `classes_id` bigint NOT NULL,
  `enseignants_id` bigint NOT NULL,
  `plages_id` bigint DEFAULT NULL,
  `salles_id` bigint DEFAULT NULL,
  `ues_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cours_programmes_ues_id_classes_id_6b2b7154_uniq` (`ues_id`,`classes_id`),
  UNIQUE KEY `cours_programmes_enseignants_id_plages_id_7b76338a_uniq` (`enseignants_id`,`plages_id`),
  UNIQUE KEY `cours_programmes_salles_id_plages_id_357b7f64_uniq` (`salles_id`,`plages_id`),
  KEY `cours_programmes_plages_id_e7e6ec5a_fk_plages_id` (`plages_id`),
  KEY `cours_programmes_classes_id_6dd944ec_fk_classes_id` (`classes_id`),
  CONSTRAINT `cours_programmes_classes_id_6dd944ec_fk_classes_id` FOREIGN KEY (`classes_id`) REFERENCES `classes` (`id`),
  CONSTRAINT `cours_programmes_enseignants_id_d55e7aa5_fk_enseignants_id` FOREIGN KEY (`enseignants_id`) REFERENCES `enseignants` (`id`),
  CONSTRAINT `cours_programmes_plages_id_e7e6ec5a_fk_plages_id` FOREIGN KEY (`plages_id`) REFERENCES `plages` (`id`),
  CONSTRAINT `cours_programmes_salles_id_099a69f9_fk_salles_id` FOREIGN KEY (`salles_id`) REFERENCES `salles` (`id`),
  CONSTRAINT `cours_programmes_ues_id_ac6fc3bb_fk_ues_id` FOREIGN KEY (`ues_id`) REFERENCES `ues` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cours_programmes`
--

LOCK TABLES `cours_programmes` WRITE;
/*!40000 ALTER TABLE `cours_programmes` DISABLE KEYS */;
INSERT INTO `cours_programmes` VALUES (2,4,11,23,1,10),(3,3,8,18,4,12),(4,4,1,8,1,1),(5,4,2,1,1,2),(6,7,14,15,1,7),(7,5,5,9,1,6),(8,6,4,3,1,4),(9,6,6,10,1,5),(10,5,5,17,1,8),(11,3,7,5,4,11),(12,7,16,19,1,9),(13,5,3,2,1,3),(14,3,17,7,4,15),(15,6,19,24,1,13),(16,7,18,22,1,14),(17,2,24,12,5,29),(18,2,2,19,3,30),(19,2,25,25,6,32),(20,2,21,14,6,35),(21,2,19,17,3,31),(25,8,4,1,16,36),(26,8,15,2,16,37),(27,12,3,NULL,NULL,42),(28,12,3,NULL,NULL,43),(29,9,2,17,12,40),(30,10,14,NULL,NULL,49),(31,11,8,NULL,NULL,46),(32,11,6,NULL,NULL,45),(33,12,3,NULL,NULL,41),(34,10,18,NULL,NULL,47),(35,11,4,NULL,NULL,44),(36,9,12,NULL,NULL,38),(37,10,14,NULL,NULL,48),(38,13,26,2,8,50),(39,14,27,2,9,50),(40,14,28,12,8,51),(41,13,29,12,9,51),(42,13,30,19,8,52),(43,14,31,19,9,52),(44,13,32,7,8,53),(45,14,33,21,8,53),(46,15,35,10,8,56),(47,15,36,5,8,57),(48,15,37,20,9,58),(49,15,38,27,9,59),(50,15,33,7,7,60),(51,17,43,15,5,62),(52,19,39,3,5,63),(53,16,44,9,9,62),(54,18,40,12,10,66),(55,18,41,6,10,67),(56,16,42,20,8,68),(57,16,34,7,6,69),(58,20,50,8,3,70),(59,20,51,9,16,76),(60,20,52,3,10,71),(61,20,45,17,8,72),(62,20,30,18,8,77),(63,20,49,33,9,74),(64,20,47,14,4,75),(65,21,47,15,4,78),(66,21,54,22,4,79),(67,21,30,17,5,80),(68,21,38,4,4,81),(69,21,49,11,4,82),(70,21,55,25,18,57),(71,24,38,8,12,84),(72,23,56,8,11,85),(73,22,57,NULL,NULL,87),(74,22,58,NULL,NULL,88),(75,22,59,NULL,NULL,89),(76,24,20,NULL,NULL,90),(77,23,60,NULL,NULL,91),(78,22,61,NULL,NULL,92),(79,22,56,NULL,NULL,69),(80,25,62,2,18,54),(81,25,63,9,18,55),(82,25,66,3,8,73),(83,25,67,NULL,NULL,94),(84,25,69,NULL,NULL,101),(85,25,71,NULL,NULL,95),(86,25,73,NULL,NULL,75),(87,26,74,NULL,NULL,96),(88,26,75,NULL,NULL,97),(89,26,76,NULL,NULL,98),(90,26,77,NULL,NULL,99),(91,26,79,NULL,NULL,100),(92,26,80,NULL,NULL,59),(93,26,81,14,5,60),(94,30,82,29,3,102),(95,28,84,NULL,NULL,108),(96,30,77,NULL,NULL,104),(97,29,84,NULL,NULL,105),(98,27,85,17,10,106),(99,28,87,NULL,NULL,107),(100,29,88,32,4,108),(101,27,86,NULL,NULL,109),(102,27,78,7,10,69),(103,1,20,5,10,19),(104,1,88,NULL,NULL,27),(105,1,22,16,10,17),(106,1,15,23,10,18),(107,1,6,26,10,20),(108,1,5,NULL,NULL,21),(109,1,23,27,10,16),(110,1,21,21,10,28);
/*!40000 ALTER TABLE `cours_programmes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departements`
--

DROP TABLE IF EXISTS `departements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departements` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `nom` varchar(45) NOT NULL,
  `facultes_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `departements_facultes_id_727f1f83_fk_facultes_id` (`facultes_id`),
  CONSTRAINT `departements_facultes_id_727f1f83_fk_facultes_id` FOREIGN KEY (`facultes_id`) REFERENCES `facultes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departements`
--

LOCK TABLES `departements` WRITE;
/*!40000 ALTER TABLE `departements` DISABLE KEYS */;
INSERT INTO `departements` VALUES (1,'Depart Info','Departement Informatique',1),(2,'Depart Math','Departement de Mathematiques',1),(3,'Depart BCH','Departement BCH',1),(4,'Depart BOA','Departement de BOA',1),(5,'Depart BOV','Departement de BOv',1),(6,'Depart CHM','Departement de Chimie',1),(7,'Depart MIB','Departement de Micro-Biolologie',1),(8,'Depart PHY','Departement de Physique',1),(9,'Depart STU','Departement STU',1),(10,'Depart GEOS','Departement de Geo-Sciences',1);
/*!40000 ALTER TABLE `departements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'firstApi','batiment'),(9,'firstApi','departement'),(13,'firstApi','enseignant'),(14,'firstApi','etudiant'),(7,'firstApi','faculte'),(16,'firstApi','ressource'),(11,'firstApi','salle'),(15,'firstApi','typeressource'),(10,'firstApi','typesalle'),(12,'firstApi','utilisateur'),(20,'programmation','classe'),(21,'programmation','classegroupe'),(24,'programmation','coursprogramme'),(23,'programmation','enseigne'),(18,'programmation','groupe'),(19,'programmation','plage'),(17,'programmation','specialite'),(22,'programmation','ue'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-06-09 09:21:36.798670'),(2,'auth','0001_initial','2022-06-09 09:21:51.492024'),(3,'admin','0001_initial','2022-06-09 09:21:54.713599'),(4,'admin','0002_logentry_remove_auto_add','2022-06-09 09:21:54.814605'),(5,'admin','0003_logentry_add_action_flag_choices','2022-06-09 09:21:54.932450'),(6,'contenttypes','0002_remove_content_type_name','2022-06-09 09:21:56.427189'),(7,'auth','0002_alter_permission_name_max_length','2022-06-09 09:21:57.991554'),(8,'auth','0003_alter_user_email_max_length','2022-06-09 09:21:59.421885'),(9,'auth','0004_alter_user_username_opts','2022-06-09 09:21:59.556455'),(10,'auth','0005_alter_user_last_login_null','2022-06-09 09:22:00.714452'),(11,'auth','0006_require_contenttypes_0002','2022-06-09 09:22:00.802610'),(12,'auth','0007_alter_validators_add_error_messages','2022-06-09 09:22:00.910380'),(13,'auth','0008_alter_user_username_max_length','2022-06-09 09:22:02.196380'),(14,'auth','0009_alter_user_last_name_max_length','2022-06-09 09:22:03.636139'),(15,'auth','0010_alter_group_name_max_length','2022-06-09 09:22:05.001734'),(16,'auth','0011_update_proxy_permissions','2022-06-09 09:22:05.136364'),(17,'auth','0012_alter_user_first_name_max_length','2022-06-09 09:22:06.718148'),(18,'sessions','0001_initial','2022-06-09 09:22:08.267032'),(19,'firstApi','0001_initial','2022-06-09 09:30:45.196486'),(20,'programmation','0001_initial','2022-06-09 09:31:20.431009'),(21,'firstApi','0002_initial','2022-06-09 09:31:27.272700');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enseignants`
--

DROP TABLE IF EXISTS `enseignants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enseignants` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `matricule` varchar(45) DEFAULT NULL,
  `noms` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(45) NOT NULL,
  `departements_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `matricule` (`matricule`),
  KEY `enseignants_departements_id_a67ff623_fk_departements_id` (`departements_id`),
  CONSTRAINT `enseignants_departements_id_a67ff623_fk_departements_id` FOREIGN KEY (`departements_id`) REFERENCES `departements` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enseignants`
--

LOCK TABLES `enseignants` WRITE;
/*!40000 ALTER TABLE `enseignants` DISABLE KEYS */;
INSERT INTO `enseignants` VALUES (1,'15S2100','MONTHE Valery','montheplanning@gmail.com','monthe0001','simple',1),(2,'15S2101','JIOMEKONG Fidele','jiomekongplanning@gmail.com','jiomekong0002','simple',1),(3,'15S2102','HAMZA  Adamou','hamzaplanning@gmail.com','hamza0003','simple',1),(4,'15S2103','TAPAMO Hypolyte','tapamoplanning@gmail.com','tapamo','simple',1),(5,'15S2104','DOMGA','domgaplanning@gmail.com','domga0004','simple',1),(6,'15S2105','MELATAGIA','melatagiaplanning@gmail.com','melatagia0005','simple',1),(7,'15S2106','BAYEM','bayemplanning@gmail.com','bayem0006','simple',1),(8,'15S2107','NZEKON Armel','nzekonplanning@gmail.com','nzekon0007','simple',1),(11,'15S2108','ABESSOLO Gyslain','abessoloplanning@gmail.com','abessolo0008','simple',1),(12,'15S2109','KIMBI Xaviera','kimbiplanning@gmail.com','kimbi0009','simple',1),(13,NULL,'Zamba bote','bote@gmail.com','pbkdf2_sha256$320000$co2F9KDpXMl7z9ZrGKzJv9$Feh2ARjdLDK3swhFQMRi85W645Fv00E5i4DVK1McqEo=','admin',NULL),(14,'15S2110','NDOUNDAM','ndoundamplanning@gmail.com','ndoundam0010','simple',1),(15,'15S2111','KOUOKAM','kouokamplanning@gmail.com','0011','simple',1),(16,'15S2112','NKONDOCK Justin','nkondockplanning@gmail.com','0012','simple',1),(17,'15S2113','TCHOUNDJA','tchoundjaplanning@gmail.com','0013','simple',NULL),(18,'15S2114','EKODECK','ekodeckplanning@gmail.com','0014','simple',1),(19,'15S2115','MESSI Thomas','messiplanning@gmail.com','0015','simple',1),(20,'15S2116','MBAKOP','mbakopplanning@gmail.com','0016','simple',2),(21,'15S2117','MEFOUMA','mefoumaplanning@gmail.com','0017','simple',NULL),(22,'15S2118','AMINOU','aminouplanning@gmail.com','0018','simple',1),(23,'15S2119','TSOPZE','tsopzeplanning@gmail.com','0019','simple',1),(24,'15S2120','MAKEMBE','makembeplanning@gmail.com','0020','simple',1),(25,'15S2121','FOKAM','fokamplanning@gmail.com','0021','simple',1),(26,NULL,'PEMHA','pemha.planning@gmail.com','00001','simple',8),(27,NULL,'NANA NBENDJO','nana.planning@gmail.com','00002','simple',8),(28,NULL,'BEN BOLIE','benplanning@gmail.com','00003','simple',8),(29,NULL,'DJUIDJE','djuidjeplanning@gmail.com','00004','simple',8),(30,NULL,'CHENDJOU','chendjouplanning@gmail.com','00004','simple',2),(31,NULL,'TENKEU','tenkeuplanning@gmail.com','00005','simple',2),(32,NULL,'NTAM Elise','ntamplanning@gmail.com','00006','simple',NULL),(33,NULL,'MATIAFA','matiafaplanning@gmail.com','00007','simple',NULL),(34,NULL,'ABDOURAHIM','abdourahimplanning@gmail.com','00008','simple',NULL),(35,NULL,'MBINACK','mbinackplanning@gmail.com','00009','simple',8),(36,NULL,'SIMO','simoplanning@gmail.com','00010','simple',8),(37,NULL,'FEWO','fewoplanning@gmail.com','00011','simple',8),(38,NULL,'KIKI','kikiplanning@gmail.com','00012','simple',2),(39,NULL,'HONA','honaplanning@gmail.com','00013','simple',8),(40,NULL,'NDOP','ndopplanning@gmail.com','00014','simple',8),(41,NULL,'NJANDJOCK','njandjockplanning@gmail.com','00015','simple',8),(42,NULL,'TETSADJIO','tetsadjioplanning@gmail.com','00016','simple',8),(43,NULL,'BIYA MOTTO','biyaplanning@gmail.com','00017','simple',8),(44,NULL,'ZEKENG','nzekengplanning@gmail.com','00018','simple',8),(45,NULL,'MBEHOU','mbehouplanning@gmail.com','00019','simple',NULL),(46,NULL,'NGUEFACK','nguefackplanning@gmail.com','00020','simple',2),(47,NULL,'DJADEU','djadeuplanning@gmail.com','00021','simple',NULL),(48,NULL,'NABILADI','nabiladiplanning@gmail.com','00022','simple',NULL),(49,NULL,'EMVUDU','emvuduplannig@gmail.com','00023','simple',2),(50,NULL,'....1','planning@gmail.com','00024','simple',NULL),(51,NULL,'xxxx0','xxxxplanning@gmail.com','00025','simple',NULL),(52,NULL,'xxxx1','xxxx1planning@gmail.com','00026','simple',NULL),(53,NULL,'xxxx2','xxxx2planning@gmail.com','00027','simple',NULL),(54,NULL,'AGHOUKENG','aghoukengplanning@gmail.com','00028','simple',2),(55,NULL,'MBANE','mbaneplanning@gmail.com','00029','simple',8),(56,NULL,'TAKAM SOH','takamplanning@gmail.com','00030','simple',2),(57,NULL,'BEKOLLE','bekolleplanning@gmail.com','00031','simple',2),(58,NULL,'KIANPI','kianpiplanning@gmail.com','00032','simple',2),(59,NULL,'MBANG','mbangplanning@gmail.com','00033','simple',2),(60,NULL,'DOUANLA','douanlaplanning@gmail.com','00034','simple',2),(61,NULL,'NOUNDJEU','noundjeuplanning@gmail.com','00035','simple',2),(62,NULL,'xxxx3','xxxx3planning@gmail.com','00036','simple',6),(63,NULL,'xxxx4','xxxx4planning@gmail.com','00037','simple',NULL),(64,NULL,'EFFA','effaplannig@gmail.com','00038','simple',6),(65,NULL,'DJUIKWO','djuikwolanning@gmail.com','00039','simple',NULL),(66,NULL,'MBATAKOU','mbatakouplanning@gmail.com','00040','simple',2),(67,NULL,'NJABON','ndjabonplanning@gmail.com','00041','simple',6),(68,NULL,'BELIBI','belibiplanning@gmail.com','00042','simple',6),(69,NULL,'DONGO','dongoplanning@gmail.com','00043','simple',6),(70,NULL,'TAGATSING','tagatsingplanning@gmail.com','00044','simple',6),(71,NULL,'DJOUFAC','djoufacplanning@gmail.com','00045','simple',6),(72,NULL,'MBEY','mbeyplanning@gmail.com','00046','simple',6),(73,NULL,'MAKON','makonplanning@gmail.com','00047','simple',NULL),(74,NULL,'NANSEU KENNE','nanseuplanning@gmail.com','00048','simple',6),(75,NULL,'SADO','sadoplanning@gmail.com','00049','simple',NULL),(76,NULL,'EBELLE','ebelleplannig@gmail.com','00050','simple',1),(77,NULL,'KONG','kongplanning@gmail.com','00051','simple',6),(78,NULL,'NJOYA','njoyaplanning@gmail.com','00052','simple',6),(79,NULL,'WANDJI MBAZOA','wandjiplanning@gmail.com','00053','simple',6),(80,NULL,'LOUMGANG','loumgangplanning@gmail.com','00054','simple',2),(81,NULL,'MKOUNGA','mkoungaplanning@gmail.com','00055','simple',NULL),(82,NULL,'NENWA','nenwaplanning@gmail.com','00056','simple',6),(83,NULL,'SIEWE','sieweplanning@gmail.com','00057','simple',6),(84,NULL,'DJANGANG','djangangplanning@gmail.com','00058','simple',6),(85,NULL,'YANKEP','yankepplanning@gmail.com','00059','simple',6),(86,NULL,'KEMEGNE','kemegneplanning@gmail.com','00060','simple',6),(87,NULL,'XXX5','xxxx5planning@gmail.com','00061','simple',NULL),(88,NULL,'XXXX6','xxxx6planning@gmail.com','00062','simple',NULL);
/*!40000 ALTER TABLE `enseignants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enseignes`
--

DROP TABLE IF EXISTS `enseignes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enseignes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `classes_id` bigint NOT NULL,
  `enseignants_id` bigint DEFAULT NULL,
  `ues_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `contrainte_enseigne` (`ues_id`,`enseignants_id`,`classes_id`),
  UNIQUE KEY `enseignes_ues_id_enseignants_id_classes_id_1a3d098f_uniq` (`ues_id`,`enseignants_id`,`classes_id`),
  KEY `enseignes_classes_id_11f0a979_fk_classes_id` (`classes_id`),
  KEY `enseignes_enseignants_id_621a6117_fk_enseignants_id` (`enseignants_id`),
  CONSTRAINT `enseignes_classes_id_11f0a979_fk_classes_id` FOREIGN KEY (`classes_id`) REFERENCES `classes` (`id`),
  CONSTRAINT `enseignes_enseignants_id_621a6117_fk_enseignants_id` FOREIGN KEY (`enseignants_id`) REFERENCES `enseignants` (`id`),
  CONSTRAINT `enseignes_ues_id_3be11e12_fk_ues_id` FOREIGN KEY (`ues_id`) REFERENCES `ues` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enseignes`
--

LOCK TABLES `enseignes` WRITE;
/*!40000 ALTER TABLE `enseignes` DISABLE KEYS */;
/*!40000 ALTER TABLE `enseignes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `etudiants`
--

DROP TABLE IF EXISTS `etudiants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `etudiants` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `matricule` varchar(45) DEFAULT NULL,
  `noms` varchar(255) NOT NULL,
  `adresse` varchar(255) DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(255) NOT NULL,
  `classes_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `etudiants_classes_id_fc4cd5e8_fk_classes_id` (`classes_id`),
  CONSTRAINT `etudiants_classes_id_fc4cd5e8_fk_classes_id` FOREIGN KEY (`classes_id`) REFERENCES `classes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `etudiants`
--

LOCK TABLES `etudiants` WRITE;
/*!40000 ALTER TABLE `etudiants` DISABLE KEYS */;
INSERT INTO `etudiants` VALUES (1,'18T2571','Essimi Mvondo Odile Rosita','650094163','rosita.essimi@facsciences-uy1.cm','facsciences-18T2571',NULL),(2,'21S2783','Manpho Ngueda Murhiell','699146923','murhiellmanpho@gmail.com','mumu@8233',NULL),(3,NULL,'Nouchen Tchamba',NULL,'voltaire@gmail.com','pbkdf2_sha256$320000$eNvx0zuy6hZz5dvbf4fRKw$SXORVpHEiQUxQk6HLSnJzqaR660rgJiTWJRxRfw3yQA=',NULL),(4,NULL,'Manuela Manu',NULL,'manu@gmail.com','pbkdf2_sha256$320000$6Djje1kFmNLnUROT9MVQYK$pnS9hwawA1/eCH5lJng+du9q1mRukSllZXKEUfTc6wk=',NULL),(5,NULL,'Ndambal',NULL,'dal@gmail.com','pbkdf2_sha256$320000$A2G1dq1x8JGo26S4pNrvNt$7dtEzLg1Pm8Wtrv/Slt4Zu2wimwFhpv31+KaL8M8pHo=',NULL),(6,NULL,'Ndambal',NULL,'sal@gmail.com','pbkdf2_sha256$320000$9EJjsWFJQJatQ0k9hjVBAH$agsiHOO+uqRSHu++KWfpD6DmSDB+jEHDj6LkceNYSig=',NULL),(7,NULL,'dabadaba',NULL,'daba@gmail.com','pbkdf2_sha256$320000$gLJKuz9DrhfahuBIepmbM1$oisafv49YaBKS0BK7s5n9nJcnAKtXjzI5uJYKByHf9I=',NULL),(8,NULL,'Rosi Rosi',NULL,'rosi@gmail.com','pbkdf2_sha256$320000$XtKDlJXmhrAtfPa6LOq0zx$3XzkBVqZNsQRCMAM8v/VlPcL0DsAahtCw8k4QPrp5Jg=',NULL),(9,NULL,'Ngoune Wilfried Baudouin',NULL,'ngoune@gmail.com','pbkdf2_sha256$320000$tqedTkZyeyEZQR7USSiHCj$52Kx0HwcDV+WfaPiKvZ1E8d7kAUO4et5YEkaZxvew3U=',NULL),(10,NULL,'Kamgo Junior',NULL,'ka@gmail.com','pbkdf2_sha256$320000$JoMR5Sj2JOH0LmRz6GiLCC$q0+wxUN3vtDaFMKmU0jQkKYXJJZHRsXLWEWsVHWNilg=',NULL),(11,NULL,'Wilfried NGOUNE',NULL,'wilfriedngou@gmail.com','pbkdf2_sha256$320000$Ac6WIykOMi0Uh3LVRuOVdl$HxLMRsnNvJGogNYcapmrZT7f1+wRQ4B8lF70LCUFPIo=',NULL),(12,NULL,'frank junior',NULL,'tabuguiafrank@gmail.com','pbkdf2_sha256$320000$g9L0XC7EBixOShUgHAgzCw$Xaz+w813vl+0vUXWhvoACYOherOCzV2zBczJ8sU+K1g=',NULL),(13,NULL,'junior',NULL,'junior@email.com','pbkdf2_sha256$320000$lDFa7IKBsPy7RuK4aOidqS$jba7ztKC6wwmUJlYS8o7ItbpP4YxEQkRgDEWAyB/RM4=',NULL),(14,NULL,'user',NULL,'user@gmail.com','pbkdf2_sha256$320000$0buf00CCoyC1ocnEvhimih$3zPtBxmU9mVboFDFtZrrdvkxiQRZ6vFYu3clarfpWig=',NULL);
/*!40000 ALTER TABLE `etudiants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facultes`
--

DROP TABLE IF EXISTS `facultes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facultes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `nom` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facultes`
--

LOCK TABLES `facultes` WRITE;
/*!40000 ALTER TABLE `facultes` DISABLE KEYS */;
INSERT INTO `facultes` VALUES (1,'Fac Sciences','Faculte des Sciences');
/*!40000 ALTER TABLE `facultes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groupes`
--

DROP TABLE IF EXISTS `groupes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groupes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `nom` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groupes`
--

LOCK TABLES `groupes` WRITE;
/*!40000 ALTER TABLE `groupes` DISABLE KEYS */;
INSERT INTO `groupes` VALUES (1,'G1','Groupe1'),(2,'G2','Groupe2'),(3,'G3','Groupe3');
/*!40000 ALTER TABLE `groupes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plages`
--

DROP TABLE IF EXISTS `plages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plages` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `jour` varchar(45) NOT NULL,
  `periode` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `plages_jour_periode_5926bca9_uniq` (`jour`,`periode`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plages`
--

LOCK TABLES `plages` WRITE;
/*!40000 ALTER TABLE `plages` DISABLE KEYS */;
INSERT INTO `plages` VALUES (14,'DIMANCHE','10h05 - 12h55'),(21,'DIMANCHE','13h05 - 15h55'),(28,'DIMANCHE','16h05 - 18h55'),(35,'DIMANCHE','19h05 - 21h55'),(7,'DIMANCHE','7h00 - 9h55'),(11,'JEUDI','10h05 - 12h55'),(18,'JEUDI','13h05 - 15h55'),(25,'JEUDI','16h05 - 18h55'),(32,'JEUDI','19h05 - 21h55'),(4,'JEUDI','7h00 - 9h55'),(8,'LUNDI','10h05 - 12h55'),(15,'LUNDI','13h05 - 15h55'),(22,'LUNDI','16h05 - 18h55'),(29,'LUNDI','19h05 - 21h55'),(1,'LUNDI','7h00 - 9h55'),(9,'MARDI','10h05 - 12h55'),(16,'MARDI','13h05 - 15h55'),(23,'MARDI','16h05 - 18h55'),(30,'MARDI','19h05 - 21h55'),(2,'MARDI','7h00 - 9h55'),(10,'MERCREDI','10h05 - 12h55'),(17,'MERCREDI','13h05 - 15h55'),(24,'MERCREDI','16h05 - 18h55'),(31,'MERCREDI','19h05 - 21h55'),(3,'MERCREDI','7h00 - 9h55'),(13,'SAMEDI','10h05 - 12h55'),(20,'SAMEDI','13h05 - 15h55'),(27,'SAMEDI','16h05 - 18h55'),(34,'SAMEDI','19h05 - 21h55'),(6,'SAMEDI','7h00 - 9h55'),(12,'VENDREDI','10h05 - 12h55'),(19,'VENDREDI','13h05 - 15h55'),(26,'VENDREDI','16h05 - 18h55'),(33,'VENDREDI','19h05 - 21h55'),(5,'VENDREDI','7h00 - 9h55');
/*!40000 ALTER TABLE `plages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ressources`
--

DROP TABLE IF EXISTS `ressources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ressources` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `nom` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL,
  `facultes_id` bigint NOT NULL,
  `type_ressources_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `ressources_facultes_id_94038bd6_fk_facultes_id` (`facultes_id`),
  KEY `ressources_type_ressources_id_300dab91_fk_type_ressources_id` (`type_ressources_id`),
  CONSTRAINT `ressources_facultes_id_94038bd6_fk_facultes_id` FOREIGN KEY (`facultes_id`) REFERENCES `facultes` (`id`),
  CONSTRAINT `ressources_type_ressources_id_300dab91_fk_type_ressources_id` FOREIGN KEY (`type_ressources_id`) REFERENCES `type_ressources` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ressources`
--

LOCK TABLES `ressources` WRITE;
/*!40000 ALTER TABLE `ressources` DISABLE KEYS */;
/*!40000 ALTER TABLE `ressources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salles`
--

DROP TABLE IF EXISTS `salles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salles` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `nom` varchar(45) NOT NULL,
  `etat_electricite` int NOT NULL,
  `capacite` int NOT NULL,
  `batiments_id` bigint DEFAULT NULL,
  `type_salles_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `salles_code_batiments_id_e93e3ef6_uniq` (`code`,`batiments_id`),
  KEY `salles_batiments_id_02f3cdfe_fk_batiments_id` (`batiments_id`),
  KEY `salles_type_salles_id_b1824b50_fk_type_salles_id` (`type_salles_id`),
  CONSTRAINT `salles_batiments_id_02f3cdfe_fk_batiments_id` FOREIGN KEY (`batiments_id`) REFERENCES `batiments` (`id`),
  CONSTRAINT `salles_type_salles_id_b1824b50_fk_type_salles_id` FOREIGN KEY (`type_salles_id`) REFERENCES `type_salles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salles`
--

LOCK TABLES `salles` WRITE;
/*!40000 ALTER TABLE `salles` DISABLE KEYS */;
INSERT INTO `salles` VALUES (1,'S006','S 006',1,100,2,1),(2,'S008','S 008',1,200,2,1),(3,'A250','Amphi 250',1,250,3,2),(4,'A350','Amphi 350',1,350,3,2),(5,'AIII','Amphi III',1,200,4,2),(6,'R101','R 101',1,160,1,1),(7,'R108','R 108',1,160,1,1),(8,'A1001','Amphi 1001',1,1000,NULL,2),(9,'A1002','Amphi 1002',1,1000,NULL,2),(10,'A502','Amphi 502',1,500,NULL,2),(11,'AI','Amphi I',1,120,4,2),(12,'AII','Amphi II',1,120,4,2),(13,'R106','R 106',1,80,1,1),(14,'R107','R 107',1,80,1,1),(15,'S01/02','S 01 / 02',1,120,1,2),(16,'A135','Amphi 135',1,140,3,2),(17,'S24B','S 24B',1,30,NULL,1),(18,'R110','R 110',1,120,1,1),(19,'E201','E 201',1,60,NULL,1),(20,'E203','E 203',1,60,NULL,1),(21,'E204','E 204',1,60,NULL,1),(22,'E205','E 205',1,60,NULL,1),(23,'E206','E 206',1,60,NULL,1);
/*!40000 ALTER TABLE `salles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specialites`
--

DROP TABLE IF EXISTS `specialites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `specialites` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `nom` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialites`
--

LOCK TABLES `specialites` WRITE;
/*!40000 ALTER TABLE `specialites` DISABLE KEYS */;
INSERT INTO `specialites` VALUES (1,'SI-GL','Systeme d\'Information et Genie Logiciel'),(2,'SR','Systeme et Reseau'),(3,'DS','Data Sciences'),(4,'SECU','Securite'),(5,'PHYSL3-EEA','Electronique, Electrotechnique et Automatiqu'),(6,'PHYSL3-MECA','Mecanique'),(7,'PHYSL3-FONDA','Fondamentale'),(8,'MATHL3-Specialites 1','math'),(9,'MATHL3-Specialites 2','BCDFG'),(10,'CHIML3-CB','Chimie Biologique'),(11,'CHIML3-CM','Chimie des matériaux'),(12,'CHIML3-CG','Chimie Generale');
/*!40000 ALTER TABLE `specialites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_ressources`
--

DROP TABLE IF EXISTS `type_ressources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type_ressources` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `nom` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_ressources`
--

LOCK TABLES `type_ressources` WRITE;
/*!40000 ALTER TABLE `type_ressources` DISABLE KEYS */;
/*!40000 ALTER TABLE `type_ressources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_salles`
--

DROP TABLE IF EXISTS `type_salles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type_salles` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `nom` varchar(45) NOT NULL,
  `description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_salles`
--

LOCK TABLES `type_salles` WRITE;
/*!40000 ALTER TABLE `type_salles` DISABLE KEYS */;
INSERT INTO `type_salles` VALUES (1,'Salle','Salle Simple',NULL),(2,'Amphi','Amphitheatre',NULL);
/*!40000 ALTER TABLE `type_salles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ues`
--

DROP TABLE IF EXISTS `ues`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ues` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `intitule` varchar(255) NOT NULL,
  `credit` smallint unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  CONSTRAINT `ues_chk_1` CHECK ((`credit` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ues`
--

LOCK TABLES `ues` WRITE;
/*!40000 ALTER TABLE `ues` DISABLE KEYS */;
INSERT INTO `ues` VALUES (1,'INF3186','Business Intelligence',6),(2,'INF3176','Programmation Avance',6),(3,'INF3206','Programmation Systeme',6),(4,'INF 3246','Traitement D\'\'Image',6),(5,'INF3236','Apprentissage Artificiel 1',6),(6,'INF3216','Supervision Reseau',6),(7,'INF3276','Theorie des Nombres',6),(8,'INF3226','Projet',3),(9,'INF3286','Projet',3),(10,'INF3196','Projet',3),(11,'INF3046','Systeme d\'exploitation et reseau',6),(12,'INF3036','Base de donnees',6),(13,'INF3256','Projet',3),(14,'INF3266','Theorie des Codes 2',6),(15,'PPE','Projet Professionnel de l\'etudiant',2),(16,'INF132','Introduction A L\' Algorithmique',6),(17,'INF112','',6),(18,'INF122','',6),(19,'MATH112','Algebre 1',6),(20,'INF142','',6),(21,'INF152','',6),(22,'INF1042','Introduction aux Structures de Donnees',6),(23,'INF1052','Introduction aux Reseaux',6),(24,'INF1062','Introduction aux Systemes d\'Exploitations',6),(25,'MATH1052','Analyse1',6),(26,'ENG152','English for Mathematics and Computer Sciences 1',3),(27,'FRA152','Francais pour Sciences Mathematiques et Informatiques 1',3),(28,'PPE1011','Projet Personnel de l\'etudiant',3),(29,'INF2044','Statistique et Analyse de Donnees',6),(30,'INF2054','Modelisation et Programmation Oriente Objet en C++ ou Java',6),(31,'INF2064','Programmation Web',6),(32,'MAT2124','Analyse2',6),(33,'EnG2144','English for Mathematics and Computer Sciences 2',3),(34,'FRA2134','Francais pour Sciences Mathematiques et Informatiques 2',3),(35,'PPExx4','PPE',3),(36,'INF4038','Base de Donnees Distribuees',6),(37,'INF4048','Compilation',6),(38,'INF4178','Genie Logiciel',6),(39,'INF4188','Web  Semantique et Applications',6),(40,'INF4198','Projet II',6),(41,'INF4208','Reseaux Mobile Et Sans Fils',6),(42,'INF4218','Programmation Distribuee',6),(43,'INF4228','Projet II',6),(44,'INF4238','Systeme sExperts',6),(45,'INF4248','Apprentissage Artificiel II',6),(46,'INF4258','Projet II',6),(47,'INF4268','Cryptographie Asymetrique',6),(48,'INF4278','Courbes Elliptique II',6),(49,'INF4288','Projet II',6),(50,'PHYS122','',6),(51,'PHYS112','',6),(52,'MAT162','Calcul différentiel et géométrie pour les Sciences Physiques',6),(53,'PPE112','Professionnali-sation et éthique',3),(54,'ENG1002','Anglais',3),(55,'FRA1002','Francais pour Sciences Physique',3),(56,'PHY2064','Eléments d\'Electronique',3),(57,'PHY2044','Introduction à la Physique quantique',6),(58,'PHY2054','Thermodynamique',6),(59,'MAT2144','Probabilités et Statistiques pour les Sciences Physiques',6),(60,'PPE2004','',3),(61,'PHY3136','Propriétés de la matière condensée',6),(62,'PHY3196','Electrotechnique',6),(63,'PHY3176','Hydraulique',6),(64,'PHY3166','Résistance des Matériaux',6),(65,'PHY3186','CAO des circuits électroniques',6),(66,'PHY3146','Vibrations lumineuses et optique cohérente',6),(67,'PHY3156','Physique statistique',6),(68,'MAT3136','Techniques mathématiques pour la Physique',6),(69,'PPE3006','Professionnali-sation et éthique',3),(70,'ENG1001','',3),(71,'PHY112','Electrocinétique et magnétostatique',3),(72,'MAT132','',6),(73,'MAT112','',6),(74,'MAT142','',6),(75,'PPE1002','',3),(76,'FRA1001','',3),(77,'MAT122','',6),(78,'MAT2074','Calcul intégral sur Rn',6),(79,'MAT2084','Calcul scientifique',6),(80,'MAT2114','',6),(81,'MAT2094','Eléments d’Analyse Numérique',6),(82,'MAT2104','Introduction à la Cryptographie',6),(83,'MAT2134','',6),(84,'MAT3096','Probabilités II',6),(85,'MAT3106','Statistique Mathématique',6),(86,'MAT3176','',6),(87,'MAT3076','',6),(88,'MAT3066','',6),(89,'MAT3086','',6),(90,'MAT3116','',6),(91,'MAT3126','',6),(92,'MAT3056','',6),(93,'BIO152','',6),(94,'CHM112','',6),(95,'CHM132','',6),(96,'CHM2054','',6),(97,'CHM2094','',6),(98,'INF2114','',3),(99,'CHM2064','',6),(100,'CHM2044','',6),(101,'CHM122','',6),(102,'CHM3106','Chimie quantique et Théorie des groupes',6),(103,'CHM3136','Relations structure-propriété dans les matériaux',6),(104,'CHM3116','Radiocristallographie',5),(105,'CHM3146','Caractérisations et analyses des matériaux',5),(106,'CHM3086','Mécanisme réactionnel B',5),(107,'CHM3126','Pharmacognosie',5),(108,'BCH3136','Métabolisme',5),(109,'CHIM3076','Cinétique Chimique et Catalyse',6);
/*!40000 ALTER TABLE `ues` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-09 16:18:40
