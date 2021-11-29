import numpy as np

def matrix_printer(matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            print(matr[i][j], end=" ")
        print(end="\n")
    print("\n")

def get_column(matr, i):
    return [row[i] for row in matr]

def rotate_by_90(matr):
    new_matrix = []
    horizontal_size = np.shape(matr)[1]  # prende la lunghezza in orizzontale
    for i in range(horizontal_size):
        column = get_column(matr, i)
        # ? lo mette al contrario https://stackoverflow.com/questions/6771428/most-efficient-way-to-reverse-a-numpy-array
        column = column[::-1]
        if len(new_matrix) == 0:
            new_matrix = [column]
        else:
            new_matrix.append(column)
    return new_matrix

def vertical_cleaner(matrice):
    new_matrix = matrice
    """
       shape returna la dimensione del vettore n 
       sottoforma di array di dimensioni in cui
       - la prima posizione è uguale alla dimensione in altezza della matrice
       (la dimensione dell'array contenitore)
       - in seconda posizione indica la dimensione degli array contenuti
       all'interno
    """
    horizontal_size = np.shape(matrice)[1]

    # array colonne da eliminare prima e dopo aver trovato un pattern
    rows_to_be_deleted_before = []
    rows_to_be_deleted_after = []

    # checker per il controllo della presenza di un
    pre_pattern_found = False

    for i in range(horizontal_size):
        # contrlla se ci sono 0
        #! forse è meglio creare un ciclo
        if not np.any(get_column(matrice, i)):
            if not pre_pattern_found:
                rows_to_be_deleted_before.append(i)
            else:
                rows_to_be_deleted_after.append(i)
        else:
            if not pre_pattern_found:
                pre_pattern_found = True
            else:
                rows_to_be_deleted_after = []

    total_to_be_deleted = rows_to_be_deleted_before
    total_to_be_deleted.extend(rows_to_be_deleted_after)

    # ? cancella orizzontalmente
    new_matrix = np.delete(matrice, total_to_be_deleted, 1)
    return new_matrix

def horizontal_cleaner(matrice):
    new_matrix = matrice
    # array righe da eliminare prima e dopo aver trovato un pattern
    rows_to_be_deleted_before = []
    rows_to_be_deleted_after = []

    # checker per il controllo della presenza di un
    pre_pattern_found = False

    #! horizontal
    # ? conto le righe vuote e le aggiungo all'array delle righe da cancellare
    for i in range(len(matrice)):
        # contrlla se ci sono 0
        #! forse è meglio creare un ciclo https://thispointer.com/6-ways-to-check-if-all-values-in-numpy-array-are-zero-in-both-1d-2d-arrays-python/
        if not np.any(matrice[i]):
            if not pre_pattern_found:
                rows_to_be_deleted_before.append(i)
            else:
                rows_to_be_deleted_after.append(i)
        else:
            if not pre_pattern_found:
                pre_pattern_found = True
            else:
                rows_to_be_deleted_after = []

    total_to_be_deleted = rows_to_be_deleted_before
    total_to_be_deleted.extend(rows_to_be_deleted_after)

    # ? cancella orizzontalmente
    new_matrix = np.delete(matrice, total_to_be_deleted, 0)

    return new_matrix


def matrix_cleaner(matrice):
    horizontalCleanMatrix = horizontal_cleaner(matrice)
    return vertical_cleaner(horizontalCleanMatrix)

# def delete_row(matr, obj):
#     matr = np.delete(matr, (0, 1), 1)
#     print(matr)

def serialize_matrix(matr):
    serialized = ''
    for row in matr:
        for element in row:
            serialized = serialized+str(element)
    return serialized

"""def generate_rotations_short(matr):
    return [rotate_by_90(matr) for i in range(4)]"""

# def generate_rotations(matr):
#     rotations = []
#     for i in range (4):
#         rotations.append(rotate_by_90(matr)) #90
#     return rotations

# def generate_or_list(matr):
#     return [serialize_matrix(matr = rotate_by_90(matr)) for i in range(4)]

def generate_serialized_list(matr):
    mat = matr
    serialized_array = []
    for i in range(4):
        mat = rotate_by_90(mat)
        serialized_array.append(serialize_matrix(mat))
    return serialized_array