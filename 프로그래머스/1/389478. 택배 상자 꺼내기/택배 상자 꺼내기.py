def solution(n, w, num):

    stacks = [[] for _ in range(w)]
    boxes = list(range(1, n + 1))[::-1]

    reverse_flow = False
    target_box_index = None

    while boxes:
        if not reverse_flow:
            for i in range(w):
                if not boxes:
                    break
                box = boxes.pop()
                if target_box_index is None and box == num:
                    target_box_index = i
                    counter = 1
                elif target_box_index is not None and target_box_index == i:
                    counter += 1
                stacks[i].append(box)
                # print(box, reverse_flow, target_box_index)
            reverse_flow = not reverse_flow

        else:
            for i in range(w - 1, 0 - 1, -1):
                if not boxes:
                    break
                box = boxes.pop()
                if target_box_index is None and box == num:
                    target_box_index = i
                    counter = 1
                elif target_box_index is not None and target_box_index == i:
                    counter += 1
                stacks[i].append(box)
                # print(box, reverse_flow, target_box_index)
            reverse_flow = not reverse_flow

    return counter