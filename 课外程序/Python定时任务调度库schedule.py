# 导入模块
import schedule, time
# 定义一个任务
def work():
    print('我是定时的任务')
def test():
    print('我是定时的任务2')
# 设置定时
# 每10秒执行一次
schedule.every(10).seconds.do(test)

# 部署每10分钟执行一次test()函数的任务
schedule.every(10).minutes.do(test)

#部署每×小时执行一次test()函数的任务
schedule.every().hour.do(test)

# 部署在每天的08:00执行test()函数的任务
schedule.every().day.at("08:00").do(test)

# 部署每个星期一执行test()函数的任务
schedule.every().monday.do(test)

# 部署每周三的13:15执行test()函数的任务
schedule.every().wednesday.at("13:15").do(test)

# 开始执行任务
while True:                 #加循环是为了执⾏完⼀次任务后不终⽌运⾏
    schedule.run_pending()  #运行所有可以运行的schedule任务
    time.sleep(1)           #让程序按秒来检查，如果检查太快，会浪费计算机的资源。