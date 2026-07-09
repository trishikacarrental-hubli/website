<?php
/* Mark a review as 'used' (dead) when the visitor copies it. Used reviews are never
   served again. Atomic: only one caller can flip a given review available/served -> used. */
require __DIR__.'/db.php';

$ok = false;
if(!empty($_POST['id']) && ctype_digit((string)$_POST['id'])){
  try{
    $st = db()->prepare("UPDATE reviews SET status='used', used_at=NOW()
                         WHERE id=? AND status<>'used'");
    $st->execute([$_POST['id']]);
    $ok = $st->rowCount() > 0;   // true if WE were the one who burned it
  }catch(Throwable $e){ /* ignore */ }
}
json(['ok'=>$ok]);
