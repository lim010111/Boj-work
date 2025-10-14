def solution(N, channels: list[str]):
    commands = ""
    target_1_idx = channels.index("KBS1")
    commands += (target_1_idx) * "1" + (target_1_idx) * "4"

    target_2_idx = channels.index("KBS2") if target_1_idx < channels.index("KBS2") else channels.index("KBS2") + 1
    commands += (target_2_idx) * "1" + (target_2_idx - 1) * "4"
    
    return commands


if __name__ == "__main__":
    N = int(input())
    channels = [input() for _ in range(N)]
    ans = solution(N, channels)
    print(ans)