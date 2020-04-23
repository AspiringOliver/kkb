sig = 'null'
flag = 0
def number():
    global result,sig, flag
    try:
        num = float(input(' '))
        if sig == 'null':
            result = num
        elif sig == '+':
            result = result + num
        elif sig == '-':
            result = result - num
        elif sig == '*':
            result = result * num
        else:
            result = result / num
    except ValueError as err:
        #即使捕获到异常，本身也不会跳出循环
        print('传入了无效参数：\n%s'%err)
        flag = 1

def signal():
    global result,sig, flag
    sig = input(' ')
    if sig == '=':
        print(round(result,8))
        flag = 1
    if sig != '+'and sig != '-'and sig != '*'and sig != '/'and sig != '=':
        print('您输入的不规范！')
        flag = 1