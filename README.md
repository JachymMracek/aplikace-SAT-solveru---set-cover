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

 #### "k", type=int
 Maximální počet podmnožin, které splňují zadání. Program hledá řešení k = 1,...k. Pokud uživatel nastaví find_best na "yes", pak tento parametr nemá smysl.
  
 #### "header", type=str
 Napsáním "yes" uživatel uvidí CNF formule, pokud napíše "no", pak se CNF formule nezobrazí na standartní výstup.

### Ukázkový vstup
python SAT_set_cover.py 10 "1;2;3;4;5;6;7;8;9;10;" yes 5 no


## Postup řešení
CNF formuli jsme vytvořili ze 2 částí.

### První část
Počet pokrívajících podmnožin může být maximálně k aneb počet pokrývajících podmnožin nesmí být k+1. Řešíme výrokem:

$$
\bigwedge_{\substack{I \subseteq \{1, \dots, n\} \\ |I| = k+1}} \left( \bigvee_{i \in I} \neg S_i \right)
$$

### Druhá část
Každý prvek z U musí náležet alespoň jedné podmnožině  z množiny řešící naší úlohu. Řešíme výrokem:

$$
\bigvee_{u \subseteq U, u \in S_i, S_i \subseteq S} S_i
$$

### CNF formule
Konjunkcí našich výroků dostáváme finální výrok:

$$
\left( \bigwedge_{\substack{I \subseteq \{1, \dots, n\} \\ |I| = k+1}} \left( \bigvee_{i \in I} \neg S_i \right) \right) \wedge \left( \bigwedge_{u \in U} \left( \bigvee_{\substack{ \\ u \in S_i,S_i \subseteq S}} S_i \right) \right)
$$


## Output

Outputem je buď chybová hláška WRONG INPUT, což znamená, že byly zadány chybné vstupní parametry. A nebo vypsané jednotlivé podmožiny, které pokrývají universe množinu + Zobrazená množina U + k pro které platí řešení. Ukázkovým výstupem
je:




                                          
