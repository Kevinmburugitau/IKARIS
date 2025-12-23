<?php
echo "php";
$test = "John,Richard,Doe,Roe";
$s = ",";
$r = explode($s,$test);
print_r /*strtoupper*/($r);
echo trim(" Im $r[1] $r[3] this is my brother $r[0] $r[2] ");
$w_1 = str_replace("Richard","Raechel",$r); 
$w_2 = str_replace("John","Jane",$r);
echo ("\nThis is my wife $w_1[1] $w_1[3] and John's wife $w_2[0] $w_2[2]");
$rich = substr($r[1],0,4);
echo ("\nI'm $rich like my name");
?>
