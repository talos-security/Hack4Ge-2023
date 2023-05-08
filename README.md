# Hack4Ge 1° Edizione

## Requisiti

La maggior parte degli applicativi vulnerabili sarà scritta in Python

- Python3.x 
- Docker

## Consigli Generali
Nella cartella sqli vi sono tutti gli applicativi vulnerabili al sql-injection.

Nella cartalla ssti vi sono quelli vulnerabili al server-side-template-injection.

## Obiettivo dell'Hackathon

L'obiettivo dell'Hackathon è quello di sviluppare uno strumento automatico in grado di identificare il maggior numero di vulnerabilità (TP) nel minor tempo possibile.
Fate attenzione ai FP (cioè vulnerabilità che non possono essere sfruttate) e FN (cioè vulnerabilità non riscontrate dal vostro strumento).


### Setup
Ogni progetto dovrà essere inviato con un README.md contente le istruzioni per il setup e per l'esecuzione del programma in modo dettagliato.
A seconda del linugaggio utilizzato dovranno essere fornite le versioni delle librerie utilizzate in modo tale da replicare esattamente il comportamento del progetto.

### Input

Il programma dovrà prendere in input la cartella del progetto da analizzare.


### Output
Il programma dovrà stampare a console i file dove è presente la vulnerabilità, il tipo di vulnerabilità e la riga. Un esempio è il seguente:

```
/home/project/test.py, SQLI, 34
/home/project/test-ssti.py, SSTI, 80
```

## Credits

## Risorse
- https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection
- https://portswigger.net/web-security/sql-injection