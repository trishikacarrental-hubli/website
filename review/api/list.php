<?php
/* Serve a BATCH of unused reviews for the chosen rating and lock them ('served')
   so no two visitors ever see the same one. Un-copied ones auto-recycle after 30 min.
   /review/api/list.php?stars=(5|4)&n=10  ->  {"items":[{"id":..,"body":".."}, ...]} */
require __DIR__.'/db.php';

$FALLBACK = [
  'good service and on time. driver was polite, car was clean. recommended for hubli',
  'reliable cab service in hubballi. fair price and safe driving. thank you',
  'clean car, courteous driver, reasonable fare. will book again'
];

$stars = (isset($_GET['stars']) && $_GET['stars'] === '4') ? 4 : 5;
$n = isset($_GET['n']) ? (int)$_GET['n'] : 10;
if ($n < 1) $n = 1;
if ($n > 20) $n = 20;

try{
  $pdo = db();

  // recycle reviews that were served but never copied (abandoned) after 30 min
  $pdo->exec("UPDATE reviews SET status='available', served_at=NULL
              WHERE status='served' AND served_at < (NOW() - INTERVAL 30 MINUTE)");

  $pdo->beginTransaction();

  // lock N available rows for this rating
  $st = $pdo->prepare("SELECT id, body FROM reviews
                       WHERE status='available' AND stars=?
                       ORDER BY RAND() LIMIT $n FOR UPDATE");
  $st->execute([$stars]);
  $rows = $st->fetchAll();

  // top up from any rating if that pool is short
  if (count($rows) < $n) {
    $need = $n - count($rows);
    $skip = '';
    if ($rows) {
      $ids = array();
      foreach ($rows as $r) $ids[] = (int)$r['id'];
      $skip = ' AND id NOT IN ('.implode(',', $ids).')';
    }
    $st2 = $pdo->query("SELECT id, body FROM reviews
                        WHERE status='available'$skip
                        ORDER BY RAND() LIMIT $need FOR UPDATE");
    $rows = array_merge($rows, $st2->fetchAll());
  }

  if ($rows) {
    $ids = array();
    foreach ($rows as $r) $ids[] = (int)$r['id'];
    $pdo->exec("UPDATE reviews SET status='served', served_at=NOW()
                WHERE id IN (".implode(',', $ids).")");
  }

  $pdo->commit();

  $items = array();
  foreach ($rows as $r) $items[] = array('id'=>(int)$r['id'], 'body'=>$r['body']);
  json(array('items'=>$items));

}catch(Throwable $e){
  json(array('items'=>array(), 'fallback'=>$FALLBACK));
}
