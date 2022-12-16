-- phpMyAdmin SQL Dump

-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 15, 2022 at 08:29 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `control_asistencia`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `r_salida` (IN `huella_i` INT)   BEGIN  
      SET @exit = (SELECT salida FROM turnos INNER JOIN huellas on turnos.usuarios_idusuarios = huellas.usuarios_idusuarios
      INNER JOIN usuarios on usuarios.idusuarios = turnos.usuarios_idusuarios
      WHERE huella_i = huellas.idhuellas AND huellas.usuarios_idusuarios = usuarios.idusuarios ORDER BY turnos.idturnos DESC LIMIT 1);
      
      SET @user = (SELECT usuarios.idusuarios FROM usuarios INNER JOIN huellas ON huellas.usuarios_idusuarios = usuarios.idusuarios 
      WHERE huella_i = huellas.idhuellas AND huellas.usuarios_idusuarios = usuarios.idusuarios);
      
      SET @imagen = (SELECT fotos.idfotos FROM fotos
      INNER JOIN usuarios ON usuarios.idusuarios = fotos.usuarios_idusuarios INNER JOIN huellas ON huellas.usuarios_idusuarios = fotos.usuarios_idusuarios WHERE huella_i = huellas.idhuellas AND huellas.usuarios_idusuarios = usuarios.idusuarios ORDER BY fotos.idfotos DESC LIMIT 1);
   
      IF @exit IS NULL THEN
		UPDATE turnos 
        INNER JOIN huellas on turnos.usuarios_idusuarios =  huellas.usuarios_idusuarios
        SET turnos.salida = NOW()
        WHERE huella_i = huellas.idhuellas;
      ELSEIF @exit IS NOT NULL THEN
     	INSERT INTO fotos (usuarios_idusuarios, imagen) VALUES (@user, @imagen);
        INSERT INTO turnos (fotos_idfotos, usuarios_idusuarios, llegada, salida) VALUES(@imagen, @user, NOW(), NULL);
      END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `salidas` (IN `huella_i` INT)   BEGIN  
      SET @exit = (SELECT salida FROM turnos INNER JOIN huellas on turnos.usuarios_idusuarios = huellas.usuarios_idusuarios
      INNER JOIN usuarios on usuarios.idusuarios = turnos.usuarios_idusuarios
      WHERE huella_i = huellas.idhuellas AND huellas.usuarios_idusuarios = usuarios.idusuarios);
   
      IF @exit IS NULL THEN
		 UPDATE turnos 
        INNER JOIN huellas on turnos.usuarios_idusuarios =     huellas.usuarios_idusuarios
        SET turnos.salida = NOW()
        WHERE huella_i = huellas.idhuellas;
      END IF;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `cargos`
--

