from sys import stdin

input = stdin.readline


def have_or_not(n, m, my_cards, cards):
    my_set = set(my_cards)
    return [1 if card in my_set else 0 for card in cards]


n = int(input())
my_cards = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))
answer = have_or_not(n, m, my_cards, cards)
print(*answer)