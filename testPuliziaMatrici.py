import numpy as np

def getColumn(matr,i):
    return [row[i] for row in matr]

def matrixPrinter(matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            print(matr[i][j], end=" ")
        print(end='\n')
    print('\n')

def rotateBy90(matr):
    newMatrice = []
    horizontalSize = np.shape(matr)[1]  #?prende la lunghezza in orizontale
    for i in range(horizontalSize):
        column = getColumn(matr, i)
        #? lo mette al contrario https://stackoverflow.com/questions/6771428/most-efficient-way-to-reverse-a-numpy-array
        column = column[::-1]
        if len(newMatrice)==0:
            #newMatrice = ([getColumn(matr, i)])
            newMatrice = [column]
        else:
            #newMatrice.append(getColumn(matr, i))
            newMatrice.append(column)
    return newMatrice


def verticalCleaner(matrice):
    newMatrice = matrice
    horizontalSize = np.shape(matrice)[1]
    
    #array righe da eliminare prima e dopo aver trovato un pattern
    rowsToBeDeletedBefore = []
    rowsToBeDeletedAfter = []

    #checker per il controllo della presenza di un
    prePatternFound = False

    for i in range(horizontalSize):
        #contrlla se ci sono 0
        #! forse è meglio creare un ciclo
        if(not np.any(getColumn(matrice,i))):
            if(not prePatternFound):
                rowsToBeDeletedBefore.append(i)            
            else:
                rowsToBeDeletedAfter.append(i)
        else:
            if(not prePatternFound):
                prePatternFound = True
            else:
                rowsToBeDeletedAfter = []

    totalToBeDeleted = rowsToBeDeletedBefore
    totalToBeDeleted.extend(rowsToBeDeletedAfter)

    #? cancella orizzontalmente
    newMatrice = np.delete(matrice,totalToBeDeleted,1)
    return newMatrice

def patternCleaner(matrice):
    newMatrice = matrice
    #array righe da eliminare prima e dopo aver trovato un pattern
    rowsToBeDeletedBefore = []
    rowsToBeDeletedAfter = []

    #checker per il controllo della presenza di un
    prePatternFound = False

    """
    shape returna la dimesnione del vettore n 
    sottforma di array di dimensioni in cui
    - la prima posizione è uguale alla dimensine in altezza della matrice
    (la dimensione dell'array contenitore)
    - in seconda posizione indica la dimensione degli array contenuti
    all'interno
    """

    #! horizontal
    #? conto le righe vuote e le aggiungo all'array delle righe da cancellare
    for i in range(len(matrice)):
        #contrlla se ci sono 0
        #! forse è meglio creare un ciclo https://thispointer.com/6-ways-to-check-if-all-values-in-numpy-array-are-zero-in-both-1d-2d-arrays-python/
        if(not np.any(matrice[i])):
            if(not prePatternFound):
                rowsToBeDeletedBefore.append(i)            
            else:
                rowsToBeDeletedAfter.append(i)
        else:
            if(not prePatternFound):
                prePatternFound = True
            else:
                rowsToBeDeletedAfter = []
    
    totalToBeDeleted = rowsToBeDeletedBefore
    totalToBeDeleted.extend(rowsToBeDeletedAfter)

    #? cancella orizzontalmente
    newMatrice = np.delete(matrice,totalToBeDeleted,0)

    return newMatrice

def deleteRow(matr, obj):
    matr = np.delete(matr,(0,1),1)
    print(matr)


matrTest1 = ([
    [1,0,1,0],
    [0,0,0,0],
    [0,1,0,0],
])
horizontalClean = patternCleaner(matrTest1)
verticalClean = verticalCleaner(horizontalClean)

matrixPrinter(verticalClean)
rotated = rotateBy90(verticalClean)
matrixPrinter(rotated)
rotated = rotateBy90(rotated)
matrixPrinter(rotated)
rotated = rotateBy90(rotated)
matrixPrinter(rotated)


#patternCleaner(matrTest1)