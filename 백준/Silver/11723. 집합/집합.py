import sys

input = sys.stdin.readline


def process(st: set, command: str, elem) -> None:
    if command == 'add':
        st.add(elem)

    elif command == 'remove':
        try:
            st.remove(elem)
        except KeyError:
            pass

    elif command == 'check':
        if elem in st:
            print(1)
        else:
            print(0)
    else:
        if elem in st:
            st.remove(elem)
        else:
            st.add(elem)

if __name__ == "__main__":
    st = set()
    for _ in range(int(input())):
        command_line = input().rstrip().split()
        command = command_line[0]
        if len(command_line) == 1:
            if command == 'all':
                st = set(range(1, 21))
            else:
                st = set()
                
        else:
            elem = int(command_line[1])
            process(st, command, elem)