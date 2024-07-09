if __name__ == "__main__":
    power = 1
    for i in range(7830457):
        power *= 2
        power = power % 10**10
    print((28433 * power + 1) % 10**10)

