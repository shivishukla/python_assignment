"""
Module contains utilities for anagram
and function using multiprocessing for number square and its sum.
"""
import multiprocessing


class Solution:
    """
    class contains utilities for anagram
    pram: input_list: type=list
    """

    def __init__(self, input_list):
        self.input_list = input_list

    def groupanagrams(self):
        """
        function check the attribute is anagram or not
        :return: list of anagram
        """
        output_dict = {}
        for item in self.input_list:
            anagram_set = set()
            for temp_item in self.input_list:
                if sorted(item) == sorted(temp_item):
                    anagram_set.add(temp_item)
            output_dict[''.join(sorted(item))] = list(anagram_set)
        output = output_dict.values()
        return output


def square_list(input_list, result_array, square_sum_value):
    """
    function to square a given list
    """
    for index, num in enumerate(input_list):
        result_array[index] = num * num

    square_sum_value.value = sum(result_array)
    print("Input list: {}".format(input_list))
    print("Result: Square list (in process): {}".format(result_array[:]))
    print("Sum of squares(in process): {}".format(square_sum_value.value))


if __name__ == "__main__":

    obj_solution = Solution(["eat", "tea", "tan", "ate", "nat", "bat"])
    result = obj_solution.groupanagrams()
    print(result)
    print('\n')

    input_list = [1, 2, 3, 4, 5]
    result_array = multiprocessing.Array('i', 5)
    square_sum_value = multiprocessing.Value('i')

    p1 = multiprocessing.Process(target=square_list, args=(input_list, result_array, square_sum_value))
    p1.start()
    p1.join()

    print("Result; Square list (in main program): {}".format(result_array[:]))
    print("Sum of squares(in main program): {}".format(square_sum_value.value))
