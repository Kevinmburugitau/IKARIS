<?php
$m0 = true;
$m1 = false;

if ((!$m0 && $m1) || ($m0 && !$m1)){
	echo var_dump($m0)." xor ".var_dump($m1)." true";
}
echo "\n";
#echo var_dump($m0)." xor ".var_dump($m1)." false";
?>
