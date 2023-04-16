-- MySQL Script generated by MySQL Workbench
-- Wed Feb  8 04:10:00 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema chugunova
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema chugunova
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `chugunova` DEFAULT CHARACTER SET utf8 ;
USE `chugunova` ;

-- -----------------------------------------------------
-- Table `chugunova`.`usr`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chugunova`.`usr` (
  `idusr` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idusr`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `chugunova`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chugunova`.`product` (
  `idp` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `descr` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`idp`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `chugunova`.`invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `chugunova`.`invoice` (
  `idinv` INT NOT NULL,
  `idusr` INT NOT NULL,
  `idp` INT NOT NULL,
  `cost` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`idinv`),
  INDEX `usr_idx` (`idusr` ASC) VISIBLE,
  INDEX `prod_idx` (`idp` ASC) VISIBLE,
  CONSTRAINT `usr`
    FOREIGN KEY (`idusr`)
    REFERENCES `chugunova`.`usr` (`idusr`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `prod`
    FOREIGN KEY (`idp`)
    REFERENCES `chugunova`.`product` (`idp`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
