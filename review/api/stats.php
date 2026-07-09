<?php
/* Quick pool health check. Visit /review/api/stats.php?key=YOUR_KEY
   Shows how many reviews are available / served / used so you know when to top up. */
require __DIR__.'/db.php';

$KEY = 'trishika-stats-7c1b';           // <-- change this
if(($_GET['key'] ?? '') !== $KEY){ http_response_code(403); exit('forbidden'); }

try{
  $rows = db()->query("SELECT status, stars, COUNT(*) c FROM reviews GROUP BY status, stars")->fetchAll();
  $total = db()->query("SELECT COUNT(*) FROM reviews")->fetchColumn();
  $avail = db()->query("SELECT COUNT(*) FROM reviews WHERE status='available'")->fetchColumn();
  json(['total'=>(int)$total, 'available'=>(int)$avail, 'breakdown'=>$rows]);
}catch(Throwable $e){ json(['error'=>$e->getMessage()]); }
