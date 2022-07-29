# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 18:01:17 2020

@author: mastro
"""

import sys
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
import math


def FrequenzaPOS(frasi):
    tokensTOT = []
    #Tokenizzo ciascuna frase nel testo diviso in frasi (frasi) e ad ogni token attribuisco la sua POS
    for frase in frasi:
        tokens = nltk.word_tokenize(frase)
        tokensTOT += tokens
    tokensPOS = nltk.pos_tag(tokensTOT)
    listaPOS = []
    #Creo una lista (listaPOS) contenente solo i POS tag dei tokens nel corpus estrapolando da ogni bigramma token-POS, il secondo elemento
    for bigramma in tokensPOS:
        listaPOS.append(bigramma[1])

    frequenzePOS = nltk.FreqDist(listaPOS) #calcolo la frequenza dei tag
    frequenzePOS_ordinate= frequenzePOS.most_common(len(listaPOS))  #ordino i tag per frequenza discendente

    for i in range(10): #stampo solo i primi 10 tag più frequenti con relativa frequenza
        print ('POS:',frequenzePOS_ordinate[i][0], 'frequenza:',frequenzePOS_ordinate[i][1])



def FrequenzaNomiVerbi(frasi):
    tokensTOT = []
    #Divido il testo in frasi, tokenizzo ciascuna frase e ad ogni token attribuisco la sua POS
    for frase in frasi:
        tokens = nltk.word_tokenize(frase)
        tokensTOT+=tokens
    tokensPOS = nltk.pos_tag(tokensTOT)
    Nomi = []
    Verbi = []
    for bigramma in tokensPOS:
        #per ogni bigramma osservo se il secondo elemento del bigramma è un tag valido per la  categoria nome o per la categoria verbo
        if (bigramma[1] == 'NN') or (bigramma[1] == 'NNS') or (bigramma[1] == 'NNP') or (bigramma[1] == 'NNPS'):
            Nomi.append(bigramma) #se la condizione è vera aggiungo il bigramma alla lista Nomi
        elif (bigramma[1] == 'VB') or (bigramma[1] == 'VBD') or (bigramma[1] == 'VBG') or (bigramma[1] == 'VBN') or (bigramma[1] == 'VBP') or (bigramma[1] == 'VBZ') or (bigramma[1] == 'MD'):
            Verbi.append(bigramma)  #se la condizione è vera aggiungo il bigramma alla lista Verbi

    #calcolo la frequenza dei nomi e dei verbi e li ordino in ordine discendente
    frequenzaNomi = nltk.FreqDist(Nomi)
    frequenzaNomi_ordinata = frequenzaNomi.most_common(len(Nomi))
    frequenzaVerbi = nltk.FreqDist(Verbi)
    frequenzaVerbi_ordinata = frequenzaVerbi.most_common(len(Verbi))

    print('I venti sostantivi più frequenti sono:')
    for i in range(20): #stampo solo i primi 20 nomi più frequenti con relativa frequenza
        print ('Sostantivo:',frequenzaNomi_ordinata[i][0][0], 'frequenza:',frequenzaNomi_ordinata[i][1])
    print()
    print('I venti verbi più frequenti sono:')
    for i in range(20): #stampo solo i primi 20 nomi più frequenti con relativa frequenza
        print ('Verbo:',frequenzaVerbi_ordinata[i][0][0], 'frequenza:',frequenzaVerbi_ordinata[i][1])



def FrequenzaBigrammi(frasi):
    #Tokenizzo ciascuna frase e ad ogni token attribuisco la sua POS
    tokensTOT = []
    for frase in frasi:
        tokens = nltk.word_tokenize(frase)
        tokensTOT += tokens

    POS = nltk.pos_tag(tokensTOT) #assegna a ogni tokens in ogni frase il suo Part-of-Speech tag, creando dei bigrammi (token - POS)
    bigrammiPOS = list(nltk.bigrams(POS)) #creo lista dei bigrammi nel testo, in cui ogni token è accompagnato dal suo POS tag



    bigrammi_nome_verbo = []
    #per ogni bigrammaPOS, se il primo token è etichettato come nome e il secondo come verbo, aggiungo a bigrammi_nome_verbo il bigramma
    for bigramma in bigrammiPOS:
        if ((bigramma[0][1] == 'NN') or (bigramma[0][1] == 'NNS') or (bigramma[0][1] == 'NNP') or (bigramma[0][1] == 'NNPS')) and ((bigramma[1][1] == 'VB') or (bigramma[1][1] == 'VBD') or (bigramma[1][1] == 'VBG') or (bigramma[1][1] == 'VBN') or (bigramma[1][1] == 'VBP') or (bigramma[1][1] == 'VBZ')):
            bigrammi_nome_verbo.append(bigramma)
    #calcolo la frequenza dei bigrammi nome-verbo e li ordino in ordine discendente
    frequenzaBigrammiNV = nltk.FreqDist(bigrammi_nome_verbo)
    frequenza_ordinataBigrammiNV = frequenzaBigrammiNV.most_common(len(bigrammi_nome_verbo))

    print('I venti bigrammi nome-verbo più frequenti sono:')
    for i in range(20): #stampo solo i primi 20 bigrammi nome-verbo più frequenti con relativa frequenza
        print("Bigramma:", frequenza_ordinataBigrammiNV[i][0][0][0], frequenza_ordinataBigrammiNV[i][0][1][0],'frequenza:',frequenza_ordinataBigrammiNV[i][1])

    bigrammi_adj_nome = []
    #per ogni bigrammaPOS, se il primo token è etichettato come aggettivo e il secondo come nome, aggiungo a bigrammi_adj_nome il bigramma
    for bigramma in bigrammiPOS:
        if ((bigramma[0][1] == 'JJ') or (bigramma[0][1] == 'JJR') or (bigramma[0][1] == 'JJS')) and ((bigramma[1][1] == 'NN') or (bigramma[1][1] == 'NNS') or (bigramma[1][1] == 'NNP') or (bigramma[1][1] == 'NNPS')):
            bigrammi_adj_nome.append(bigramma)
    #calcolo la frequenza dei bigrammi nome-verbo e li ordino in ordine discendente
    frequenzaBigrammiAN = nltk.FreqDist(bigrammi_adj_nome)
    frequenza_ordinataBigrammiAN = frequenzaBigrammiAN.most_common(len(bigrammi_adj_nome))

    print()
    print('I venti bigrammi aggettivo-nome più frequenti sono:')
    for i in range(20): #stampo solo i primi 20 bigrammi aggettivo-verbo più frequenti con relativa frequenza
        print('Bigramma:', frequenza_ordinataBigrammiAN[i][0][0][0], frequenza_ordinataBigrammiAN[i][0][1][0],'Frequenza:',frequenza_ordinataBigrammiAN[i][1])



def EstraiBigrammi3(frasi):
    tokensTOT = []
    #creo la lista dei tokens totali e per ciascun token calcolo la frequenza e li ordino in ordine decrescente
    for frase in frasi:
        tokens = nltk.word_tokenize(frase)
        tokensTOT += tokens
    frequenza_tokens = nltk.FreqDist(tokensTOT)
    frequenza_tokens_ordinata = frequenza_tokens.most_common(len(tokensTOT))

    tokensMaggTre = [] #array contenente solo i token con frequenza maggiore di 3
    #osservo la frequenza di ciascun token: se il token ha frequenza > 3 lo aggiungo a tokensMaggTre
    for bigramma in frequenza_tokens_ordinata:
        if bigramma[1] > 3:
            tokensMaggTre.append(bigramma[0])

    bigrammi = list(nltk.bigrams(tokensTOT)) #creo lista dei bigrammi nel corpus
    #calcolo la frequenza dei bigrammi e li ordino in ordine discendente
    frequenza_bigrammi = nltk.FreqDist(bigrammi)
    frequenza_bigrammi_ordinata = frequenza_bigrammi.most_common(len(bigrammi))

    bigrammi_tokensMaggTre = [] #lista dei bigrammi formati da tokens con frequenza > 3 con relativa frequenza
    #per ogni bigramma del corpus controllo se è formato da tokens che hanno una frequenza > 3. Se la condizione è vera aggiungo il bigramma a bigrammi_tokensMaggTre
    for bigramma in frequenza_bigrammi_ordinata:
        if (bigramma[0][0] in tokensMaggTre) and (bigramma[0][1] in tokensMaggTre):
            bigrammi_tokensMaggTre.append(bigramma)

    return tokensTOT, bigrammi_tokensMaggTre




def BigrammaProbCong_CondMAX(tokensTOT, bigrammi3):
    list_probCong = [] #lista di tuple ognuna contenente il bigramma e la rispettiva probabilità congiunta
    list_probCond = [] #lista di tuple ognuna contenente il bigramma e la rispettiva probabilità condizionata
    #estraggo i bigrammi diversi dai bigrammi con frequenza > 3
    bigrammiDiversi = sorted(set(bigrammi3))
    lunghezzaCorpus=len(tokensTOT)
    for bigramma in bigrammiDiversi:
        freq_bigramma = bigramma[1] #estraggo la frequenza del bigramma
        frequenzaU = tokensTOT.count(bigramma[0][0]) #estraggo la frequenza del primo elemento del bigramma all'interno del corpus
        probCong = (frequenzaU/lunghezzaCorpus)*(freq_bigramma/frequenzaU) #prob congiunta calcolata con regola del prodotto
        #per ogni bigramma creo una tupla contenente il bigramma con la sua relativa probabilità congiunta e lo aggiungo a list_probCong
        tuplaBPCg = (probCong, bigramma[0])
        list_probCong.append(tuplaBPCg)

        probCond = (freq_bigramma/frequenzaU) #calcolo la probabilità condizionata
        #per ogni bigramma creo una tupla contenente il bigramma con la sua relativa probabilità condizionata e lo aggiungo a list_probCond
        tuplaBPCd = (probCond, bigramma[0])
        list_probCond.append(tuplaBPCd)


    #ordino in ordine decrescente le liste di tuple contenenti le diverse probabilità
    bigr_ordinati_probCong = sorted(list_probCong, reverse=True)
    bigr_ordinati_probCond = sorted(list_probCond, reverse=True)

    print('I venti bigrammi con probabilità congiunta maggiore, calcolata con la regola del prodotto, sono:')
    for i in range(20):  #stampo solo i primi 20 bigrammi bigramma-probCong con probabilità congiunta maggiore
        print('Bigramma:', bigr_ordinati_probCong[i][1], 'Probabilità:', bigr_ordinati_probCong[i][0])

    print()
    print('I venti bigrammi con probabilità condizionata maggiore sono:')
    for i in range(20): #stampo solo i primi 20 bigrammi bigramma-probCond con probabilità condizionata maggiore
        print('Bigramma:', bigr_ordinati_probCond[i][1], 'Probabilità:', bigr_ordinati_probCond[i][0])

    return bigrammiDiversi


def LocalMutualInfo (tokensTOT, bigrammiDiversi):
    lunghezzaCorpus=len(tokensTOT)
    LMI_bigrammi = [] #lista di tuple ognuna contenente il bigramma e la rispettiva LMI
    for bigramma in bigrammiDiversi:
        freq_bigramma = bigramma[1] #estraggo la frequenza del bigramma
        frequenzaU = tokensTOT.count(bigramma[0][0]) #estraggo la frequenza del primo token
        frequenzaV = tokensTOT.count(bigramma[0][1]) #estraggo la frequenza del secondo token
        probBigr = freq_bigramma/lunghezzaCorpus #calcolo la probabilità del bigramma
        probU = frequenzaU/lunghezzaCorpus #calcolo la probabilità del primo token
        probV = frequenzaV/lunghezzaCorpus #calcolo la probabilità del secondo token
        LMI = freq_bigramma * (math.log2(probBigr/(probU*probV))) #calcolo la Local Mutual Information

        #per ogni bigramma creo una tupla contenente il bigramma con la sua relativa LMI e lo aggiungo a LMI_bigrammmi
        tuplaB_LMI = (LMI, bigramma[0])
        LMI_bigrammi.append(tuplaB_LMI)

    #ordino in ordine decrescente le liste di tuple contenenti le diverse LMI
    bigr_ordinati_LMI = sorted(LMI_bigrammi, reverse=True)


    print('I venti bigrammi con forza associativa maggiore sono:')
    for i in range(20): #stampo solo i primi 20 bigrammi bigramma-LMI con LMI maggiore
        print('Bigramma:', bigr_ordinati_LMI[i][1], 'LMI:', bigr_ordinati_LMI[i][0])


def EstraiFrasi(frasi): #dal corpus estraggo le frasi di lunghezza 8, 9, 10, 11, 12, 13, 14, 15, calcolata in tokens
    frasi8 = []
    frasi9 = []
    frasi10 = []
    frasi11 = []
    frasi12 = []
    frasi13 = []
    frasi14 = []
    frasi15 = []
    for frase in frasi:
        tokens = nltk.word_tokenize(frase)
        if len(tokens) == 8:
            frasi8.append(frase)
        elif len(tokens) == 9:
            frasi9.append(frase)
        elif len(tokens) == 10:
            frasi10.append(frase)
        elif len(tokens) == 11:
            frasi11.append(frase)
        elif len(tokens) == 12:
            frasi12.append(frase)
        elif len(tokens) == 13:
            frasi13.append(frase)
        elif len(tokens) == 14:
            frasi14.append(frase)
        elif len(tokens) == 15:
            frasi15.append(frase)

    frasi8_15 = [frasi8, frasi9, frasi10, frasi11, frasi12, frasi13, frasi14, frasi15] #lista contenente le liste con le frasi di diversa lunghezza

    return frasi8_15

def MarkovUno(tokensTOT, frasi8_15):
    lunghezzaCorpus = len(tokensTOT)
    lunghezzaVocabolario = len(set(tokensTOT))
    freq_tokens = nltk.FreqDist(tokensTOT)
    bigrammiTOT=list(nltk.bigrams(tokensTOT))
    freq_bigrammi = nltk.FreqDist(bigrammiTOT)
    Prob_Markov = [] #lista di tuple contenenti la frase con la rispettiva probabilità markoviana
    for lista in frasi8_15:
        for frase in lista:
            tokensFrase = nltk.word_tokenize(frase)
            prob1 = (freq_tokens[tokensFrase[0]]*1.0 + 1)/(lunghezzaCorpus*1.0 + lunghezzaVocabolario) #calcolo la probabilità del primo token con add-one smoothing
            bigrammi=list(nltk.bigrams(tokensFrase))#creo la lista dei bigrammi della singola frase
            for bigramma in bigrammi:
                probabilitàBigramma = (freq_bigrammi[bigramma]*1.0 + 1)/(freq_tokens[bigramma[0]]*1.0 + lunghezzaVocabolario) #calcolo la probabilità del bigramma con add-one smoothing
                prob1 = prob1*probabilitàBigramma #calcolo ricorsivamente la probabilità in termini markoviani
            #per ogni bigramma creo una tupla contenente la frase e la relativa probabilità e la aggiungo a Prob_Markov
            tuplaFraseMarkov = (prob1, frase)
            Prob_Markov.append(tuplaFraseMarkov)

    frasi_Markov_8 = []
    frasi_Markov_9 = []
    frasi_Markov_10 = []
    frasi_Markov_11 = []
    frasi_Markov_12 = []
    frasi_Markov_13 = []
    frasi_Markov_14 = []
    frasi_Markov_15 = []

    #per ogni bigramma probabilità-frase, tokenizzo la frase, controllo la sua lunghezza e la aggiungo alla rispettiva lista
    for bigramma in Prob_Markov:
        tokens = nltk.word_tokenize(bigramma[1])
        if len(tokens) == 8:
            frasi_Markov_8.append(bigramma)
        elif len(tokens) == 9:
            frasi_Markov_9.append(bigramma)
        elif len(tokens) == 10:
            frasi_Markov_10.append(bigramma)
        elif len(tokens) == 11:
            frasi_Markov_11.append(bigramma)
        elif len(tokens) == 12:
            frasi_Markov_12.append(bigramma)
        elif len(tokens) == 13:
            frasi_Markov_13.append(bigramma)
        elif len(tokens) == 14:
            frasi_Markov_14.append(bigramma)
        elif len(tokens) == 15:
            frasi_Markov_15.append(bigramma)


    #ordino le liste in ordine decrescente
    frasi_ordinate_Markov8 = sorted(frasi_Markov_8, reverse=True)
    frasi_ordinate_Markov9 = sorted(frasi_Markov_9, reverse=True)
    frasi_ordinate_Markov10 = sorted(frasi_Markov_10, reverse=True)
    frasi_ordinate_Markov11 = sorted(frasi_Markov_11, reverse=True)
    frasi_ordinate_Markov12 = sorted(frasi_Markov_12, reverse=True)
    frasi_ordinate_Markov13 = sorted(frasi_Markov_13, reverse=True)
    frasi_ordinate_Markov14 = sorted(frasi_Markov_14, reverse=True)
    frasi_ordinate_Markov15 = sorted(frasi_Markov_15, reverse=True)

    #creo una lista di liste contenenti le diverse tuple frase-probabilità
    frasi_ordinate_Markov = [frasi_ordinate_Markov8, frasi_ordinate_Markov9, frasi_ordinate_Markov10, frasi_ordinate_Markov11, frasi_ordinate_Markov12, frasi_ordinate_Markov13, frasi_ordinate_Markov14, frasi_ordinate_Markov15]



    lunghezze = 8
    #stampo per ogni frase di lunghezza tra 8 a 15, la frase con la probabilità di Markov maggiore
    for lista in frasi_ordinate_Markov:
        if not lista:
            print('Non esistono frasi di lunghezza',lunghezze)
        else:
            print('La frase di lunghezza', lunghezze,'con probabilità di Markov di ordine 1 maggiore è:')
            print('Frase:',lista[0][1], 'Probabilità Markov ordine 1:', lista[0][0])
            print()

        lunghezze += 1



def NamedEntityRecognition(tokensTOT):
    PersonList = [] #lista dei tokens etichettati come persona
    LocationList = [] #lista dei tokens etichettati come luogo
    tokensPOS = nltk.pos_tag(tokensTOT)
    analisi = nltk.ne_chunk(tokensPOS) #rappresentazione ad albero

    for nodo in analisi: #scorro i nodi dell'albero
        NE = ""
        if hasattr(nodo, 'label'): #controllo se nodo è una foglia o un nodo intermedio
            if nodo.label() in ['PERSON', 'GPE']: #controllo se il nodo è etichettato come un'entità di persona o luogo aggiungendolo alla rispettiva lista
                for partNE in nodo.leaves():
                    NE = NE + ' ' + partNE[0]
                if (nodo.label() == 'PERSON'):
                    PersonList.append(NE)
                elif (nodo.label() == 'GPE'):
                    LocationList.append(NE)

    #calcolo la frequenza dei tokens taggati come Person e GPE e li ordino in ordine decrescente
    freq_NER_Person = nltk.FreqDist(PersonList)
    freq_ordinate_NER_Person = freq_NER_Person.most_common(len(PersonList))


    freq_NER_Location = nltk.FreqDist(LocationList)
    freq_ordinate_NER_Location = freq_NER_Location.most_common(len(LocationList))

    print('I quindici nomi propri di persona più frequenti sono:')
    for i in range(15): #stampo i 15 tokens taggati Person più frequenti con relativa frequenza
        print('Nome:',freq_ordinate_NER_Person[i][0], 'Frequenza:',freq_ordinate_NER_Person[i][1])

    print()
    print('I quindici nomi propri di luogo più frequenti sono:')
    for i in range(15): #stampo i 15 tokens taggati GPE più frequenti con relativa frequenza
        print('Location:',freq_ordinate_NER_Location[i][0], 'Frequenza:',freq_ordinate_NER_Location[i][1])



def main(file1, file2):
    fileInput1 = open(file1, mode = 'r', encoding = 'utf-8')
    fileInput2 = open(file2, mode = 'r', encoding = 'utf-8')
    raw1 = fileInput1.read()
    raw2 = fileInput2.read()
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    frasi1 = sent_tokenizer.tokenize(raw1) #divide il testo in frasi
    frasi2 = sent_tokenizer.tokenize(raw2)
    print('I dieci POS più frequenti in',file1,'sono:')
    FrequenzaPOS(frasi1)
    print()
    FrequenzaNomiVerbi(frasi1)
    print()
    FrequenzaBigrammi(frasi1)
    print()
    tokensTOT1, bigrammi3_1 = EstraiBigrammi3(frasi1)
    bigrammiDiversi1 = BigrammaProbCong_CondMAX(tokensTOT1, bigrammi3_1)
    print()
    LocalMutualInfo(tokensTOT1, bigrammiDiversi1)
    print()
    frasi8_15_1 = EstraiFrasi(frasi1)
    MarkovUno(tokensTOT1, frasi8_15_1)
    print()
    NamedEntityRecognition(tokensTOT1)
    print()
    print()
    print('----------------------------------------------------')
    print()
    print()
    print('I dieci POS più frequenti in',file2,'sono:')
    FrequenzaPOS(frasi2)
    print()
    FrequenzaNomiVerbi(frasi2)
    print()
    FrequenzaBigrammi(frasi2)
    print()
    tokensTOT2, bigrammi3_2 = EstraiBigrammi3(frasi2)
    bigrammiDiversi2 = BigrammaProbCong_CondMAX(tokensTOT2, bigrammi3_2)
    print()
    LocalMutualInfo(tokensTOT2, bigrammiDiversi2)
    print()
    frasi8_15_2 = EstraiFrasi(frasi2)
    MarkovUno(tokensTOT2, frasi8_15_2)
    print()
    NamedEntityRecognition(tokensTOT2)




main (sys.argv[1], sys.argv[2])
