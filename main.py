import requests
import random
import time

print('**********  一个简单的刷问卷星的问卷数方法  **********'
      '\n\n **********  Version : 1.0.0  **********')

count = 50  # 这里填需要刷的问卷数
while count:
    count -= 1
    ktimes = random.randint(15, 50)

    # 这里填问卷url 目前模拟机制还不完善 代更新...
    url = "https://www.wjx.cn/joinnew/processjq.ashx?shortid=rSbaIY0&starttime=2021%2F12%2F26%2015%3A13%3A38&source" \
          "=directphone&submittype=1&ktimes={}&hlv=1&rn=237664522&jqpram=szwMyXEuE&jpm=13&isMtitle=1&iwx=1&t" \
          "=1640502850036&jqnonce=bf859da1-5a79-44aa-a155-e393fc9a9fb2&jqsign=ea%3F2%3Ecf6*2f0%3E*33ff*f622*b4%3E4ad" \
          "%3Ef%3Eae5".format(ktimes)
    # 请求体(data) 如:第一题有2个选项 那么就是'1$' + str(random.randint(1,2))
    #  到最后会趋于相等,请及时调整概率
    data = {
        'submitdata': '1$' + str(random.randint(1, 2)) +
                      '}2$' + str(random.randint(1, 4)) +
                      '}3$' + str(random.randint(2, 4)) +
                      '}4$' + str(random.randint(1, 1)) +
                      '}5$' + str(random.randint(1, 2)) +
                      '}6$' + str(random.randint(1, 1)) +
                      '}7$' + str(random.randint(2, 4)) +
                      '}8$' + str(random.randint(1, 2)) +
                      '}9$' + str(random.randint(2, 3)) +
                      '}10$' + str(random.randint(1, 2))
    }
    # 请求头
    header = {
        "Host": "www.wjx.cn",
        "Connection": "keep-alive",
        "Accept": "text/plain, */*; q\u003d0.01",
        "Origin": "https://www.wjx.cn",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1945A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
        "Referer": "https://www.wjx.cn/vm/eYwHv9E.aspx",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,en-US;q\u003d0.9",
    }

    response = requests.post(url, data, headers=header).status_code
    print('提交状态{}'.format(response))
    stimes = random.randint(1, 30)  # 生成随机停止时间
    print('停止', stimes, '秒')
    time.sleep(stimes)