CREATE TABLE `cargos` (
  `id_cargo` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cargos`
--

INSERT INTO `cargos` (`id_cargo`, `nombre`) VALUES
(1, 'Gerente'),
(2, 'Limpieza'),
(3, 'Vigilante');

-- --------------------------------------------------------

--
-- Table structure for table `fotos`
--

CREATE TABLE `fotos` (
  `idfotos` int(10) UNSIGNED NOT NULL,
  `usuarios_idusuarios` int(10) UNSIGNED NOT NULL,
  `imagen` longblob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fotos`
--

INSERT INTO `fotos` (`idfotos`, `usuarios_idusuarios`, `imagen`) VALUES
(1, 1, ''),
(2, 2, ''),
(3, 3, ''),
(4, 4, ''),
(5, 5, ''),
(6, 6, ''),
(7, 7, ''),
(8, 8, ''),
(9, 9, ''),
(10, 10, ''),
(17, 1, ''),
(18, 1, 0x3137),
(19, 1, 0x3138),
(20, 1, 0x3139),
(21, 1, 0x3230),
(22, 1, 0x3231);

-- --------------------------------------------------------

--
-- Table structure for table `horarios`
--

CREATE TABLE `horarios` (
  `idhorarios` int(10) UNSIGNED NOT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_fin` time DEFAULT NULL,
  `dia` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `horarios`
--

INSERT INTO `horarios` (`idhorarios`, `hora_inicio`, `hora_fin`, `dia`) VALUES
(1, '17:47:42', '09:28:03', NULL),
(2, '08:46:08', '21:27:38', NULL),
(3, '07:12:23', '02:11:19', NULL),
(4, '09:08:47', '09:58:08', NULL),
(5, '02:10:43', '07:55:01', NULL),
(6, '01:12:01', '04:24:27', NULL),
(7, '09:42:04', '03:00:21', NULL),
(8, '19:10:10', '07:59:22', NULL),
(9, '05:57:54', '18:14:53', NULL),
(10, '23:32:35', '16:44:54', NULL),
(11, '04:07:37', '01:38:59', NULL),
(12, '09:11:38', '12:11:00', NULL),
(13, '10:32:45', '05:38:38', NULL),
(14, '07:14:16', '16:56:54', NULL),
(15, '09:39:22', '13:17:42', NULL),
(16, '17:45:13', '09:12:14', NULL),
(17, '22:07:34', '11:51:39', NULL),
(18, '19:49:13', '09:55:05', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `huellas`
--

CREATE TABLE `huellas` (
  `idhuellas` int(10) UNSIGNED NOT NULL,
  `usuarios_idusuarios` int(10) UNSIGNED NOT NULL,
  `huehuella` blob NOT NULL,
  `huenombre` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `huellas`
--

INSERT INTO `huellas` (`idhuellas`, `usuarios_idusuarios`, `huehuella`, `huenombre`) VALUES
(1, 1, 0x00f83901c82ae3735cc0413709ab71f08814559220fb486a94e0c1b673d670097312bfcc1f451643d84f24507efc2b9ab399ad76c6552487bb49c9f960143143ea38577b9bcb177761d03e7130daaa416a933695736fa21a9a770ba03f5a6adb53facc519e62b37300016ce4eeb09ebc2096c54348c4096cc60192d45f743d2d54e3395fb92cedb16f32cf04df263b9d4092d22e1d4e47a4665d8426475bee5d65bd1204d7a89082b777722cbaa454c229f10eb6f7351de418b691f3d6a1435b8b4123515eafdc24b2f4d0cef9c89d0ff31b4225da247625e4bb8c47bfeef8bb7972f7cca960082875c076e32dbb8d924c1401061669d6ca76cf3ef50c81f32a8de3c451d28a6bafc5bcc3b620a4010b78c7388853b9edaa57d88bb0b7d7cbd0dc310b0a97c8cb700a7792fd3c8ad4b1636067f5fcbd0b9c7afe95160f6f00f84d01c82ae3735cc0413709ab71f08b145592230b11c04514a3640c76bc5db456b0f693e27f8057ccb47a4a11ed05534a4170a85cc5bb2fb1d22f5f418e4a20f54970b5819e8163b8b191ff611d0fbbdbcff0a3fdd51a9cd685bc49266da69e8baaaf118844ce6e8b901b642d4861cedc8bb4505e092ca859271d91a0cf9bbc20767362be4e051c67b9bf30a5e5baf40cf3c6b8e02bc5c90bc9cbb3664d9166fb36d3c3c3f9ba7d553897db1f6b541bd6b2a476112f2d138fc6a40e3d054847d278655bae08d394c4181685e8f02866a711a85b13756429bca0d0f79da83defe01313d22e225c95913e7fc9818121c51c55702470a038d97412730c96bd11013ac4fa5e5950676b24888c1a97ecf623be1a1d0bba3cc724e15f5a54331afe4ec219953b7a5316da2dc13d7753b180cb6092df7e9002bce3aad8c94424297f3bc90c88ef4e5d6316c2df7e218b11d95f6f00f87f01c82ae3735cc0413709ab71f0d714559253d008bbcabb268bda890ef382bb7d62fee684fcd101eaf12be91a1eecbbe536770e656fbe6c22acc68c69dd4b672eb15d33c6183bef1835718665cd58d7eb51b91305d70b394778881fada33fd50bc5ca4ee597b264384dc4349adbf3c1aa823469e21c77dc64bbdd31d9c2a7403fa63f1d1e4baa1c6beeb1a57016b91de231b45a2e72e09078c991725c312e2576fc3d9cde37d48dccecec0ccb1a5b765c23404c36c50764082ed8aac4cdcc7fcd738e827aa08914d1a83abf143fe9eadfaa3a4a5fb347a1eb81e70cc8d6219ac617b4e59726d5b8f48bd4f52a3233283c3a0b6d1cf35f4f9d534a0b42ae1afa07557b1d47b82d678d431d062d8bc5b228c70e9df3e9a4ad7981143c5dd3be9408dd22a14352aa02211f0e99f5016ab7774d80678278124aa013598f7742bb16fa090109f02e40ead68515958ca83f2c70587e3c8339a99d390ebe9d5be9b800d5a8c2924d7f4809f47842d7ae9a443c654a3ce62ed70897f2e1910f882cc134006f00e87f01c82ae3735cc0413709ab71f09c1455928ab63230c9be8ea93ee5f89dcb5f37a9f1485f19e588bce9440f6427c0c60b62c302d800c578c9346d79f53f233e2d97f83113f5c81214a7709f944c5a26d0349b26a9e8225b4c6e0e3e38ff26bed8cb7a601dad05ee4ee6a1d34d3112e1187dcf8ab13ddcff587e8d1b9a76c04d306eac1d2830ef20a244d5405a1a2f0e3c27b6646311345f3d9c1aebe886225f257c0fa1a7d169d8868a2e154cd80353e37f124cd9b48d415fd22214d4621f87ff9faf326084e0e7c7f0f715be619c9ccd67a16e8ac7ab10a7b9d2b49f65ade236f25ebfa980cda81b2878a55f2783100d6f74d1e5a4cacbe5d0e8cbe945f905bef1a6ce3caeb45db402bce1b8dcf57bcc6336c611e78b66de036e7695b0085f89b7f8f423cdc9386ac61de84e8e252235841c7d45f7c07ba13e631bdbae57d6499177df467a1300bf9565011599194f050b29cd58303d798016f96832a6da1b0769314bd650e3b22e4d10456c7338569fb7c6870f78b2716b272b0986d3e588836f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 'sebas'),
(2, 2, 0x00f87f01c82ae3735cc0413709ab71f0e8145592a8ff2d5aa2c0fdc30d6e970cf0d1b64669c044cf9ce60abfb958dafd3b395547c61974d59849748266f6857f3eff2081c0c2f0937273b2e90d985bf6c3037cf641498b8df581afb13adfc447d744e78b075495e88d6672c6dda8920c0b79eef05f1255424aad497710e6ca824251b8f7bbd4fc8aaa1a24ab3ae772ac21e9266104f0ea21249b145ad59a75b482f84fbd41c31a584fc137b34afccf432b5594cf85e8ade51abc9d436d03010c2de270914066bd4c88bb1c29f5e993b3a16a42893c80c15859a0cda68c21d0b963299611d8f11b216afc6dd91479b9d6b0a5dbf01a8ef2db0a20293630dfe391f5559a3169f1b3ea3f980682b5dbf647a4b024a21f2b1ce14ac78d75114c589148d12c5ef80269f2ab6a30c71e794a4e356b67dd0e4763f2d7c57fb710cd04bf755d3fd4933c47ee70d52b673e6c93bdb541e9b5da8175a21d840148d6edc158a09f43e936f11c2c3a2346862d88a58656150609920662fa0cbc34efd145bf62be76996f00f87b01c82ae3735cc0413709ab71f0d514559214bb393ef930ba4cebc614d8035781c41914a91286bb47b4ec3a214776b285d2fd8bc95441873734abe347e5ba192f21ea6bbbe579e6ed14c78cb63f50983ec1a1649cd735cf45391d4c3ca2cb89a02bd217a1c01d96fde53af1a300eb9959b9d4903b6ce39bc3ce609a2eed4a7b9da633a1b196548af9e2f4e45b5d73a449115751a4c07572fbb5877b430357b782287984ac11c15b8919c5e4730dd09ef7ea970252fb7619d392c56466c9d6e1856c4944ccefc8c103ba42db26e0ce8945238ec11aadcfc049e17c39b5dd01cb74195e3ad10760c6675e38584e9891171894ad761b19b84932f0dc28741906473a0ec11b6db4419c25b646dbc6e1e886e9487e1487f853809d31be0666df763fa7cc2bb32bfe01cdb25cab4023cbb0c3756569b041d95cec3610351378c5fd34a65460fcb7a521a5227441e13e02d352143896a52514520926270a795f9f0db055f2858d09eb630bad9e6684f8694d79ce76782cfaead86618db879d7c6f00f88101c82ae3735cc0413709ab71f0d714559253d5cd3aeef19700ec8e4e9451958457ce8f8fc0c1c928f1417c2d1a1a57632e315c80a61f8913c5550f238c7430cab920d295a7138715e33e3119433a1e839c918e4e307ab6f869846f0096c0c2142dc96e3e970f15ac045a44acd6803133a6c7d94e92c5a91ab616f4860114d041d26126583cb28675a8cb56f9b0d3573992cf0a8cf52117e678f3cdc00d29fcbacb3899ebc5ba195955944173f32b26caf3266defe24a15c578358edcc58f95da6feaa2f7caf0067dcc99680c50b84d040a382785f1a0d95e20897add911d76aef2c9056105fa74892d950349f5c09a2ea9362ed1dc3e4021292089c986d933071dc3d0b3da915ee7347cbdec4cd84f5a4921a6f455e9ea2444353606d3f13b508a1c353ca5cfb7fe80b29cc3aa143c6e3c33291715472c4360e70ad16de46274e1d7e0d69ddd80608aaa72c60effb470ebc80895876e698ebce31b353b2ed4c3dc5642715810989e7bf75eac90634951c184a006333f5867d1d14a5f5385f5c0777e6f00e88101c82ae3735cc0413709ab71b08a145592d2a4d8a6cbd278b6730d1833cb6e218dc81d67824eddd3ab8d309c9bb9d15cc6915d0d2a5a3c11c86f2ed8baffb1d42c76747a5bff880177e78881063d3aaaed6c0a928d4d5e14fcd1afe477e35c366b7e5efc9e7918afdee382f279e717e4b9afd8dd062f216ee42b279b5b2c92db21432d4ca74f75ffafb1fa4895a52b57f528a33245c391ade5b902ce61fd2a51c9cccbf004d24108696d2351e4d501b7766201335dfd3c04d8005909046259706f1a127333a710b534898e6862b22e11aaebfc9c5bdd6a0a1b53da4434dc41bc676c088aeffa58ef13abf1f1c184680669291d663542b4ffb9dc5ff1a3aa250d7a7d110bd89577ad0001803bdc732b23dc6bbcb97641c877408e2e0b06f1fb2efb62e7fe30ea10832b8e7a4ad4771dacbc4d79184f308ddbe8a818505849c216f5e838e42d0c261c6850322e49e575c8c05be24e9ede334964f83038d8d12ef57711d6cfba31da1d2299eabeb04935b460297dd3bd2bb0623762fcfc753415ae95806f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 'lila');

-- --------------------------------------------------------

--
-- Table structure for table `turnos`
--

CREATE TABLE `turnos` (
  `idturnos` int(10) UNSIGNED NOT NULL,
  `fotos_idfotos` int(10) UNSIGNED NOT NULL,
  `usuarios_idusuarios` int(10) UNSIGNED NOT NULL,
  `llegada` datetime DEFAULT NULL,
  `salida` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `turnos`
--

INSERT INTO `turnos` (`idturnos`, `fotos_idfotos`, `usuarios_idusuarios`, `llegada`, `salida`) VALUES
(1, 1, 1, '2021-12-12 17:47:42', '2022-12-15 14:26:19'),
(2, 2, 2, '2021-12-12 08:46:08', '2022-12-15 14:26:38'),
(20, 20, 1, '2022-12-15 14:26:11', '2022-12-15 14:26:19'),
(21, 21, 1, '2022-12-15 14:26:29', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `idusuarios` int(10) UNSIGNED NOT NULL,
  `cargo` int(11) NOT NULL,
  `name_01` varchar(50) DEFAULT NULL,
  `name_02` varchar(50) DEFAULT NULL,
  `lastname01` varchar(50) DEFAULT NULL,
  `lastname02` varchar(50) DEFAULT NULL,
  `fecha_nac` datetime DEFAULT NULL,
  `identificacion` int(10) UNSIGNED DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `telefono` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`idusuarios`, `cargo`, `name_01`, `name_02`, `lastname01`, `lastname02`, `fecha_nac`, `identificacion`, `sexo`, `email`, `telefono`) VALUES
(1, 1, 'Belva', 'Kassie', 'Flemmich', 'Mayne', '2021-10-10 18:28:31', 4294967295, 'M', 'kmayne0@ucsd.edu', 290),
(2, 1, 'Carry', 'Yurik', 'Gibby', 'Sherrin', '2022-02-19 00:27:14', 674822749, 'M', 'ysherrin1@gizmodo.com', 761),
(3, 1, 'Nial', 'Ancell', 'Martyntsev', 'Leeke', '2022-06-03 02:20:05', 4294967295, 'M', 'aleeke2@examiner.com', 206),
(4, 1, 'Karena', 'Ambrosio', 'Ladlow', 'Willcox', '2022-11-05 18:29:19', 611106957, 'H', 'awillcox3@angelfire.com', 742),
(5, 2, 'Juliann', 'Susann', 'Stanbro', 'Neller', '2022-10-19 17:24:14', 69676372, 'M', 'sneller4@stumbleupon.com', 457),
(6, 2, 'Francisco', 'Marisa', 'Vine', 'Iacovelli', '2022-06-29 14:20:53', 110919203, 'M', 'miacovelli5@creativecommons.org', 736),
(7, 2, 'Veradis', 'Jobyna', 'Jacklings', 'Willis', '2021-09-18 14:44:31', 3793751678, 'M', 'jwillis6@sakura.ne.jp', 899),
(8, 3, 'Glenda', 'Maxim', 'Van Arsdale', 'Josefsohn', '2022-04-19 06:40:39', 4294967295, 'H', 'mjosefsohn7@weather.com', 237),
(9, 3, 'Doralin', 'Lucienne', 'Ivanyushin', 'Overstreet', '2022-01-30 19:19:00', 1203533861, 'M', 'loverstreet8@ucoz.ru', 662),
(10, 3, 'Timmy', 'Matilde', 'McLinden', 'Tevlin', '2022-09-18 14:12:54', 2533866954, 'H', 'mtevlin9@alibaba.com', 124),
(11, 2, 'Min', 'Yoongi', 'Flemmich', 'Mayne', '2021-10-10 23:23:31', 422333395, 'M', 'minyoongi@edu.co', 32222);

-- --------------------------------------------------------

--
-- Table structure for table `usuarios_has_horarios`
--

CREATE TABLE `usuarios_has_horarios` (
  `usuarios_idusuarios` int(10) UNSIGNED NOT NULL,
  `horarios_idhorarios` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usuarios_has_horarios`
--

INSERT INTO `usuarios_has_horarios` (`usuarios_idusuarios`, `horarios_idhorarios`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 12);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cargos`
--
ALTER TABLE `cargos`
  ADD PRIMARY KEY (`id_cargo`);

--
-- Indexes for table `fotos`
--
ALTER TABLE `fotos`
  ADD PRIMARY KEY (`idfotos`),
  ADD KEY `fotos_FKIndex1` (`usuarios_idusuarios`);

--
-- Indexes for table `horarios`
--
ALTER TABLE `horarios`
  ADD PRIMARY KEY (`idhorarios`);

--
-- Indexes for table `huellas`
--
ALTER TABLE `huellas`
  ADD PRIMARY KEY (`idhuellas`),
  ADD KEY `huellas_FKIndex1` (`usuarios_idusuarios`);

--
-- Indexes for table `turnos`
--
ALTER TABLE `turnos`
  ADD PRIMARY KEY (`idturnos`),
  ADD KEY `turnos_FKIndex1` (`usuarios_idusuarios`),
  ADD KEY `turnos_FKIndex2` (`fotos_idfotos`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idusuarios`),
  ADD KEY `fk_cargo` (`cargo`);

--
-- Indexes for table `usuarios_has_horarios`
--
ALTER TABLE `usuarios_has_horarios`
  ADD PRIMARY KEY (`usuarios_idusuarios`,`horarios_idhorarios`),
  ADD KEY `usuarios_has_horarios_FKIndex1` (`usuarios_idusuarios`),
  ADD KEY `usuarios_has_horarios_FKIndex2` (`horarios_idhorarios`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cargos`
--
ALTER TABLE `cargos`
  MODIFY `id_cargo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `fotos`
--
ALTER TABLE `fotos`
  MODIFY `idfotos` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `horarios`
--
ALTER TABLE `horarios`
  MODIFY `idhorarios` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `huellas`
--
ALTER TABLE `huellas`
  MODIFY `idhuellas` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `turnos`
--
ALTER TABLE `turnos`
  MODIFY `idturnos` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idusuarios` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `fotos`
--
ALTER TABLE `fotos`
  ADD CONSTRAINT `fotos_ibfk_1` FOREIGN KEY (`usuarios_idusuarios`) REFERENCES `usuarios` (`idusuarios`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `huellas`
--
ALTER TABLE `huellas`
  ADD CONSTRAINT `huellas_ibfk_1` FOREIGN KEY (`usuarios_idusuarios`) REFERENCES `usuarios` (`idusuarios`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `turnos`
--
ALTER TABLE `turnos`
  ADD CONSTRAINT `turnos_ibfk_1` FOREIGN KEY (`usuarios_idusuarios`) REFERENCES `usuarios` (`idusuarios`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `turnos_ibfk_2` FOREIGN KEY (`fotos_idfotos`) REFERENCES `fotos` (`idfotos`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `fk_cargo` FOREIGN KEY (`cargo`) REFERENCES `cargos` (`id_cargo`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `usuarios_has_horarios`
--
ALTER TABLE `usuarios_has_horarios`
  ADD CONSTRAINT `usuarios_has_horarios_ibfk_1` FOREIGN KEY (`usuarios_idusuarios`) REFERENCES `usuarios` (`idusuarios`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `usuarios_has_horarios_ibfk_2` FOREIGN KEY (`horarios_idhorarios`) REFERENCES `horarios` (`idhorarios`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
