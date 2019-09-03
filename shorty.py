from eunjeon import Mecab


def validate(msg):
    # print(len(msg.split()))
    # if len(msg.split()) == 1:
    #     return ['PASS', 'ONEWORD', ""]

    """'
    eunjeon.Mecab 를 이용해 입력받은 문장의 축을 이루는 명사+동사의 개수가
    전체 형태소의 개수보다 많을 경우wordpop() 함수롤 실행시킴.

    입력값에 대하여 선택적으로 봇이 답변하도록 하여 채팅창 도배를막음.
    """
    tagger = Mecab('/usr/local/lib/mecab/dic/mecab-ko-dic')
    Pos = tagger.pos(msg)
    numWord = 0  # 동사개수 - 형태소 분리 후 VV 개수로 파악.
    realword = []  # 실제 의미를 가지는 단어들
    target = ["NNG", "NNP", "NNB", "NNBC", "NP", "VV", "VA", "VX", "XSV", "XR", "MAG",
              "IC"]  # POS tag chart : https://bit.ly/2KOA1ua
    for i in Pos:
        if i[1] in target:
            print(i[0])
            numWord += 1
            realword.append(i[0])  # 실제 의미를 가지는 단어들만 전달되도록 필터링함.
    if Pos[-1][1] == "SF":  # 문장부호는 맨 마지막에 한번만 붙이도록.
        realword.append(Pos[-1][0])

    numPos = len(Pos)  # 전체 형태소의 개수
    print(Pos)
    print(numWord, numPos - numWord)
    if numWord >= (numPos - numWord):  # 의미를 가지는 요소가 문장의 과반 이상일 경우(비율은 수정가능)
        return wordpop(realword)
    else:
        return ["PASS", numWord, numPos]


def wordpop(msg):
    res = []
    print("input : ", msg)

    for i in msg:
        res.append(i[0])
    print(res)
    return res
