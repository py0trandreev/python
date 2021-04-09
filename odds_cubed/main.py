odds_cubed = []
sum_digits = 0
sum_total = 0
#a.
for i in range(1, 1001):
    if i % 2 != 0:
        odds_cubed.append(i ** 3)


for j in range(len(odds_cubed)):
    current_val = odds_cubed[j]
    while current_val != 0:
        last_digit = current_val % 10
        current_val = current_val // 10
        sum_digits += last_digit

    if sum_digits % 7 == 0:
        sum_total += odds_cubed[j]
    sum_digits = 0

print(odds_cubed)
print(sum_total)

#b.
# Add 17 to every item
sum_total = 0

for i in range(len(odds_cubed)):
    odds_cubed[i] = odds_cubed[i] + 17

print(odds_cubed)

for j in range(len(odds_cubed)):
    current_val = odds_cubed[j]
    while current_val != 0:
        last_digit = current_val % 10
        current_val = current_val // 10
        sum_digits += last_digit

    if sum_digits % 7 == 0:
        sum_total += odds_cubed[j]
    sum_digits = 0
print(sum_total)