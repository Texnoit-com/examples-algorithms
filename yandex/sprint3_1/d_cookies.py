'''К Васе в гости пришли одноклассники. Его мама решила угостить ребят
печеньем. Но не всё так просто. Печенья могут быть разного размера.
 А у каждого ребёнка есть фактор жадности —– минимальный размер печенья,
которое он возьмёт. Нужно выяснить, сколько ребят останутся довольными
в лучшем случае, когда они действуют оптимально.
Каждый ребёнок может взять не больше одного печенья.'''


def comparison(greeds, cookies, index1, index2,
               lenght_greeds, lenght_cookies, count):
    if index1 == lenght_greeds or index2 == lenght_cookies:
        print(count)
        return
    if greeds[index1] <= cookies[index2]:
        comparison(greeds, cookies, index1+1,
                   index2+1, lenght_greeds,
                   lenght_cookies, count+1)
    else:
        comparison(greeds, cookies, index1,
                   index2+1, lenght_greeds,
                   lenght_cookies, count)


def get_pleasure(greeds, cookies):
    greeds = list(map(int, greeds.split(' ')))
    cookies = list(map(int, cookies.split(' ')))
    greeds.sort()
    cookies.sort()
    lenght_greeds = len(greeds)
    lenght_cookies = len(cookies)
    count = 0
    #comparison(greeds, cookies, 0, 0, lenght_greeds, lenght_cookies, 0)
    for i in range(lenght_greeds):
        if cookies and greeds[lenght_greeds-1-i] <= cookies[-1]:
            cookies.pop()
            count += 1
    print(count)



if __name__ == '__main__':
    '''_ = input()
    greeds = input()
    _ = input()
    cookies = input()
    get_pleasure(greeds, cookies)'''
    get_pleasure('8 5 5 8 6 9 8 2 4 7', '9 8 1 1 1 5 10 8')
