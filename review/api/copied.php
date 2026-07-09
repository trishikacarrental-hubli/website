<?php
/* Mark a review as 'used' when the visitor copies it. Used reviews are never served again. */
require __DIR__.'/db.php';

if(!empty($_POST['id']) && ctype_digit((string)$_POST['id'])){
  try{
    db()->prepare("UPDATE reviews SET status='used', used_at=NOW()
                   WHERE id=? AND status<>'used'")->execute([$_POST['id']]);
  }catch(Throwable $e){ /* ignore */ }
}
json(['ok'=>true]);
