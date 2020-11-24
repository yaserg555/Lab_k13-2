def f2():
    s=list(range(2,20))
    print(s[3:9])


def f6(s):
    print(f'1) {s[:len(s) // 2 + 1 * len(s) % 2]}')
    print(f'2) {s[:len(s) // 2]}')
    print(f'3) {s[:len(s) // 3]}')
    print(f'4) {s[len(s) // 2:]}')
    print(f'5) {s[len(s) // 2 + 1 * len(s) % 2:]}')
    print(f'6) {s[len(s) // 3:2 * len(s) // 3]}')
    print(f'7) {s[:10]}')
    print(f'8) {list(reversed(s[:10]))}')
    print(f'9) {s[2::3]}')
    print(f'10) {list(reversed(s[2::3]))}')


def f9a():
    try:
        x = int(input())
    except:
        return False
    else:
        s.append(x)
        return True
    
    
def f9b():
    try:
        x = int(input())
    except:
        s.clear()
        return False
    else:
        s.append(x)
        return True
