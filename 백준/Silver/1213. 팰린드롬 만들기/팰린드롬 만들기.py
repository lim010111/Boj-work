def palindrome_name(name: str) -> None:
    result = ""
    char_counter = {}
    for char in name:
        if char not in char_counter:
            char_counter[char] = 0
        char_counter[char] += 1

    if len(name) % 2 == 0:
        for char in sorted(char_counter.keys()):
            if char_counter[char] % 2 == 1:
                print("I'm Sorry Hansoo")
                return
            result += char * (char_counter[char]//2)
        print(result + result[::-1])
        return
        
    else:
        mid_char = ""
        for char in char_counter.keys():
            if char_counter[char] % 2 == 1:
                if mid_char:
                    print("I'm Sorry Hansoo")
                    return
                else:
                    mid_char = char
        

        for char in sorted(char_counter.keys()):
            result += char * (char_counter[char]//2)
        print(result + mid_char + result[::-1])
        return
            

            
    

if __name__ == "__main__":
    name = input()
    palindrome_name(name)