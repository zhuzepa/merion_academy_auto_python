total_score = 0


def update_score(glass_count):
    global total_score
    total_score += glass_count


update_score(4)
update_score(20)
print(total_score)
