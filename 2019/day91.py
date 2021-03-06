from under100.day65 import test


# https://edabit.com/challenge/ASpHKyuSXZL3MjL92
def amplify(num):
    num_list = [i for i in range(1, num + 1)]
    for i in range(len(num_list)):
        if not num_list[i] % 4:
            num_list[i] *= 10
    return num_list


# https://edabit.com/challenge/r9y4yrSAGRaqTT7nM
def find_missing(lst):
    if lst is None or not len(lst):
        return False
    lst.sort()
    a_list = []
    for i in lst:
        if not len(i) or i is None:
            return False
        a_list.append(len(i))
    a_list.sort()
    for l in range(len(a_list)):
        if a_list[l] + 1 != (a_list[l + 1]):
            return a_list[l] + 1


# IndexError: list index out of range
# https://edabit.com/challenge/35JtGyWLFhxGkHNnj
def sel_reverse(lst, length):
    if not length:
        return lst
    if length > len(lst):
        return lst[::-1]
    r_list = []
    for i in range(len(lst)):
        r_list.append(lst[length])
        for ii in range(length):
            r_list.append(lst[ii])


def test_suite():
    test(amplify(4) == [1, 2, 3, 40])
    test(amplify(3) == [1, 2, 3])
    test(amplify(25) == [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240,
                         25])
    test((amplify(1), [1]))
    test((amplify(4), [1, 2, 3, 40]))
    test((amplify(25),
          [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240,
           25]))
    test((amplify(100),
          [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25,
           26, 27, 280, 29, 30, 31, 320, 33, 34, 35, 360, 37, 38, 39, 400, 41, 42, 43, 440, 45, 46, 47,
           480, 49, 50, 51, 520, 53, 54, 55, 560, 57, 58, 59, 600, 61, 62, 63, 640, 65, 66, 67, 680, 69,
           70, 71, 720, 73, 74, 75, 760, 77, 78, 79, 800, 81, 82, 83, 840, 85, 86, 87, 880, 89, 90, 91,
           920, 93, 94, 95, 960, 97, 98, 99, 1000]))
    test((amplify(333),
          [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25,
           26, 27, 280, 29, 30, 31, 320, 33, 34, 35, 360, 37, 38, 39, 400, 41, 42, 43, 440, 45, 46, 47,
           480, 49, 50, 51, 520, 53, 54, 55, 560, 57, 58, 59, 600, 61, 62, 63, 640, 65, 66, 67, 680, 69,
           70, 71, 720, 73, 74, 75, 760, 77, 78, 79, 800, 81, 82, 83, 840, 85, 86, 87, 880, 89, 90, 91,
           920, 93, 94, 95, 960, 97, 98, 99, 1000, 101, 102, 103, 1040, 105, 106, 107, 1080, 109, 110, 111,
           1120, 113, 114, 115, 1160, 117, 118, 119, 1200, 121, 122, 123, 1240, 125, 126, 127, 1280, 129,
           130, 131, 1320, 133, 134, 135, 1360, 137, 138, 139, 1400, 141, 142, 143, 1440, 145, 146, 147,
           1480, 149, 150, 151, 1520, 153, 154, 155, 1560, 157, 158, 159, 1600, 161, 162, 163, 1640, 165,
           166, 167, 1680, 169, 170, 171, 1720, 173, 174, 175, 1760, 177, 178, 179, 1800, 181, 182, 183,
           1840, 185, 186, 187, 1880, 189, 190, 191, 1920, 193, 194, 195, 1960, 197, 198, 199, 2000, 201,
           202, 203, 2040, 205, 206, 207, 2080, 209, 210, 211, 2120, 213, 214, 215, 2160, 217, 218, 219,
           2200, 221, 222, 223, 2240, 225, 226, 227, 2280, 229, 230, 231, 2320, 233, 234, 235, 2360, 237,
           238, 239, 2400, 241, 242, 243, 2440, 245, 246, 247, 2480, 249, 250, 251, 2520, 253, 254, 255,
           2560, 257, 258, 259, 2600, 261, 262, 263, 2640, 265, 266, 267, 2680, 269, 270, 271, 2720, 273,
           274, 275, 2760, 277, 278, 279, 2800, 281, 282, 283, 2840, 285, 286, 287, 2880, 289, 290, 291,
           2920, 293, 294, 295, 2960, 297, 298, 299, 3000, 301, 302, 303, 3040, 305, 306, 307, 3080, 309,
           310, 311, 3120, 313, 314, 315, 3160, 317, 318, 319, 3200, 321, 322, 323, 3240, 325, 326, 327,
           3280, 329, 330, 331, 3320, 333]))
    test((amplify(500),
          [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25,
           26, 27, 280, 29, 30, 31, 320, 33, 34, 35, 360, 37, 38, 39, 400, 41, 42, 43, 440, 45, 46, 47,
           480, 49, 50, 51, 520, 53, 54, 55, 560, 57, 58, 59, 600, 61, 62, 63, 640, 65, 66, 67, 680, 69,
           70, 71, 720, 73, 74, 75, 760, 77, 78, 79, 800, 81, 82, 83, 840, 85, 86, 87, 880, 89, 90, 91,
           920, 93, 94, 95, 960, 97, 98, 99, 1000, 101, 102, 103, 1040, 105, 106, 107, 1080, 109, 110, 111,
           1120, 113, 114, 115, 1160, 117, 118, 119, 1200, 121, 122, 123, 1240, 125, 126, 127, 1280, 129,
           130, 131, 1320, 133, 134, 135, 1360, 137, 138, 139, 1400, 141, 142, 143, 1440, 145, 146, 147,
           1480, 149, 150, 151, 1520, 153, 154, 155, 1560, 157, 158, 159, 1600, 161, 162, 163, 1640, 165,
           166, 167, 1680, 169, 170, 171, 1720, 173, 174, 175, 1760, 177, 178, 179, 1800, 181, 182, 183,
           1840, 185, 186, 187, 1880, 189, 190, 191, 1920, 193, 194, 195, 1960, 197, 198, 199, 2000, 201,
           202, 203, 2040, 205, 206, 207, 2080, 209, 210, 211, 2120, 213, 214, 215, 2160, 217, 218, 219,
           2200, 221, 222, 223, 2240, 225, 226, 227, 2280, 229, 230, 231, 2320, 233, 234, 235, 2360, 237,
           238, 239, 2400, 241, 242, 243, 2440, 245, 246, 247, 2480, 249, 250, 251, 2520, 253, 254, 255,
           2560, 257, 258, 259, 2600, 261, 262, 263, 2640, 265, 266, 267, 2680, 269, 270, 271, 2720, 273,
           274, 275, 2760, 277, 278, 279, 2800, 281, 282, 283, 2840, 285, 286, 287, 2880, 289, 290, 291,
           2920, 293, 294, 295, 2960, 297, 298, 299, 3000, 301, 302, 303, 3040, 305, 306, 307, 3080, 309,
           310, 311, 3120, 313, 314, 315, 3160, 317, 318, 319, 3200, 321, 322, 323, 3240, 325, 326, 327,
           3280, 329, 330, 331, 3320, 333, 334, 335, 3360, 337, 338, 339, 3400, 341, 342, 343, 3440, 345,
           346, 347, 3480, 349, 350, 351, 3520, 353, 354, 355, 3560, 357, 358, 359, 3600, 361, 362, 363,
           3640, 365, 366, 367, 3680, 369, 370, 371, 3720, 373, 374, 375, 3760, 377, 378, 379, 3800, 381,
           382, 383, 3840, 385, 386, 387, 3880, 389, 390, 391, 3920, 393, 394, 395, 3960, 397, 398, 399,
           4000, 401, 402, 403, 4040, 405, 406, 407, 4080, 409, 410, 411, 4120, 413, 414, 415, 4160, 417,
           418, 419, 4200, 421, 422, 423, 4240, 425, 426, 427, 4280, 429, 430, 431, 4320, 433, 434, 435,
           4360, 437, 438, 439, 4400, 441, 442, 443, 4440, 445, 446, 447, 4480, 449, 450, 451, 4520, 453,
           454, 455, 4560, 457, 458, 459, 4600, 461, 462, 463, 4640, 465, 466, 467, 4680, 469, 470, 471,
           4720, 473, 474, 475, 4760, 477, 478, 479, 4800, 481, 482, 483, 4840, 485, 486, 487, 4880, 489,
           490, 491, 4920, 493, 494, 495, 4960, 497, 498, 499, 5000]))
    test(find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]) == 3)
    test(find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]) == 3)
    test(find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]) == 2)
    test(find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]) == 3)
    test(find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]) == 3)
    test(find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]) == 2)
    test(find_missing([[False], [False, False, False]]) == 2)
    test(find_missing(
        [["f", "r", "s"], ["d", "e"], ["a", "f", "b", "n"], ["z"], ["fg", "gty", "d", "dfr", "dr", "q"]]) ==
         5)
    test(find_missing([[5, 2, 9], [4, 5, 1, 1, 5, 6], [1, 1], [5, 6, 7, 8, 9]]) == 4)
    test(find_missing([]) == False)
    test(find_missing(None) == False)
    test(find_missing([[], [1, 2, 2]]) == False)
    test(sel_reverse([1, 2, 3, 4, 5, 6], 2) == [2, 1, 4, 3, 6, 5])
    test(sel_reverse([2, 4, 6, 8, 10, 12, 14, 16], 3) == [6, 4, 2, 12, 10, 8, 16, 14])
    test(sel_reverse([5, 7, 2, 6, 0, 4, 6], 100) == [6, 4, 0, 6, 2, 7, 5])
    test(sel_reverse([1, 2, 3, 4, 5, 6], 2) == [2, 1, 4, 3, 6, 5])
    test(sel_reverse([2, 4, 6, 8, 10, 12, 14, 16], 3) == [6, 4, 2, 12, 10, 8, 16, 14])
    test(sel_reverse([5, 7, 2, 6, 0, 4, 6], 100) == [6, 4, 0, 6, 2, 7, 5])
    test(sel_reverse([6, 0, 0, 0, 3, 8, 9, 7, 1], 9) == [1, 7, 9, 8, 3, 0, 0, 0, 6])
    test(sel_reverse([12, 54, 67, 34, 65, 34, 33], 0) == [12, 54, 67, 34, 65, 34, 33])
    test(sel_reverse([12, 54, 67, 34, 65, 34, 33], 1) == [12, 54, 67, 34, 65, 34, 33])
    test(sel_reverse([22, 13, 22, 13, 13, 22, 22, 13], 5) == [13, 13, 22, 13, 22, 13, 22, 22])
    test(sel_reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9])
    test(sel_reverse([1], 2) == [1])
    test(sel_reverse([1, 2], 2) == [2, 1])


if __name__ == '__main__':
    test_suite()
