<?php
/* Copy this file to db.php and fill in your Hostinger MySQL details.
   (hPanel -> Databases -> MySQL Databases -> create DB + user, then note the values.)
   db.php is gitignored so your credentials never get committed. */

$DB_HOST = 'localhost';
$DB_NAME = 'REPLACE_DB_NAME';
$DB_USER = 'REPLACE_DB_USER';
$DB_PASS = 'REPLACE_DB_PASS';

function db(){
  global $DB_HOST,$DB_NAME,$DB_USER,$DB_PASS;
  static $pdo=null;
  if($pdo) return $pdo;
  $pdo = new PDO("mysql:host=$DB_HOST;dbname=$DB_NAME;charset=utf8mb4",$DB_USER,$DB_PASS,[
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
  ]);
  return $pdo;
}

function json($x){ header('Content-Type: application/json'); echo json_encode($x); exit; }
