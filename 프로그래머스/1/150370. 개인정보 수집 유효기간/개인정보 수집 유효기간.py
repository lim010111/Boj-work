def solution(today, terms, privacies):
    '''
    for privacy in privacies:
        date, term
        if date + terms[term] >= today:
            파기_list.append(privacy_index)
    '''

    def is_expired(today, expiration):
        return today[0] * 365 + today[1] * 28 + today[2] >= expiration[0] * 365 + expiration[1] * 28 + expiration[2]

    terms_dic = {elem.split(' ')[0]:int(elem.split(' ')[1]) for elem in terms}

    today = list(map(int, today.split('.')))

    results = []

    for i, privacy in enumerate(privacies):
        date, term = privacy.split(' ')
        date = list(map(int, date.split('.')))
        date[1] += terms_dic[term]
        if date[1] > 12:
            date[0] += date[1] // 12
            date[1] %= 12

            if date[1] == 0:
                date[1] = 12
                date[0] -= 1

        print("today: ", today, "date: ", date)

        if is_expired(today, date):
            results.append(i + 1)

    return results