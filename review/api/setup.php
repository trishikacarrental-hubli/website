<?php
/* One-time setup: creates the table and loads reviews from seed_reviews.txt.
   Visit /review/api/setup.php?key=YOUR_KEY once, then DELETE this file.
   Safe to re-run after adding new lines to seed_reviews.txt (duplicates are skipped). */
require __DIR__.'/db.php';

$KEY = 'su-7Fq2Kd9mXtZr4';            // <-- change this before uploading
if(($_GET['key'] ?? '') !== $KEY){ http_response_code(403); exit('forbidden'); }
header('Content-Type: text/plain');

$pdo = db();
$pdo->exec("CREATE TABLE IF NOT EXISTS reviews(
  id INT AUTO_INCREMENT PRIMARY KEY,
  stars TINYINT NOT NULL DEFAULT 5,
  body TEXT NOT NULL,
  hash CHAR(40) NOT NULL,
  status ENUM('available','served','used') NOT NULL DEFAULT 'available',
  served_at DATETIME NULL,
  used_at DATETIME NULL,
  UNIQUE KEY uq_hash (hash),
  KEY idx_status_stars (status, stars)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4");

$file = __DIR__.'/seed_reviews.txt';
if(!is_readable($file)){ exit("seed_reviews.txt not found next to setup.php\n"); }

$lines = file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
$ins = $pdo->prepare("INSERT IGNORE INTO reviews (stars, body, hash) VALUES (?,?,?)");
$added = 0; $seen = 0;

foreach($lines as $ln){
  $ln = trim($ln);
  if($ln === '' || $ln[0] === '#') continue;      // skip blanks / comments
  $p = explode('|', $ln, 2);
  if(count($p) < 2) continue;
  $stars = ((int)$p[0] === 4) ? 4 : 5;
  $body  = trim($p[1]);
  if($body === '') continue;
  $seen++;
  $hash = sha1(mb_strtolower($body));
  $ins->execute([$stars, $body, $hash]);
  $added += $ins->rowCount();
}

$avail = $pdo->query("SELECT COUNT(*) FROM reviews WHERE status='available'")->fetchColumn();
$total = $pdo->query("SELECT COUNT(*) FROM reviews")->fetchColumn();

echo "Setup complete.\n";
echo "Lines read: $seen\n";
echo "New reviews added: $added\n";
echo "Total in DB: $total  |  Available now: $avail\n\n";
echo ">>> IMPORTANT: delete setup.php from the server now. <<<\n";
