def find_pair_sum(nums, target_sum):
    num_indices, result_pairs = {}, []

    for i, num in enumerate(nums):
        complement = target_sum - num
        if complement in num_indices:
            result_pairs.append((num_indices[complement], i))
        #añadir el índice actual al diccionario incluso si no coincide con un complemento
        num_indices[num] = i

    return result_pairs

# EJEMPLO DE USO
nums = [3, 1, 5, 7, 5, 9]
target_sum = 10
result_pairs = find_pair_sum(nums, target_sum)

print(result_pairs)
