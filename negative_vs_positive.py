def positives_v_negatives(*args):
    positive_sum = 0
    negative_sum = 0
    is_negative = False
    for num in args:
        if num > 0:
            positive_sum += num
        else:
            negative_sum += num

    return negative_sum, positive_sum


numbers = [int(x) for x in input().split()]

negative_sum, positive_sum = positives_v_negatives(*numbers)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

