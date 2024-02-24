-- MySQL dump 10.13  Distrib 5.6.23, for Win32 (x86)
--
-- Host: 127.0.0.1    Database: school
-- ------------------------------------------------------
-- Server version	5.6.49-log

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
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `id` int(3) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `dept` varchar(20) DEFAULT NULL,
  `post` varchar(15) DEFAULT NULL,
  `salary` int(4) DEFAULT NULL,
  `mobileno` char(10) DEFAULT NULL,
  `residence` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (101,'bhavanii','box office','staff',7500,'9758700954','ngo colony'),(102,'amirtha','box office','staff',7000,'9640625794','velacherry'),(103,'pooja','box office','staff',7000,'9446663136','vijay nagar'),(104,'bhavesh','box office','staff',7000,'9427721237','pallikaranai'),(105,'daniel','house mgmt','janitor',3500,'9191814317','velacherry'),(106,'jhonny','house mgmt','janitor',3000,'9769912557','kannigapuram'),(107,'shanjay','house mgmt','cleaner',2000,'9669253754','pallikaranai'),(108,'blesso','house mgmt','cleaner',2000,'9385496642','vijay nagar'),(109,'alamelu','house mgmt','manager',4000,'9312643528','vijay nagar'),(110,'saamy','refreshment mgmt','cashier',7000,'9171672008','pallikaranai'),(111,'radha','refreshment mgmt','cashier',7000,'9996602468','kannigapuram'),(112,'usha','refreshment mgmt','staff',7000,'9681658235','vijay nagar'),(113,'sathya','refreshment mgmt','staff',7000,'9451674335','vijay nagar'),(114,'nikil','refreshment mgmt','cashier',7000,'9566551092','velacherry'),(115,'karthk','refreshment mgmt','cashier',7000,'9264427824','velacherry'),(118,'gayle','parking mgmt','staff',6500,'9414652430','pallikaranai'),(119,'jadhav','parking mgmt','staff',6500,'9724890192','pallikaranai'),(120,'bala','parking mgmt','staff',6500,'9470234721','vijay nagar'),(121,'ramurthy','parking mgmt','staff',6500,'9456296635','kannigapuram'),(122,'kunj','security','watchman',6000,'9949596856','pallikaranai'),(123,'pavithra','security','watchman',6000,'9725795565','velacherry'),(124,'maala','security','usher',6000,'9420012779','vijay nagar'),(125,'ananya','security','usher',6000,'9850688391','velacherry'),(126,'vibab','equipment mgmt','technician',7500,'9170427314','ngo colony'),(127,'bhava','equipment mgmt','technician',7500,'9980508983','velacherry'),(128,'akash','equipment mgmt','technician',7500,'9227574068','ngo colony'),(129,'anish','equipment mgmt','projectionist',7500,'9604390170','velacherry'),(130,'rohit','equipment mgmt','projectionist',7500,'9348445605','pallikaranai'),(131,'shema','helping  mgmt','helper',4000,'9439267530','vijay nagar'),(132,'dheepu','helping  mgmt','helper',4000,'9269315209','kannigapuram'),(133,'priya dharshini','janitor','janitor',7060,'9090909099','besent nagar');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pullingo`
--

DROP TABLE IF EXISTS `pullingo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pullingo` (
  `id` int(3) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `dept` varchar(20) DEFAULT NULL,
  `mobileno` char(10) DEFAULT NULL,
  `residence` varchar(20) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pullingo`
--

LOCK TABLES `pullingo` WRITE;
/*!40000 ALTER TABLE `pullingo` DISABLE KEYS */;
INSERT INTO `pullingo` VALUES (1,'gaythe','ADMIN','9444244910','perrumbakkam','amuku'),(2,'shiva','ADMIN','9445099353','perrumbakkam','dumuku'),(3,'alamelu','MANAGER','8989898989','perrumbakkam','amaal'),(4,'sangee','MANAGER','8939542130','perrumbakam','dumaal');
/*!40000 ALTER TABLE `pullingo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'school'
--

--
-- Dumping routines for database 'school'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-06 19:54:56
