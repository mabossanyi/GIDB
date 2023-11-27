/*
	Author: Marc-Andre Bossanyi
	Email: ma.bossanyi@gmail.com
	Creation Date: 2023/11/26
	Last Updated: 2023/11/26
*/

-- Script CREATE for the table "Element"
CREATE TABLE Element(
	idElement SERIAL NOT NULL,
	name VARCHAR(12) NOT NULL,
	isDeleted BOOL NOT NULL, 
	CONSTRAINT pk_idElement PRIMARY KEY (idElement)
);


-- Script CREATE for the table "Weapon"
CREATE TABLE Weapon(
	idWeapon SERIAL NOT NULL, 
	name VARCHAR(14) NOT NULL, 
	isDeleted BOOL NOT NULL, 
	CONSTRAINT pk_idWeapon PRIMARY KEY (idWeapon)
);


-- Script CREATE for the table "Character"
CREATE TABLE Character(
	idCharacter SERIAL NOT NULL, 
	name VARCHAR(29) NOT NULL, 
	rarity INT NOT NULL, 
	idElement INT NOT NULL, 
	idWeapon INT NOT NULL, 
	isOwned BOOL NOT NULL, 
	isDeleted BOOL NOT NULL, 
	CONSTRAINT pk_idCharacter PRIMARY KEY (idCharacter),
	CONSTRAINT fk_idElement FOREIGN KEY (idElement) REFERENCES Element(idElement),
	CONSTRAINT fk_idWeapon FOREIGN KEY (idWeapon) REFERENCES Weapon(idWeapon)
);


-- Script CREATE for the table "Stat"
CREATE TABLE Stat(
	idStat SERIAL NOT NULL,
	name VARCHAR(55) NOT NULL, 
	isDeleted BOOL NOT NULL, 
	CONSTRAINT pk_idStat PRIMARY KEY (idStat)
);


-- Script CREATE for the table "Slot"
CREATE TABLE Slot(
	idSlot SERIAL NOT NULL, 
	name VARCHAR(17) NOT NULL, 
	isDeleted BOOL NOT NULL, 
	CONSTRAINT pk_idSlot PRIMARY KEY (idSlot)
);


-- Script CREATE for the table "CharacterStat"
CREATE TABLE CharacterStat(
	idCharacter INT NOT NULL, 
	idSlot INT NOT NULL, 
	idStat INT NOT NULL, 
	CONSTRAINT pk_idCharacterStat PRIMARY KEY (idCharacter, idSlot), 
	CONSTRAINT fk_idCharacter FOREIGN KEY (idCharacter) REFERENCES Character(idCharacter),
	CONSTRAINT fk_idSlot FOREIGN KEY (idSlot) REFERENCES Slot(idSlot),
	CONSTRAINT fk_idStat FOREIGN KEY (idStat) REFERENCES Stat(idStat)
);


-- Script CREATE for the table "Item"
CREATE TABLE Item(
	idItem SERIAL NOT NULL, 
	name VARCHAR(38) NOT NULL, 
	isDeleted BOOL NOT NULL, 
	CONSTRAINT pk_idItem PRIMARY KEY (idItem)
);


-- Script CREATE for the table "CharacterItem"
CREATE TABLE CharacterItem(
	idCharacter INT NOT NULL, 
	idSlot INT NOT NULL, 
	idItem INT NOT NULL, 
	CONSTRAINT pk_CharacterItem PRIMARY KEY (idCharacter, idSlot, idItem), 
	CONSTRAINT fk_idCharacter FOREIGN KEY (idCharacter) REFERENCES Character(idCharacter),
	CONSTRAINT fk_idSlot FOREIGN KEY (idSlot) REFERENCES Slot(idSlot),
	CONSTRAINT fk_idItem FOREIGN KEY (idItem) REFERENCES Item(idItem)
);


-- Script CREATE for the table "ItemsSet"
CREATE TABLE ItemsSet(
	idItem INT NOT NULL, 
	quantity INT NOT NULL, 
	description VARCHAR(1255) NOT NULL, 
	CONSTRAINT pk_idItemsSet PRIMARY KEY (idItem, quantity), 
	CONSTRAINT fk_idItem FOREIGN KEY (idItem) REFERENCES Item(idItem)
);

