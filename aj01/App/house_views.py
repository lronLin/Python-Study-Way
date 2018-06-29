
import os

from flask import Blueprint, render_template, redirect, \
    url_for, session, request, jsonify

from App.models import Area, Facility, House, db, \
    HouseImage, User, Order
from utils import status_code
from utils.functions import is_login
from utils.setting import UPLOAD_DIR

house_blueprint = Blueprint('house', __name__)


@house_blueprint.route('/myhouse/', methods=['GET'])
def my_house():
    return render_template('myhouse.html')  # 返回页面


@house_blueprint.route('/myhouses/', methods=['GET'])
@is_login
def user_my_house():
    houses = House.query.filter(House.user_id == session['user_id']).all()
    houses_info = [house.to_dict() for house in houses]
    return jsonify(code=status_code.OK, houses_info=houses_info)


@house_blueprint.route('/newhouse/', methods=['GET'])
def new_house():
    return render_template('newhouse.html')  # 返回我的新房源


@house_blueprint.route('/area_facility/', methods=['GET'])
def area_facility():
    areas = Area.query.all()
    facilitys = Facility.query.all()

    areas_list = [area.to_dict() for area in areas]  # 序列化
    facilitys_list = [facility.to_dict() for facility in facilitys]
    return jsonify(code=status_code.OK,
                   areas=areas_list,
                   facilitys=facilitys_list)


@house_blueprint.route('/newhouse/', methods=['POST'])
def user_new_house():
    data = request.form.to_dict()
    facility_ids = request.form.getlist('facility')

    house = House()
    house.user_id = session['user_id']  # 用户编号
    house.title = data.get('title')  # 标题
    house.price = data.get('price')  # 单价
    house.area_id = data.get('area_id')  # 区域编号
    house.address = data.get('address')  # 地址
    house.room_count = data.get('room_count')  # 房间数目
    house.house_id = data.get('acreage')  # 房屋面积
    house.unit = data.get('unit')  # 几室几厅
    house.capacity = data.get('capacity')  # 容纳人数
    house.beds = data.get('beds')  # 床铺配置
    house.deposit = data.get('deposit')  # 押金
    house.min_days = data.get('min_days')  # 最少入住天数
    house.max_days = data.get('max_days')  # 最多入住天数

    facility_list = Facility.query.filter(Facility.id.in_(facility_ids)).all()  # Basequery结果需.all()
    house.facilities = facility_list
    try:
        house.add_update()
    except:
        db.session.rollback()
    return jsonify(code=status_code.OK, house_id=house.id)


@house_blueprint.route('/house_images/', methods=['POST'])
def house_images():
    house_id = request.form.get('house_id')
    house_image = request.files.get('house_image')

    save_url = os.path.join(UPLOAD_DIR, house_image.filename)
    house_image.save(save_url)

    # 保存房屋图片信息
    image_url = os.path.join('upload', house_image.filename)

    # 保存房屋的首图
    house = House.query.get(house_id)
    if not house.index_image_url:
        house.index_image_url = image_url
        house.add_update()

    h_image = HouseImage()
    h_image.house_id = house_id
    h_image.url = image_url
    try:
        h_image.add_update()
    except:
        db.session.rollback()
        return jsonify(status_code.DATABASE_ERROR)
    return jsonify(code=status_code.OK, image_url=image_url)


@house_blueprint.route('/detail/', methods=['GET'])
def detail():
    return render_template('detail.html')


# 接口
@house_blueprint.route('/detail/<int:id>/', methods=['GET'])
def house_detail(id):
    house = House.query.get(id)  # 查询
    house_info = house.to_full_dict()  # 详情

    # facility_list = house.facilities
    # facility_info = [facility.to_dict() for facility in facility_list]

    return jsonify(code=status_code.OK,
                   house_info=house_info)


@house_blueprint.route('/booking/', methods=['GET'])
def booking():
    return render_template('booking.html')


@house_blueprint.route('/index/', methods=['GET'])
def index():
    return render_template('index.html')


@house_blueprint.route('/hindex/', methods=['GET'])
def hindex():
    username = ''
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        username = user.name

    houses = House.query.order_by(House.id.desc()).all()[:5]
    houses_info = [house.to_dict() for house in houses]

    return jsonify(code=status_code.OK, username=username, houses_info=houses_info)


@house_blueprint.route('/search/', methods=['GET'])
def search():
    return render_template('search.html')


@house_blueprint.route('/house_search/', methods=['GET'])
def house_search():

    search_dict = request.args
    aid = search_dict.get('aid')  # 区域id
    sd = search_dict.get('sd')  # 开始时间
    ed = search_dict.get('ed')  # 结束时间
    # 通过区域搜索房屋信息
    houses = House.query.filter(House.area_id == aid)
    # 房东过滤掉自己的房屋信息
    if 'user_id' in session:
        houses = houses.filter(House.user_id != session['user_id'])

    # 判断搜索的开始时间结束时间和房屋订单的开始时间和结束时间
    # 第一种情况
    order1 = Order.query.get(Order.begin_date >= sd, Order.begin_date >= ed).all()
    # 第二种情况
    order2 = Order.query.get(Order.end_date >= sd, Order.end_date <= ed).all()
    # 第三种情况
    order3 = Order.query.get(Order.begin_date <= sd, Order.end_date >= ed).all()
    # 第四种情况
    order4 = Order.query.get(Order.begin_date >= sd, Order.end_date <= ed).all()

    house_ids1 = [order.house_id for order in order1]
    house_ids2 = [order.house_id for order in order2]
    house_ids3 = [order.house_id for order in order3]
    house_ids4 = [order.house_id for order in order4]
    # 不需要搜索出来的房屋信息
    house_list_ids = list(set(house_ids1 + house_ids2 + house_ids3 + house_ids4))

    hlist = houses.filter(House.id.notin_(house_list_ids)).all()
    house_info = [house.to_dict() for house in hlist]

    return jsonify(code=status_code.OK, house_info=house_info)

