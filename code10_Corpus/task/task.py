from random import randint
NOUNS = ['세종', '한글', '한글날']

def get_rand():
    random_list = []
    for i in range(11):
        random_list.append(NOUNS[randint(0, 2)])
    return random_list

def get_rank(random_list):
    result = {}

    for n in random_list:
        if not (n in result):
            result[n] = 0
        result[n] += 1
    result = sorted(result.items(), key = lambda x:x[1], reverse = True )
    return result

if __name__ == "__main__":
    #result = get_rank(get_rand())
    print(get_rank(get_rand()))

    #for k, v in result:
    #    print(k)