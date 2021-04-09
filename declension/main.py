# Iterate numbers through range
for i in range(1, 21):
    if i == 1:
        ending = ""
    elif 2 <= i <= 4:
        ending = "а"
    else:
        ending = "ов"

    print(i, "процент" + ending)
