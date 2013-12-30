import urllib.request
import re
class qiubai:
    def __init__(self, page=1):
        self.page = page
    def search(self, page):
        url = "http://www.qiushibaike.com/week/page/%s" % page
        re_qb = re.compile(r'detail.*?<img.*?\s>(.*?)<.*?title="(.*?)">\s*(.*?)\s*?<', re.DOTALL)
        html = urllib.request.urlopen(url)
        text=html.read().decode("utf-8")

        my_qiubai = re_qb.findall(text)
        for s in my_qiubai:
            print("---",s[0],"----",s[1])
            print("内容：",s[2])
        s = input("回车继续,q退出")
        if s == "q":
            exit()
        else:
            page = int(page) + 1
            print("-"*18 + "第" + str(page) + "页" + "-"*18)
            self.search(page)
        print("-"*40)
    def query(self):
        global p
        p = input("输入要看的页数:")
        if p == "q":
            exit()
        elif not p.isdigit() or p == "0":
            self.query()
        else:
            print("-"*18 + "第" + p + "页" + "-"*18)
            self.search(p)
if __name__ == "__main__":
    print("-"*40)
    print("一入糗百深似海，从此节操是路人---hhdys")
    print('输入"q"退出程序')
    print("-"*40)
    qb = qiubai()
    qb.query()
