# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)

CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return render_template('movies.html')

class Explore(Resource):
    def get(self):
        return {'id': '10001', 'name': 'Amay', 'age': 18}

api.add_resource(Explore, '/api/explore')

class Movies(Resource):
    def get(self):
        movie1 = {
            'id': '26387939',
            'title': '摔跤吧！爸爸',
            'intro': '''导演: 涅提·蒂瓦里
编剧: 比于什·古普塔 / 施热亚·简
主演: 阿米尔·汗 / 法缇玛·萨那·纱卡 / 桑亚·玛荷塔 / 阿帕尔夏克提·库拉那 / 沙克希·坦沃 / 更多...
类型: 剧情 / 传记 / 运动
制片国家/地区: 印度
语言: 印地语
上映日期: 2017-05-05(中国大陆) / 2016-12-23(印度)
片长: 161分钟(印度) / 140分钟(中国大陆)
又名: 我和我的冠军女儿(台) / 打死不离3父女(港) / 摔跤吧！老爸 / 摔跤家族 / दंगल / Wrestling Competition''',
            'cover_url': 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2457983084.webp',
            'rating': 9.1
        }

        movie2 = {
            'id': '1292052',
            'title': '肖申克的救赎',
            'intro': '''导演: 弗兰克·德拉邦特
编剧: 弗兰克·德拉邦特 / 斯蒂芬·金
主演: 蒂姆·罗宾斯 / 摩根·弗里曼 / 鲍勃·冈顿 / 威廉姆·赛德勒 / 克兰西·布朗 / 更多...
类型: 剧情 / 犯罪
制片国家/地区: 美国
语言: 英语
上映日期: 1994-09-10(多伦多电影节) / 1994-10-14(美国)
片长: 142 分钟
又名: 月黑高飞(港) / 刺激1995(台) / 地狱诺言 / 铁窗岁月 / 消香克的救赎''',
            'cover_url': 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.webp',
            'rating': 9.6
        }

        movie3 = {
            'id': '1295644',
            'title': '这个杀手不太冷',
            'intro': '''导演: 吕克·贝松
编剧: 吕克·贝松
主演: 让·雷诺 / 娜塔莉·波特曼 / 加里·奥德曼 / 丹尼·爱罗 / 彼得·阿佩尔 / 更多...
类型: 剧情 / 动作 / 犯罪
制片国家/地区: 法国
语言: 英语 / 意大利语 / 法语
上映日期: 1994-09-14(法国)
片长: 110分钟(剧场版) / 133分钟(国际版)
又名: 杀手莱昂 / 终极追杀令(台) / 杀手里昂 / Leon / Leon: The Professional''',
            'cover_url': 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p511118051.webp',
            'rating': 9.4
        }

        movie4 = {
            'id': '26683290',
            'title': '你的名字',
            'intro': '''导演: 新海诚
编剧: 新海诚
主演: 神木隆之介 / 上白石萌音 / 长泽雅美 / 市原悦子 / 成田凌 / 更多...
类型: 剧情 / 爱情 / 动画
官方网站: www.kiminona.com
制片国家/地区: 日本
语言: 日语
上映日期: 2016-12-02(中国大陆) / 2016-08-26(日本)
片长: 106分钟
又名: 你的名字 / 君之名 / Your Name''',
            'cover_url': 'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2395733377.webp',
            'rating': 8.5
        }

        return [movie1, movie2, movie3, movie4]

api.add_resource(Movies, '/api/movies')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
