<?php
/* Serve ONE unused review and mark it 'served' so no two people get the same one.
   ?stars=5 (default) or 4.  Optional ?release=<id> puts a shuffled-away review back. */
require __DIR__.'/db.php';

$FALLBACK = 'Good and reliable cab service in hubli. on time pickup, clean car and fair price. recommended';

try{
  $pdo = db();

  // recycle reviews that were shown but never copied (abandoned) after 30 min
  $pdo->exec("UPDATE reviews SET status='available', served_at=NULL
              WHERE status='served' AND served_at < (NOW() - INTERVAL 30 MINUTE)");

  // if the user tapped "suggest another", release the one they skipped
  if(!empty($_GET['release']) && ctype_digit((string)$_GET['release'])){
    $st = $pdo->prepare("UPDATE reviews SET status='available', served_at=NULL
                         WHERE id=? AND status='served'");
    $st->execute([$_GET['release']]);
  }

  $stars = (isset($_GET['stars']) && $_GET['stars']=='4') ? 4 : 5;

  $pdo->beginTransaction();
  // lock one available row for this rating; fall back to any rating if that pool is empty
  $row = $pdo->query("SELECT id,body FROM reviews WHERE status='available' AND stars=$stars
                      ORDER BY RAND() LIMIT 1 FOR UPDATE")->fetch();
  if(!$row){
    $row = $pdo->query("SELECT id,body FROM reviews WHERE status='available'
                        ORDER BY RAND() LIMIT 1 FOR UPDATE")->fetch();
  }
  if($row){
    $pdo->prepare("UPDATE reviews SET status='served', served_at=NOW() WHERE id=?")
        ->execute([$row['id']]);
    $pdo->commit();
    json(['id'=>(int)$row['id'], 'body'=>$row['body']]);
  }
  $pdo->commit();
  // pool exhausted
  json(['id'=>0, 'body'=>$FALLBACK, 'empty'=>true]);

}catch(Throwable $e){
  json(['id'=>0, 'body'=>$FALLBACK]);
}
