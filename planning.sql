-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema plannings
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `plannings` ;

-- -----------------------------------------------------
-- Schema plannings
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `plannings` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci ;
-- -----------------------------------------------------
-- Schema plannings
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Table `plannings`.`facultes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`facultes` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `updated_at` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` VARCHAR(45) NULL DEFAULT NULL,
  UNIQUE INDEX `code_UNIQUE` (`code` ASC) VISIBLE,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `plannings`.`departements`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`departements` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NULL,
  `facultes_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `code_UNIQUE` (`code` ASC) VISIBLE,
  INDEX `fk_departements_facultes1_idx` (`facultes_id` ASC) VISIBLE,
  CONSTRAINT `fk_departements_facultes1`
    FOREIGN KEY (`facultes_id`)
    REFERENCES `plannings`.`facultes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `plannings`.`classes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`classes` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  `effectif` INT UNSIGNED NOT NULL,
  `departements_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `code_UNIQUE` (`code` ASC) VISIBLE,
  INDEX `fk_niveaus_departements1_idx` (`departements_id` ASC) VISIBLE,
  CONSTRAINT `fk_niveaus_departements1`
    FOREIGN KEY (`departements_id`)
    REFERENCES `plannings`.`departements` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `plannings`.`etudiants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`etudiants` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `matricule` VARCHAR(45) NULL,
  `noms` VARCHAR(255) NOT NULL,
  `adresse` VARCHAR(255) NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `classes_id` INT UNSIGNED NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `matricule_UNIQUE` (`matricule` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  INDEX `fk_etudiants_niveaus1_idx` (`classes_id` ASC) VISIBLE,
  UNIQUE INDEX `niveaus_id_UNIQUE` (`classes_id` ASC) VISIBLE,
  CONSTRAINT `fk_etudiants_niveaus1`
    FOREIGN KEY (`classes_id`)
    REFERENCES `plannings`.`classes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `plannings`.`enseignants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`enseignants` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `matricule` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `role` ENUM('admin', 'simple', 'chef_departement') NOT NULL DEFAULT 'simple',
  `departements_id` INT UNSIGNED NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `matricule_UNIQUE` (`matricule` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  INDEX `fk_enseignants_departements_idx` (`departements_id` ASC) VISIBLE,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `departements_id_UNIQUE` (`departements_id` ASC) VISIBLE,
  CONSTRAINT `fk_enseignants_departements`
    FOREIGN KEY (`departements_id`)
    REFERENCES `plannings`.`departements` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `plannings`.`ues`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`ues` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  `intitule` VARCHAR(255) NULL,
  `credit` TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `plannings`.`specialites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`specialites` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(255) NULL,
  `classes_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `classes_id`),
  UNIQUE INDEX `code_UNIQUE` (`code` ASC) VISIBLE,
  INDEX `fk_specialites_niveaus1_idx` (`classes_id` ASC) VISIBLE,
  CONSTRAINT `fk_specialites_niveaus1`
    FOREIGN KEY (`classes_id`)
    REFERENCES `plannings`.`classes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `plannings`.`groupes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`groupes` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `code_UNIQUE` (`code` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `plannings`.`plages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`plages` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `jour` VARCHAR(45) NOT NULL,
  `periode` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `jour_UNIQUE` (`jour` ASC, `periode` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `plannings`.`classes_groupes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`classes_groupes` (
  `groupes_id` INT UNSIGNED NULL,
  `classes_id` INT UNSIGNED NULL,
  INDEX `fk_groupes_has_niveaus_niveaus1_idx` (`classes_id` ASC) VISIBLE,
  INDEX `fk_groupes_has_niveaus_groupes1_idx` (`groupes_id` ASC) VISIBLE,
  UNIQUE INDEX `groupes_id_UNIQUE` (`groupes_id` ASC, `classes_id` ASC) VISIBLE,
  CONSTRAINT `fk_groupes_has_niveaus_groupes1`
    FOREIGN KEY (`groupes_id`)
    REFERENCES `plannings`.`groupes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_groupes_has_niveaus_niveaus1`
    FOREIGN KEY (`classes_id`)
    REFERENCES `plannings`.`classes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `plannings`.`enseignes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`enseignes` (
  `ues_id` INT UNSIGNED NOT NULL,
  `enseignants_id` INT UNSIGNED NOT NULL,
  `classes_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`ues_id`, `enseignants_id`, `classes_id`),
  INDEX `fk_ues_has_enseignants_enseignants1_idx` (`enseignants_id` ASC) VISIBLE,
  INDEX `fk_ues_has_enseignants_ues1_idx` (`ues_id` ASC) VISIBLE,
  INDEX `fk_ues_has_enseignants_classes1_idx` (`classes_id` ASC) VISIBLE,
  CONSTRAINT `fk_ues_has_enseignants_ues1`
    FOREIGN KEY (`ues_id`)
    REFERENCES `plannings`.`ues` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ues_has_enseignants_enseignants1`
    FOREIGN KEY (`enseignants_id`)
    REFERENCES `plannings`.`enseignants` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ues_has_enseignants_classes1`
    FOREIGN KEY (`classes_id`)
    REFERENCES `plannings`.`classes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `plannings`.`batiments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`batiments` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `localisation` VARCHAR(45) NULL DEFAULT NULL,
  `facultes_id` INT UNSIGNED NOT NULL,
  `updated_at` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` VARCHAR(45) NULL DEFAULT NULL,
  UNIQUE INDEX `code_UNIQUE` (`code` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  INDEX `fk_batiments_facultes_idx` (`facultes_id` ASC) VISIBLE,
  CONSTRAINT `fk_batiments_facultes`
    FOREIGN KEY (`facultes_id`)
    REFERENCES `plannings`.`facultes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `plannings`.`type_salles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`type_salles` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `description` VARCHAR(45) NULL DEFAULT NULL,
  `updated_at` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` VARCHAR(45) NULL DEFAULT NULL,
  UNIQUE INDEX `code_UNIQUE` (`code` ASC) VISIBLE,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `plannings`.`salles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`salles` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NULL DEFAULT NULL,
  `capacite` INT NOT NULL,
  `etat_electricite` TINYINT NULL DEFAULT NULL,
  `batiments_id` INT UNSIGNED NULL,
  `type_salles_id` INT UNSIGNED NOT NULL,
  `updated_at` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_salles_batiments1_idx` (`batiments_id` ASC) VISIBLE,
  UNIQUE INDEX `code_UNIQUE` (`code` ASC, `batiments_id` ASC) VISIBLE,
  INDEX `fk_salles_type_salles1_idx` (`type_salles_id` ASC) VISIBLE,
  CONSTRAINT `fk_salles_batiments1`
    FOREIGN KEY (`batiments_id`)
    REFERENCES `plannings`.`batiments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_salles_type_salles1`
    FOREIGN KEY (`type_salles_id`)
    REFERENCES `plannings`.`type_salles` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `plannings`.`cours_programmmes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`cours_programmmes` (
  `plages_id` INT UNSIGNED NOT NULL,
  `salles_id` INT UNSIGNED NOT NULL,
  `ues_id` INT UNSIGNED NULL,
  `classes_id` INT UNSIGNED NULL,
  `enseignants_id` INT UNSIGNED NULL,
  PRIMARY KEY (`salles_id`, `plages_id`),
  INDEX `fk_plages_has_salles_salles1_idx` (`salles_id` ASC) VISIBLE,
  INDEX `fk_plages_has_salles_plages1_idx` (`plages_id` ASC) VISIBLE,
  INDEX `fk_plages_has_salles_ues1_idx` (`ues_id` ASC) VISIBLE,
  INDEX `fk_plages_has_salles_classes1_idx` (`classes_id` ASC) VISIBLE,
  INDEX `fk_plages_has_salles_enseignants1_idx` (`enseignants_id` ASC) VISIBLE,
  UNIQUE INDEX `ues_id_UNIQUE` (`ues_id` ASC, `classes_id` ASC) VISIBLE,
  UNIQUE INDEX `enseignants_id_UNIQUE` (`enseignants_id` ASC, `plages_id` ASC) VISIBLE,
  CONSTRAINT `fk_plages_has_salles_plages1`
    FOREIGN KEY (`plages_id`)
    REFERENCES `plannings`.`plages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_plages_has_salles_salles1`
    FOREIGN KEY (`salles_id`)
    REFERENCES `plannings`.`salles` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_plages_has_salles_ues1`
    FOREIGN KEY (`ues_id`)
    REFERENCES `plannings`.`ues` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_plages_has_salles_classes1`
    FOREIGN KEY (`classes_id`)
    REFERENCES `plannings`.`classes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_plages_has_salles_enseignants1`
    FOREIGN KEY (`enseignants_id`)
    REFERENCES `plannings`.`enseignants` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `plannings` ;
USE `plannings` ;

-- -----------------------------------------------------
-- Table `plannings`.`type_ressources`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`type_ressources` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `description` VARCHAR(45) NULL DEFAULT NULL,
  `updated_at` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `code_UNIQUE` (`code` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `plannings`.`ressources`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `plannings`.`ressources` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `description` VARCHAR(45) NULL,
  `facultes_id` INT UNSIGNED NOT NULL,
  `type_ressources_id` INT UNSIGNED NULL,
  `updated_at` VARCHAR(45) NULL,
  `created_at` VARCHAR(45) NULL,
  UNIQUE INDEX `code_UNIQUE` (`code` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  INDEX `fk_ressources_facultes1_idx` (`facultes_id` ASC) VISIBLE,
  INDEX `fk_ressources_type_ressources1_idx` (`type_ressources_id` ASC) VISIBLE,
  CONSTRAINT `fk_ressources_facultes1`
    FOREIGN KEY (`facultes_id`)
    REFERENCES `plannings`.`facultes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ressources_type_ressources1`
    FOREIGN KEY (`type_ressources_id`)
    REFERENCES `plannings`.`type_ressources` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
