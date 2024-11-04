-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2024 at 05:34 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `edu_connect`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add assigned_studentreg', 7, 'add_assigned_studentreg'),
(26, 'Can change assigned_studentreg', 7, 'change_assigned_studentreg'),
(27, 'Can delete assigned_studentreg', 7, 'delete_assigned_studentreg'),
(28, 'Can view assigned_studentreg', 7, 'view_assigned_studentreg'),
(29, 'Can add class_schedules', 8, 'add_class_schedules'),
(30, 'Can change class_schedules', 8, 'change_class_schedules'),
(31, 'Can delete class_schedules', 8, 'delete_class_schedules'),
(32, 'Can view class_schedules', 8, 'view_class_schedules'),
(33, 'Can add course_assign', 9, 'add_course_assign'),
(34, 'Can change course_assign', 9, 'change_course_assign'),
(35, 'Can delete course_assign', 9, 'delete_course_assign'),
(36, 'Can view course_assign', 9, 'view_course_assign'),
(37, 'Can add course_details', 10, 'add_course_details'),
(38, 'Can change course_details', 10, 'change_course_details'),
(39, 'Can delete course_details', 10, 'delete_course_details'),
(40, 'Can view course_details', 10, 'view_course_details'),
(41, 'Can add course_payment', 11, 'add_course_payment'),
(42, 'Can change course_payment', 11, 'change_course_payment'),
(43, 'Can delete course_payment', 11, 'delete_course_payment'),
(44, 'Can view course_payment', 11, 'view_course_payment'),
(45, 'Can add facultyreg', 12, 'add_facultyreg'),
(46, 'Can change facultyreg', 12, 'change_facultyreg'),
(47, 'Can delete facultyreg', 12, 'delete_facultyreg'),
(48, 'Can view facultyreg', 12, 'view_facultyreg'),
(49, 'Can add leave_applications', 13, 'add_leave_applications'),
(50, 'Can change leave_applications', 13, 'change_leave_applications'),
(51, 'Can delete leave_applications', 13, 'delete_leave_applications'),
(52, 'Can view leave_applications', 13, 'view_leave_applications'),
(53, 'Can add studentreg', 14, 'add_studentreg'),
(54, 'Can change studentreg', 14, 'change_studentreg'),
(55, 'Can delete studentreg', 14, 'delete_studentreg'),
(56, 'Can view studentreg', 14, 'view_studentreg'),
(57, 'Can add study_materials', 15, 'add_study_materials'),
(58, 'Can change study_materials', 15, 'change_study_materials'),
(59, 'Can delete study_materials', 15, 'delete_study_materials'),
(60, 'Can view study_materials', 15, 'view_study_materials'),
(61, 'Can add chats', 16, 'add_chats'),
(62, 'Can change chats', 16, 'change_chats'),
(63, 'Can delete chats', 16, 'delete_chats'),
(64, 'Can view chats', 16, 'view_chats');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'educonnect', 'assigned_studentreg'),
(16, 'educonnect', 'chats'),
(8, 'educonnect', 'class_schedules'),
(9, 'educonnect', 'course_assign'),
(10, 'educonnect', 'course_details'),
(11, 'educonnect', 'course_payment'),
(12, 'educonnect', 'facultyreg'),
(13, 'educonnect', 'leave_applications'),
(14, 'educonnect', 'studentreg'),
(15, 'educonnect', 'study_materials'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-03-17 16:10:48.517571'),
(2, 'auth', '0001_initial', '2024-03-17 16:10:48.941931'),
(3, 'admin', '0001_initial', '2024-03-17 16:10:49.057836'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-03-17 16:10:49.067502'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-03-17 16:10:49.080850'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-03-17 16:10:49.148822'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-03-17 16:10:49.203681'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-03-17 16:10:49.220220'),
(9, 'auth', '0004_alter_user_username_opts', '2024-03-17 16:10:49.229158'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-03-17 16:10:49.276989'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-03-17 16:10:49.285469'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-03-17 16:10:49.297940'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-03-17 16:10:49.314303'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-03-17 16:10:49.328309'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-03-17 16:10:49.343915'),
(16, 'auth', '0011_update_proxy_permissions', '2024-03-17 16:10:49.359261'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-03-17 16:10:49.373040'),
(18, 'educonnect', '0001_initial', '2024-03-17 16:10:49.473188'),
(19, 'educonnect', '0002_study_materials', '2024-03-17 16:10:49.486244'),
(20, 'educonnect', '0003_rename_fid_study_materials_sid', '2024-03-17 16:10:49.508855'),
(21, 'educonnect', '0004_chats', '2024-03-17 16:10:49.533009'),
(22, 'educonnect', '0005_rename_card_name_course_payment_order_id_and_more', '2024-03-17 16:10:49.577855'),
(23, 'educonnect', '0006_auto_20240310_2123', '2024-03-17 16:10:49.612277'),
(24, 'educonnect', '0007_remove_study_materials_sid', '2024-03-17 16:10:49.626359'),
(25, 'educonnect', '0008_auto_20240312_2240', '2024-03-17 16:10:49.645168'),
(26, 'educonnect', '0009_study_materials_s_id', '2024-03-17 16:10:49.659260'),
(27, 'educonnect', '0010_remove_study_materials_s_id', '2024-03-17 16:10:49.667976'),
(28, 'sessions', '0001_initial', '2024-03-17 16:10:49.705528');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('vn554ia439zoz8qhwggyoaje70vj47h6', 'e30:1rlubK:greVweD193Cf3C1TZfcLZxpAOaccTelu1JwzgSD0BSU', '2024-03-31 17:47:14.256343');

-- --------------------------------------------------------

--
-- Table structure for table `educonnect_assigned_studentreg`
--

CREATE TABLE `educonnect_assigned_studentreg` (
  `id` bigint(20) NOT NULL,
  `name` varchar(150) NOT NULL,
  `city` varchar(150) NOT NULL,
  `place` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `sid` varchar(150) NOT NULL,
  `fid` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `educonnect_assigned_studentreg`
--

INSERT INTO `educonnect_assigned_studentreg` (`id`, `name`, `city`, `place`, `email`, `phone`, `sid`, `fid`) VALUES
(1, 'Akhil S', 'Kannur', 'Thalassery', 'akhil@gmail.com', '8958392028', '1', '1');

-- --------------------------------------------------------

--
-- Table structure for table `educonnect_chats`
--

CREATE TABLE `educonnect_chats` (
  `id` bigint(20) NOT NULL,
  `s_id` varchar(150) NOT NULL,
  `m_id` varchar(150) NOT NULL,
  `s_msg` varchar(150) NOT NULL,
  `m_msg` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `educonnect_class_schedules`
--

CREATE TABLE `educonnect_class_schedules` (
  `id` bigint(20) NOT NULL,
  `typee` varchar(150) NOT NULL,
  `fid` varchar(150) NOT NULL,
  `date` varchar(150) NOT NULL,
  `link` varchar(150) NOT NULL,
  `message` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `host_key` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `educonnect_course_assign`
--

CREATE TABLE `educonnect_course_assign` (
  `id` bigint(20) NOT NULL,
  `course_id` varchar(150) NOT NULL,
  `std_name` varchar(150) NOT NULL,
  `sid` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `educonnect_course_details`
--

CREATE TABLE `educonnect_course_details` (
  `id` bigint(20) NOT NULL,
  `name` varchar(150) NOT NULL,
  `details` varchar(150) NOT NULL,
  `startdate` varchar(150) NOT NULL,
  `enddate` varchar(150) NOT NULL,
  `amount` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `educonnect_course_details`
--

INSERT INTO `educonnect_course_details` (`id`, `name`, `details`, `startdate`, `enddate`, `amount`) VALUES
(1, 'Introduction to Computer Science', 'Basics of computer science, covering fundamental concepts such as algorithms, data structures, and simple programming.', '2024-05-08', '2024-08-01', '7000'),
(2, 'Web Development Fundamentals', 'An introduction to HTML, CSS, and JavaScript, focusing on building static websites.', '2024-06-17', '2024-10-16', '6000');

-- --------------------------------------------------------

--
-- Table structure for table `educonnect_course_payment`
--

CREATE TABLE `educonnect_course_payment` (
  `id` bigint(20) NOT NULL,
  `sid` varchar(150) NOT NULL,
  `course` varchar(150) NOT NULL,
  `c_id` varchar(150) NOT NULL,
  `amount` varchar(150) NOT NULL,
  `payment_id` varchar(150) NOT NULL,
  `paid` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `educonnect_course_payment`
--

INSERT INTO `educonnect_course_payment` (`id`, `sid`, `course`, `c_id`, `amount`, `payment_id`, `paid`) VALUES
(1, '1', 'Introduction to Computer Science', '1', '7000.0', 'order_NnUMbZ6GPnocgG', 1),
(2, '2', 'Web Development Fundamentals', '2', '6000.0', 'order_NnUORNHOIa6ceF', 1);

-- --------------------------------------------------------

--
-- Table structure for table `educonnect_facultyreg`
--

CREATE TABLE `educonnect_facultyreg` (
  `id` bigint(20) NOT NULL,
  `name` varchar(150) NOT NULL,
  `course` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `address` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `educonnect_facultyreg`
--

INSERT INTO `educonnect_facultyreg` (`id`, `name`, `course`, `email`, `phone`, `address`, `password`) VALUES
(1, 'Anusha', 'Basic Programming Concepts', 'anu@gmail.com', '8590432096', '789 Paper St.  TX 75001', 'Anusha@123'),
(2, 'Aravind sharma', 'Select', 'aravind@gmail.com', '8590432096', 'Mookola HOUSE vennmenad ', 'Aravind@123');

-- --------------------------------------------------------

--
-- Table structure for table `educonnect_leave_applications`
--

CREATE TABLE `educonnect_leave_applications` (
  `id` bigint(20) NOT NULL,
  `sid` varchar(150) NOT NULL,
  `fid` varchar(150) NOT NULL,
  `date` varchar(150) NOT NULL,
  `reason` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `educonnect_studentreg`
--

CREATE TABLE `educonnect_studentreg` (
  `id` bigint(20) NOT NULL,
  `name` varchar(150) NOT NULL,
  `place` varchar(150) NOT NULL,
  `city` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `address` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  `st_type` varchar(150) NOT NULL,
  `disability_certificate` varchar(100) DEFAULT NULL,
  `disability_status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `educonnect_studentreg`
--

INSERT INTO `educonnect_studentreg` (`id`, `name`, `place`, `city`, `email`, `phone`, `address`, `password`, `status`, `st_type`, `disability_certificate`, `disability_status`) VALUES
(1, 'Akhil S', 'Thalassery', 'Kannur', 'akhil@gmail.com', '8958392028', 'Peter Gibbons 789 Paper St. Office 10 Techville', 'Akhil@123', 'approved', 'Deaf', 'certificates/Screenshot_2024-02-19_210437_F6pK7e5.png', 'yes'),
(2, 'Riya G P', 'Guruvayoor', 'Thrissur', 'riya@gmail.com', '8078152909', 'Mookola HOUSE', 'Riya@123', 'approved', 'Deaf', '', 'no'),
(3, 'Athira anil', 'Pasukadavu', 'Kozhikode', 'athira@gmail.com', '7867950040', '789 Paper St.  TX 75001', 'Athira@123', 'approved', 'Deaf', 'certificates/Screenshot_2024-02-19_210648_TUqXkB9.png', 'yes'),
(4, '11234567', '234ggu8890', '2334tggjjui', 'awerrgklp@gmail.com', '23445778822', '1234tgnkkkkk', '23456789hb', 'pending', '', '', 'no'),
(5, 'a34556677', '1345667715ffgg', '124567889q', '24355@rfhujjgmail.com', '8590432096', 'SOFTWARE DEVELOPER,Mookoloahouse Venmenad p.o', 'Asd3311356', 'pending', '', '', 'no'),
(6, 'ardra', '23456789', 'aeedra', '2345yu88@gmail.com', '78675678900', '789 Paper St. Office 10 Techville, TX 75001', 'asdfghjk23456', 'pending', '', '', 'no'),
(7, 'Devika', 'asdfghjk', 'agdhjkhklkhl', 'det457ppd@gmail.com', '423690456677', '789 Paper St.  TX 75001', '13445as@', 'pending', '', '', 'no'),
(8, 'Ardra M P', 'vytila', 'Kannur', '23457y@gmailfjju4uu.com', '07867950040', '789 Paper St. Office 10 Techville, TX 75001', 'sw21124f', 'pending', '', '', 'no'),
(9, 'ardra', 'rrrp[er\'', 'Thrissur122', 'ardramp0220@gmail.com', '8590432096', 'SOFTWARE DEVELOPER,Mookoloahouse Venmenad p.o', 'dkgl;h', 'pending', '', '', 'no');

-- --------------------------------------------------------

--
-- Table structure for table `educonnect_study_materials`
--

CREATE TABLE `educonnect_study_materials` (
  `id` bigint(20) NOT NULL,
  `name` varchar(150) NOT NULL,
  `details` varchar(150) NOT NULL,
  `file` varchar(150) NOT NULL,
  `c_id` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `educonnect_study_materials`
--

INSERT INTO `educonnect_study_materials` (`id`, `name`, `details`, `file`, `c_id`) VALUES
(1, 'Introduction to Computer Science', 'notes', 'Introduction to Datascience  notes_PbWwxto.pdf', '1'),
(2, 'Web Development Fundamentals', 'notes', 'Computer Security Fundamentals notes_A6lkdEs.pdf', '2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `educonnect_assigned_studentreg`
--
ALTER TABLE `educonnect_assigned_studentreg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `educonnect_chats`
--
ALTER TABLE `educonnect_chats`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `educonnect_class_schedules`
--
ALTER TABLE `educonnect_class_schedules`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `educonnect_course_assign`
--
ALTER TABLE `educonnect_course_assign`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `educonnect_course_details`
--
ALTER TABLE `educonnect_course_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `educonnect_course_payment`
--
ALTER TABLE `educonnect_course_payment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `educonnect_facultyreg`
--
ALTER TABLE `educonnect_facultyreg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `educonnect_leave_applications`
--
ALTER TABLE `educonnect_leave_applications`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `educonnect_studentreg`
--
ALTER TABLE `educonnect_studentreg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `educonnect_study_materials`
--
ALTER TABLE `educonnect_study_materials`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `educonnect_assigned_studentreg`
--
ALTER TABLE `educonnect_assigned_studentreg`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `educonnect_chats`
--
ALTER TABLE `educonnect_chats`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `educonnect_class_schedules`
--
ALTER TABLE `educonnect_class_schedules`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `educonnect_course_assign`
--
ALTER TABLE `educonnect_course_assign`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `educonnect_course_details`
--
ALTER TABLE `educonnect_course_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `educonnect_course_payment`
--
ALTER TABLE `educonnect_course_payment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `educonnect_facultyreg`
--
ALTER TABLE `educonnect_facultyreg`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `educonnect_leave_applications`
--
ALTER TABLE `educonnect_leave_applications`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `educonnect_studentreg`
--
ALTER TABLE `educonnect_studentreg`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `educonnect_study_materials`
--
ALTER TABLE `educonnect_study_materials`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
