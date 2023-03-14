# merge_sort function inspered by trybe course


def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)

    if (end - start) > 1:  # se não reduzi o suficiente, continua

        mid = (start + end) // 2  # encontrando o meio

        merge_sort(arr, start, mid)  # dividindo as listas

        merge_sort(arr, mid, end)

        merge(arr, start, mid, end)  # unindo as listas


# função auxiliar que realiza a mistura dos dois arrays


def merge(arr, start, mid, end):
    left = arr[start:mid]  # indexando a lista da esquerda

    right = arr[mid:end]  # indexando a lista da direita

    left_index, right_index = 0, 0  # as duas listas começarão do início

    for general_index in range(
        start, end
    ):  # percorrer sobre a lista inteira como se fosse uma

        if left_index >= len(
            left
        ):  # se os elementos da esquerda acabaram, preenche o restante com a lista da direita

            arr[general_index] = right[right_index]

            right_index = right_index + 1

        elif right_index >= len(
            right
        ):  # se os elementos da direita acabaram, preenche o restante com a lista da esquerda

            arr[general_index] = left[left_index]

            left_index = left_index + 1

        elif (
            left[left_index] < right[right_index]
        ):  # se o elemento do topo da esquerda for menor que o da direita, ele será o escolhido

            arr[general_index] = left[left_index]

            left_index = left_index + 1

        else:

            arr[general_index] = right[
                right_index
            ]  # caso o da direita seja menor, ele será o escolhido

            right_index = right_index + 1


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ("", "", False)

    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    merge_sort(first_list)
    merge_sort(second_list)

    str1 = "".join(first_list)
    str2 = "".join(second_list)

    is_strings_a_anagram = str1 == str2

    tuple = (str1, str2, is_strings_a_anagram)

    return tuple
