# Author: Tuyen Mathew Duong
# Email: tuyen@geekstrident.com
# Created Date: 2021-10-13


def rekey(text, key, is_reversed=False):
    lst = text.split(' ')
    l1 = sorted(set(map(int, str(key))))

    if not is_reversed:
        tmp_lst = []
        l1.reverse()
        for index in l1:
            if index < len(lst):
                tmp_lst.append(lst.pop(index))

        lst = tmp_lst + lst
    else:
        gap = len(l1)
        tmp_lst = lst[:gap]
        tmp_lst.reverse()
        lst = lst[gap:]
        for i, val in enumerate(tmp_lst):
            lst.insert(l1[i], val)

    new_text = ' '.join(lst)
    half = int(len(lst) / 2)
    print('{}\n{}\n{}'.format(new_text, ' '.join(lst[:half]), ' '.join(lst[half:])))
    return new_text
