<?php

function func1($a) {
    eval($a);
}

function func2($a) {
    func1($a);
}

function func3($a) {
    func2($a);
}

func3($_GET["a"]);
