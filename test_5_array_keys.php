<?php

$array = $_REQUEST['array'];

$keys = [];

foreach ($array as $k => $value) {
    $keys[] = $k;
}

for ($i = 1; $i <= 5; $i++) {
    echo $keys[$i];
}