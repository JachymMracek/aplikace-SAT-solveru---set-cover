# aplikace-SAT-solveru SET COVER

## Použité technologie
 Aplikace SAT solveru je naprogramována v jazyce Python s použitím SAT solveru Glucosce 4.2, kde jsou využity knihovny os, subprocess, itertools a argparse. Programu je určený pro operační systém Linux.

 ### Použité knihovny
 #### import os
 Pro nalezení glucose-syrup souboru.
 
 #### import subprocess
 Knihovna, která zprostředkuje spuštění SAT solveru v Pythonu.
 
 #### from itertools import combinations
 Pro vygenerování všech klauzulí, které řeší 1 část CNF formule. (Popis níže)
 
 #### import argparse
 Knihovna pro umožnění uživatelovi zadat vstupní parametry.
 
 ## Popis zadání
 Aplikace dostane množina U, která obsahuje čísla 1 až n a vstupní množinu S, která obsahuje číselné podmnožiny. Úkolem aplikace je najít podmnožiny z S, takové aby pokrily všechny prvky v množině U aneb každý číselný prvek v U
 je alespoň v jedné podmnožině z podmnožin splňující zadání.

 ## Popis vstupních parametrů
 #### "n", type=int
 číslo, které udává počet prvků v množině U, která obsahuje prvky 1 až n.
 
 #### "all_numbers_of_collection_set", type=str
 String reprezentující množinu obsahující číselné podmnožiny, kde prvky v podmnožině mohou obshaovat pouze čísla, které musejí být oddělené čárkou (","), a jednotlivé podmnožiny musejí být ukončené středníkem (";"), tedy i poslední.
 
 #### "find_best", type=str
 Uživatel si může zvolit zda chce najít nejlepší k nebo program spustit pro zadané k, pokud uživatel napíše "yes", pak aplikace hledá nejlepší k a nebere zřetel na zvolené k. Pokud uživatel nechce hledat nejlepší k, pak napište "no".

 #### k", type=int
 Maximální počet podmnožin, které splňují zadání. Program hledá řešení k = 1,...k. Pokud uživatel nastaví find_best na "yes", pak tento parametr nemá smysl.
  
 ####"header", type=str
 Napsáním "yes" uživatel uvidí CNF formule, pokud napíše "no", pak se CNF formule nezobrazí na standartní výstup.

### ukázkový vstup (za default):
  parser.add_argument("n", type=int, nargs="?", default=5, help="Write count n of elements in universe")
  parser.add_argument("all_numbers_of_collection_set", type=str, nargs="*", default="1,2,3;2,4;3,4;4,5;",help="Write lined up all numbers in collection where each set ends with ;")
  parser.add_argument("find_best", type=str, nargs="?", default="no", help="Do you want find best k? (write:yes) or (write:no)")
  parser.add_argument("k", type=int, nargs="?", default="2", help="Write count of sets which should cover universe.")
  parser.add_argument("header", type=str, nargs="?", default="no", help="Do you want CNF formula and statistics during SAT solving?(yes/no)")

## Postup řešení pomocí výrokové logiky

CNF formuli jsme vytvořili ze 2 částí.

### první část

Popisuje, že chceme aby byly vybrány právě k podmnožin z S, tak že vygenerujeme všechny klauzule ve tvaru ((not(s_1) or not(s_2) ... or not(s_k+1)), kde tyto klauzule jsou musí být všechny splněny, tedy musí platit claus_1 and claus_2 ...
Tímto výrokem zařídíme, že SAT bude brát maximálně k podmnožin.

### druhá část

Druhá část řeší, aby sjednocení množin obsahovalo, všechny prvky v U, tedy každému prvku vytvoříme klauzuli, která obshauje s_i, takové které obshauje daný prvek, čímž vznikne výrok pro každý prvek ve tvaru s_i or s_j or ......
Tyto všechny klazule musí platit a proto využíjeme konjunkci pro tyto klauzule

### CNF

Naše finalní klauzule je první část and druhá část.

## Output

Outputem je buď chybová hláška WRONG INPUT, což znamená, že byly zadány chybné vstupní parametry. A nebo vypsané jednotlivé podmožiny, které pokrývají universe množinu + Zobrazená množina U + k pro které platí řešení. Ukázkovým výstupem
je:




                                          
