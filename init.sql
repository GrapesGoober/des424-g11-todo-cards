CREATE DATABASE TodoCards;
USE TodoCards;

--
-- Database: `todocards`
--

-- --------------------------------------------------------

--
-- Table structure for table `access`
--

CREATE TABLE `access` (
  `accessId` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `deckId` int(11) NOT NULL,
  `accessType` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `access`
--

INSERT INTO `access` (`accessId`, `username`, `deckId`, `accessType`) VALUES
(2, 'ajarn', 3, 'view'),
(3, 'ajarn', 4, 'view'),
(4, 'ajarn', 5, 'view'),
(5, 'bob', 2, 'edit'),
(6, 'cindy', 3, 'edit'),
(8, 'fay', 5, 'edit'),
(9, 'ajarn', 6, 'edit'),
(10, 'ajarn', 7, 'edit'),
(11, 'bob', 6, 'edit'),
(12, 'cindy', 6, 'edit'),
(14, 'fay', 7, 'edit'),
(16, 'ajarn', 9, 'view'),
(20, 'ajarn', 14, 'edit'),
(29, 'ajarn', 1, 'view'),
(30, 'ajarn', 1, 'edit'),
(43, 'ajarn', 18, 'edit'),
(45, 'cindy', 18, 'edit'),
(47, 'fay', 18, 'edit'),
(48, 'ajarn', 1, 'edit'),
(49, 'cindy', 1, 'edit');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`) VALUES
('admin1'),
('admin2'),
('admin3'),
('admin4');

-- --------------------------------------------------------

--
-- Table structure for table `card`
--

CREATE TABLE `card` (
  `cardid` int(11) NOT NULL,
  `deckId` int(11) NOT NULL,
  `cardName` varchar(50) NOT NULL,
  `cardDescription` text NOT NULL,
  `cardDue` date NOT NULL,
  `cardIsFinished` tinyint(1) NOT NULL,
  `cardColor` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `card`
--

INSERT INTO `card` (`cardid`, `deckId`, `cardName`, `cardDescription`, `cardDue`, `cardIsFinished`, `cardColor`) VALUES
(1, 1, 'Write introduction', '200 words zuzu', '2023-10-17', 0, 'lightblue'),
(2, 1, 'Write abstract', '500 words zuzu', '2023-11-17', 0, 'pink'),
(3, 1, 'Cleaning', 'clean bathroom', '2023-11-15', 0, 'lightgreen'),
(4, 4, 'deanCard1', 'bok bok', '2023-11-16', 1, 'pink'),
(5, 4, 'deanCard2newwww', 'Hello Mars', '2023-11-30', 1, 'lightblue'),
(6, 7, 'deanandfayCard1', 'wakkkkkkkkkk', '2023-11-08', 1, 'pink'),
(7, 7, 'deanandfayCard2', 'i love nicki minaj', '2023-11-30', 1, 'lightgreen'),
(8, 3, 'cindyCard1', '', '2023-11-15', 0, 'lightblue'),
(9, 4, 'ForDeanDelete1', '', '2023-11-13', 0, 'lightblue'),
(11, 3, 'ForCindyDelete1', '', '2023-11-13', 1, 'lightblue'),
(14, 3, 'ForCindyDelete2', '', '2023-11-30', 0, 'lightblue'),
(15, 1, 'testAdding', '', '2023-11-23', 0, 'lightgreen'),
(16, 4, 'deanCard3', 'testAdding', '2023-11-30', 1, 'pink'),
(18, 4, 'deanCard4', 'testAdding2', '2023-11-20', 0, 'lightblue');

-- --------------------------------------------------------

--
-- Table structure for table `deck`
--

CREATE TABLE `deck` (
  `deckid` int(11) NOT NULL,
  `deckName` varchar(50) NOT NULL,
  `deckDescription` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `deck`
--

INSERT INTO `deck` (`deckid`, `deckName`, `deckDescription`) VALUES
(1, 'QuickDeck', 'This is the default deck.'),
(2, 'bobDeck', ''),
(3, 'cindyDecktestEdit', 'i love nicki minaj'),
(4, 'deanDeck', ''),
(5, 'fayDeck', ''),
(6, 'bobandcindyDeck', ''),
(7, 'deanandfayDeck', ''),
(9, 'testDelete2', ''),
(14, 'ajarnDeck1', 'UwU'),
(18, 'ajarnDeckforStudentToview', 'UwU');

-- --------------------------------------------------------

--
-- Table structure for table `share`
--

CREATE TABLE `share` (
  `code` varchar(20) NOT NULL,
  `deckId` int(11) NOT NULL,
  `type` varchar(4) NOT NULL,
  `expires` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `share`
--

INSERT INTO `share` (`code`, `deckId`, `type`, `expires`) VALUES
('TWuhSSm8tG0WXJT', 3, 'edit', '2023-11-18 14:34:11'),
('x1iRz8a4ZtSBDfa', 6, 'edit', '2023-11-18 14:33:27'),
('ZDGq45VFJAHFyWB', 1, 'edit', '2023-11-18 16:21:25');

-- --------------------------------------------------------

--
-- Table structure for table `subcard`
--

CREATE TABLE `subcard` (
  `scardid` int(11) NOT NULL,
  `cardID` int(11) NOT NULL,
  `scardName` varchar(50) NOT NULL,
  `scardIsFinished` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `subcard`
--

INSERT INTO `subcard` (`scardid`, `cardID`, `scardName`, `scardIsFinished`) VALUES
(1, 1, 'write intro', 0),
(2, 2, 'find motivation(to do this work)', 0),
(3, 4, 'deancard1subcard1New', 0),
(4, 4, 'deancard1subcard2', 1),
(5, 6, 'deanandfayCard1subcard1', 0),
(6, 8, 'cindyCard1subcard1', 1),
(7, 4, 'TestDeanDelete1', 1),
(9, 8, 'TestCindyDelete1', 1),
(10, 8, 'cindyCard1Subcard3', 0),
(11, 8, 'cindyCard1Subcard4', 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`) VALUES
('admin1', 'c59c3b0b037dc96ad3ca912c8139a3dde54514f2eef83dd70222305c7bcb083e32c88ee39b7e0f69ab3b275932e1c3c2'),
('admin2', '7a4c416299d97f30a2826885394dea5e3c92349feb867d01cc2e26850f1262cd4d377110946cd461ec5768e76edd631a'),
('admin3', 'd43c2fa938979411f1a8a8528ba7d94d8e823cf17724b60e0a9f51be631c3619436b2fb5eb6605c779e5eb3d505515cc'),
('admin4', '02ebe5ba2c0855775c207fb05e34e0b9648e6c8b52fd9504a8dfbee7a5a6e29ecd20c5d397a5ceabc64c776070737ebf'),
('ajarn', '6a195e4ec0e9de6a5d35562e4f920e72a57d4b9750ba00964756d2e9ff3290123ad74d0b75edf4f77d1c2ebe3d6c10c7'),
('bob', '4cbeba55bcfada7cf0142c53c101d9ac770abb26d02235b6f71a77d6d7f86bb10ac1e543dd8cbafcf8952c2d40528297'),
('cindy', '42e97aa817224cb8b2d50562f2fb2933bef91495f6166b1e7f33701765db0cac598fd8abd828b5a92ae56a8d17f5eb3b'),
('fay', '1429511ebd6b934780d07ae90f6715c018f97ace7001302dac2488e8a74ce8f311f1212d3c3154943757be6e80897a09'),
('testdelete1', '99e0536ac81827634d0fe73dd929530bb3f7b08a8e274fb6fdc5b37da2f53cf84f844ca8557347db78f3ef9808e1c115'),
('testdelete2', 'b1028582be83cbdea1d41accf9be21f0183798177200255111bb643df4dc260ed45db01694b87f5121330d7d675ccbc1'),
('testdelete3', 'f764438690090defb481ce5ab38b76512beb5a47ceb4620af7643f6be6bc7edac91e784bc75f61c756905adb86526f2c'),
('testdelete4', ' 625c127d2edeb1eac7dd8feaf45ce700ca4a9d7524e02bbf1492ca6894918a4cfb578ceb997f4a5785630072f573dd8');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `access`
--
ALTER TABLE `access`
  ADD PRIMARY KEY (`accessId`),
  ADD KEY `access_ibfk_1` (`deckId`),
  ADD KEY `access_ibfk_2` (`username`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `card`
--
ALTER TABLE `card`
  ADD PRIMARY KEY (`cardid`),
  ADD KEY `deckID` (`deckId`);

--
-- Indexes for table `deck`
--
ALTER TABLE `deck`
  ADD PRIMARY KEY (`deckid`);

--
-- Indexes for table `share`
--
ALTER TABLE `share`
  ADD PRIMARY KEY (`code`),
  ADD KEY `share_ibfk_1` (`deckId`);

--
-- Indexes for table `subcard`
--
ALTER TABLE `subcard`
  ADD PRIMARY KEY (`scardid`),
  ADD KEY `cardID` (`cardID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `access`
--
ALTER TABLE `access`
  MODIFY `accessId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `card`
--
ALTER TABLE `card`
  MODIFY `cardid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `deck`
--
ALTER TABLE `deck`
  MODIFY `deckid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `subcard`
--
ALTER TABLE `subcard`
  MODIFY `scardid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `access`
--
ALTER TABLE `access`
  ADD CONSTRAINT `access_ibfk_1` FOREIGN KEY (`deckId`) REFERENCES `deck` (`deckid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `access_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `card`
--
ALTER TABLE `card`
  ADD CONSTRAINT `card_ibfk_1` FOREIGN KEY (`deckId`) REFERENCES `deck` (`deckid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `share`
--
ALTER TABLE `share`
  ADD CONSTRAINT `share_ibfk_1` FOREIGN KEY (`deckId`) REFERENCES `deck` (`deckid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `subcard`
--
ALTER TABLE `subcard`
  ADD CONSTRAINT `subcard_ibfk_1` FOREIGN KEY (`cardID`) REFERENCES `card` (`cardid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

DROP USER IF EXISTS 'user';
CREATE USER 'user' IDENTIFIED BY 'user123'; 
GRANT SELECT, INSERT ON * TO 'user' IDENTIFIED BY 'user123';
GRANT UPDATE, DELETE ON `deck` TO 'user' IDENTIFIED BY 'user123';
GRANT UPDATE, DELETE ON `card` TO 'user' IDENTIFIED BY 'user123';
GRANT UPDATE, DELETE ON `subcard` TO 'user' IDENTIFIED BY 'user123';
GRANT DELETE ON `access` TO 'user' IDENTIFIED BY 'user123';
GRANT DELETE ON `share` TO 'user' IDENTIFIED BY 'user123';
FLUSH PRIVILEGES;

DROP USER IF EXISTS superadmin;
CREATE USER IF NOT EXISTS 'superadmin' IDENTIFIED BY 'superadmin123'; 
GRANT SELECT ON * TO 'superadmin' IDENTIFIED BY 'superadmin123';
GRANT DELETE ON `user` TO 'superadmin' IDENTIFIED BY 'superadmin123';
GRANT DELETE ON `deck` TO 'superadmin' IDENTIFIED BY 'superadmin123';
FLUSH PRIVILEGES;