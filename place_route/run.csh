#! /bin/csh

./PnR_image ./testcase_latest2 sc.lef sc_block.v sc.map drcRules_calibre_asap7_Rule_Deck.rul switched_capacitor_filter | tee log
