# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 11:53:40 2020

@author: mastro
"""
import sys
import nltk

def LunghezzaCorpus(frasi):
    tokensTot=[] #array che contiene tutti i token
    frasiTot = 0
    for frase in frasi:
        frasiTot = frasiTot + 1 #per ogni frase aggiunge 1 a frasiTot
        tokens = nltk.word_tokenize(frase) #tokenizza le frasi nel testo
        tokensTot += tokens #aggiunge alla lista i tokens
    numeroTokens=len(tokensTot) #mi restituisce il numero totale di tokens = corpus
    
    
    return tokensTot, frasiTot, numeroTokens

def LunghezzaMedia(frasi):
    tokensTot=[]
    frasiTot = 0 
    for frase in frasi:
        frasiTot = frasiTot + 1
        tokens = nltk.word_tokenize(frase)
        tokensTot += tokens 
        Lunghezze_TOT = 0 #totale di tutte le lunghezze dei tokens
        for token in tokensTot:
            Lunghezze_TOT = Lunghezze_TOT + len(token) 
        media_parola = Lunghezze_TOT / len(tokensTot) #media calcolata: totale delle lunghezze dei tokens/numero totale tokens
        media_frase = len(tokensTot) / frasiTot #media calcolata: totale dei tokens/ totale delle frasi
   
    return media_parola, media_frase  

def Vocabolario_TTR(frasi):
    tokensTot=[]
    for frase in frasi:
        tokens = nltk.word_tokenize(frase) #tokenizza le frasi nel testo
        tokensTot += tokens #aggiunge alla lista i tokens
    tokens5000 = [] #array dei primi 5000 tokens nel corpus
    for i in range(5000): 
        tokens5000.append(tokensTot[i]) #aggiungo all'array i primi 5000 tokens
   
    
    types5000 = len(set(tokens5000)) #restituisce numero totale di types (vocabolario) nei primi 5000 tokens
    TTR = types5000/len(tokens5000) #Type/Token ratio 
    
    return types5000, TTR


def CrescitaLessicale (tokensTot):
    #definisco le classi di frequenza
    V1 = 1
    V5 = 5
    V10 = 10
    
    
    for i in range (0, len(tokensTot), 500): #ciclo la lista di tokens di 500 in 500
        listaTokensCum = tokensTot[0:i + 500] #creo la lista dei tokens da 0 a i+500
        vocabolarioCum = list(set(listaTokensCum)) #calcolo il vocabolario di listaTokensCum
        
        voc1 = [] #lista contenente i types con frequenza 1 (hapax)
        voc5 = [] #lista contenente i types con frequenza 5
        voc10 = [] #lista contenente i types con frequenza 10
        for tok in vocabolarioCum:
            frequenza = listaTokensCum.count(tok) #per ogni token nel vocabolario calcolo la frequenza
            if frequenza == V1: 
                voc1.append(tok)
            elif frequenza == V5:
                voc5.append(tok)
            elif frequenza == V10:
                voc10.append(tok)
                
        
        #stampo le dimensioni delle classi di frequenza al crescere del corpus
        print('0 -', len(listaTokensCum))
        print('Dimensione della classe di frequenza', V1,':',len(voc1))
        print('Dimensione della classe di frequenza', V5,':',len(voc5))
        print('Dimensione della classe di frequenza', V10,':',len(voc10))
        print()



def MediaNomiVerbi(frasi):
    tokensTOT = []
    Nomi = 0 #contatore nomi
    Verbi = 0 #contatore verbi
    frasiTot = 0 #contatore frasi
    for frase in frasi:
        frasiTot = frasiTot + 1
        tokens = nltk.word_tokenize(frase)
        tokensTOT+=tokens
    tokensPOS = nltk.pos_tag(tokensTOT) #assegna a ogni tokens in ogni frase il suo Part-of-Speech tag, creando dei bigrammi (token - POS)
    for bigramma in tokensPOS:
        if (bigramma[1] == 'NN') or (bigramma[1] == 'NNS') or (bigramma[1] == 'NNP') or (bigramma[1] == 'NNPS'): #per ogni bigramma osservo se il secondo elemento del bigramma è un tag valido per la  categoria nome
            Nomi += 1 #aggiungo il nome al contatore Nomi
        elif (bigramma[1] == 'VB') or (bigramma[1] == 'VBD') or (bigramma[1] == 'VBG') or (bigramma[1] == 'VBN') or (bigramma[1] == 'VBP') or (bigramma[1] == 'VBZ') or (bigramma[1] == 'MD'): #per ogni bigramma osservo se il secondo elemento del bigramma è un tag valido per la categoria verbo 
            Verbi += 1 #aggiungo il verbo al contatore Verbi
       
    media_nomi_frase = Nomi/frasiTot #calcolo la media dei nomi per frase dividendo i nomi totali nel corpus per le frasi totali nel corpus
    media_verbi_frase = Verbi/frasiTot #calcolo la media dei verbi per frase dividendo i verbi totali nel corpus per le frasi totali nel corpus
                 
    return Nomi, Verbi, media_nomi_frase, media_verbi_frase





def DensitàLessicale(frasi, corpus, Nomi, Verbi): #uso come parametri Nomi e Verbi dalla funzione MediaNomiVerbi
    tokensTOT = [] #array che contiene tutti i bigrammi token-POS
    for frase in frasi:
        tokens = nltk.word_tokenize(frase)
        tokensTOT+=tokens
    
    tokensPOS = nltk.pos_tag(tokensTOT)    
    Punteggiatura = 0
    Aggettivi = 0
    Avverbi = 0
    for bigramma in tokensPOS: #calcolo il totale degli aggettivi, degli avverbi e della punteggiatura nel corpus osservando le etichette del bigramma token-POS
        if (bigramma[1] == '.') or (bigramma[1] ==','):
           Punteggiatura += 1
        elif (bigramma[1] == 'JJ') or (bigramma[1] == 'JJR') or (bigramma[1] == 'JJS'):
            Aggettivi += 1
        elif (bigramma[1] == 'RB') or (bigramma[1] == 'RBR') or (bigramma[1] == 'RBS') or (bigramma[1] == 'WRB'):
            Avverbi += 1
            
    densità = (Nomi + Verbi + Aggettivi + Avverbi) / (corpus - Punteggiatura) #densità calcolata come la somma di Nomi, Verbi, Aggettivi e Avverbi/ il totale dei tokens - la punteggiatura 
    
    return densità
      


def main(file1, file2):
    fileInput1 = open(file1, mode = 'r', encoding = 'utf-8')
    fileInput2 = open(file2, mode = 'r', encoding = 'utf-8')
    raw1 = fileInput1.read()
    raw2 = fileInput2.read()
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    frasi1 = sent_tokenizer.tokenize(raw1) #divide il testo in frasi
    frasi2 = sent_tokenizer.tokenize(raw2)
    tokensTot1, frasiTot1, corpus1= LunghezzaCorpus(frasi1)
    tokensTot2, frasiTot2, corpus2= LunghezzaCorpus(frasi2)
    media_parola1, media_frase1 = LunghezzaMedia(frasi1)
    media_parola2, media_frase2 = LunghezzaMedia(frasi2)
    types1, TTR1 = Vocabolario_TTR(frasi1)
    types2, TTR2 = Vocabolario_TTR(frasi2)
    Nomi1, Verbi1, media_nomi1, media_verbi1 = MediaNomiVerbi(frasi1)
    Nomi2, Verbi2, media_nomi2, media_verbi2 = MediaNomiVerbi(frasi2)
    densità1 = DensitàLessicale(frasi1, corpus1, Nomi1, Verbi1)
    densità2 = DensitàLessicale(frasi2, corpus2, Nomi2, Verbi2)
    print('Il file', file1, 'contiene', frasiTot1, 'frasi e ha un corpus lungo', corpus1, 
          'tokens.')
    print('La lunghezza media delle parole in caratteri è:', media_parola1) 
    print('La lunghezza media delle frasi in token è:', media_frase1)
    print('La grandezza del vocabolario nei primi 5000 tokens è di:', types1, 
          '\nLa TTR nei primi 5000 tokens è:', TTR1)
    print()
    print('La crescita delle classi di frequenza V1, V5, V10 nel testo è:')
    CrescitaLessicale(tokensTot1)
    print('In media per ciascuna frase ci sono',media_nomi1,'nomi.')
    print('In media per ciascuna frase ci sono',media_verbi1,'verbi.')
    print('La densità lessicale del testo è:', densità1)
    print()
    print()
    print('----------------------------------------------------')
    print()
    print()
    print('Il file', file2, 'contiene', frasiTot2, 'frasi e ha un corpus lungo', corpus2, 
          'tokens.')
    print('La lunghezza media delle parole in caratteri è:', media_parola2)
    print('La lunghezza media delle frasi in token è:', media_frase2)
    print('La grandezza del vocabolario nei primi 5000 tokens è di:', types2, 
          '\nLa TTR nei primi 5000 tokens è:', TTR2)
    print()
    print('La crescita delle classi di frequenza V1, V5, V10 nel testo è:')
    CrescitaLessicale(tokensTot2)
    print('In media per ciascuna frase ci sono',media_nomi2,'nomi.')
    print('In media per ciascuna frase ci sono',media_verbi2,'verbi.')
    print('La densità lessicale del testo è:', densità2)
    print()
    print()
    
    
    
    

main (sys.argv[1], sys.argv[2])