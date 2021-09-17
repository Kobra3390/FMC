# Introduzione a FMC (IT)
**FMC** acronimo di *Fast Mac Changer* è uno script scritto in Python che permette di effettuare il **Mac Spoofing**, per effettuate questa operazione il tool usa Macchanger mediante dei sottoprocessi gestiti dal modulo subprocess di python, lo script è scritto nella versione *3.9.5* del linguaggio. Il progetto nasce dall’esigenza di fornire un programma da riga di comando semplice per chi non è pratico di macchanger e anche per l’installazione di quest’ultimo sui sistemi operativi GNU/Linux che sono sprovvisti di questo tool (come Pop OS). Lo script é disponibile solo per Linux e distrubuzioni correlate

---

# Introduction to FMC (EN)
**FMC** (Fast Mac Changer) is a scrpit, written in python, that is used for **Mac Spoofing**; to do this, the tool uses Macchanger through some subprocesses, managed by python's subprocess module. The script is written in python ver. 3.9.5. The script is only available for Linux and related distributions

---
# COS’E’ IL MAC ADDRESS E IL MAC SPOOFING (IT)
Prima di usare il tool è meglio spendere due righe sulla parte teorica legata al mac address e il mac spoofing (anche se sei giunto fin qui dovresti già saperlo :P). 
Il Mac Address (acronimo di Media Access Control) è un codice alfa numerico che i produttori di schede di rete inseriscono nelle memorie EEPROM dei propri dispositivi, tale codice è univoco alla scheda, ciò la rende il dispositivo unico al mondo. Il Mac Address è quindi il codice fiscale dei computer. Il Mac Spoofing è un’operazione che permette di camuffare tale indirizzo, per svariate operazioni: 
+ Fingere di essere un altro computer e quindi prendere la sua identità
+ Proteggere la propria privacy durante operazioni illecite o durante una comune navigazione, il mac address viene utilizzato in fase di autenticazione nelle reti e anche nelle comunicazioni nelle reti LAN (mediante il protocollo ARP). 

Essendo un codice univoco che non può essere modificato, il Mac Spoofing effettua una modifica software, infatti riavviando il proprio device il MAC tornerà quello di partenza.

---

# WHAT IS A MAC ADDRESS AND WHAT'S MAC SPOOFING (EN)

Before using the tool it's better to read a little about mac addresses and mac spoofing (even if you should know about this stuff if you're here :P)
The Mac Address (Mac as in Media Access Control) is an alpha-numeric code that network card producers insert in the EEPROM memories of their devices; this code is exclusive to it's network card, this makes every device unique in it's address. You could say that the Mac Address is like a fiscal code for computers.
"Mac Spoofing" is an operation that lets us camouflage the Mac Address, for various uses:

+ Pretending to be another computer, basically taking it's identity
+ Protecting one's privacy during illicit operations or just a common navigation of the internet (since the mac address is used in the autentication fase in networks and in communications in LAN networks).

Since the address is unique and can't be modified, Mac Spoofing modifies the software, so restarting your device will undo the process and return your address to the old one.

---

# INSTALLAZIONE (IT)

Linux:

```
$ git clone https://github.com/Kobra3390/FMC.git
$ cd FMC
$ python3 FMC.py
```

---
# INSTALLATION (EN)

```
$ git clone https://github.com/Kobra3390/FMC.git
$ cd FMC
$ python3 FMC.py
```

---

# CARATTERISTICHE(IT)
 
1. **Install Macchanger**	:	Tale opzione permette di installare sulla macchina Macchanger qual ora non fosse già pre-installato
1. **Change The Mac Address Manually**	:	Questa opzione permette all’utente di inserire un mac address manualmente in input
1. **Use An Mac Address Vendor**		:	Questa opzione permette di utilizzare un mac address vendor che fornisce Macchanger
1. **Show The Current Mac Address**	:	Questa opzione permette di visionare il mac address corrente
1. **Back To The Original Mac Address**	:	questa opzione permette di tornare all’mac address di origine della macchina
1. **Set Full Random Mac Address**	:	questa opzione permette di generare un mac address random e funzionale 

---

# CHARACTERISTICS(EN)

1. **Install Macchanger**: To install Macchanger on the device if it's not pre-installed already
1. **Change The Mac Address Manually**:	To manually insert a Mac Address in input
1. **Use An Mac Address Vendor**: To use a mac address vendor, supplied by Macchanger
1. **Show The Current Mac Address**	: to view the current Mac Address
1. **Back To The Original Mac Address**:	To return to the orginal Mac Address
1. **Set Full Random Mac Address**:	to generate a random and functional Mac Address











