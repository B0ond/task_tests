def yield_example(i):
    for i in range(i+1):
        yield i * i


print(f'Yield:')
for item in yield_example(4):
    print(item)


def yield_example2(i):
    for i in range(i+1):
        print(i*i)


print(f'через принт:')
yield_example2(4)