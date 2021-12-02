import db_manager as dbm
import matrix_util as utils

matr_test1 = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
]

matr_gui = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

clean_matrix = utils.matrix_cleaner(matr_test1)
clean_matrix_gui = utils.matrix_cleaner(matr_gui)

print("Original matrix")
utils.matrix_printer(matr_test1)

print("Original matrix")
utils.matrix_printer(matr_gui)

# print("Cleared matrix (vertical):")
# matrix_printer(vertical_clean)
# print("Cleared matrix (horizontal):")
# matrix_printer(horizontalClean)


print("Cleared matrix:")
utils.matrix_printer(clean_matrix)
print("Cleared matrix:")
utils.matrix_printer(clean_matrix_gui)

print("90-degrees matrix:")
rotated = utils.rotate_by_90(clean_matrix)
utils.matrix_printer(rotated)
rotated = utils.rotate_by_90(rotated)

print("180-degrees  matrix:")
utils.matrix_printer(rotated)
rotated = utils.rotate_by_90(rotated)

print("270-degrees matrix:")
utils.matrix_printer(rotated)

dbm.init()
# if dbm.insert('b', 'alphabet', utils.serialize_matrix(clean_matrix), utils.generate_serialized_list(clean_matrix)):
#     print("Tupla inserita con successo")
# else:
#     print("Tupla non inserita")
print(f"Il pattern trovato ha nome = {dbm.search_pattern(utils.generate_serialized_list(rotated), 'alphabet')}")


