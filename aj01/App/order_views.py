
from datetime import datetime

from flask import Blueprint, render_template, url_for, \
    session, request, jsonify

from App.models import Order, House, db
from utils.functions import is_login
from utils import status_code

order_blueprint = Blueprint('order', __name__)


# 创建订单
@order_blueprint.route('/create_order/', methods=['POST'])
@is_login
def create_order():

    # 获取begin_date,end_date,house_id,user_id的值
    begin_date = datetime.strftime(request.form.get('begin_date'), '%Y-%m-%d')
    end_date = datetime.strftime(request.form.get('end_date'), '%Y-%m-%d')
    house_id = request.form.get('house_id')
    user_id = session['user_id']

    # 验证begin_date, end_date是否存在
    if not all([begin_date, end_date]):
        return jsonify(status_code.ORDER_BEGIN_END_DATA_NOT_NULL)

    # 判断开始与结束时间(begin_date < end_date --> True)
    if begin_date > end_date:
        return jsonify(status_code.ORDER_BEGIN_DATA_GT_END_DATA_ERROR)

    house = House.query.get(house_id)

    order = Order()
    order.user_id = user_id
    order.house_id = house_id
    order.begin_date = begin_date
    order.end_date = end_date
    # strptime 将字符串转换成日期
    order.days = (end_date - begin_date).days + 1
    order.house_price = house.price
    order.amount = order.days * order.house_price

    order.add_update()

    return jsonify(status_code.SUCCESS)


# 查看我的订单
@order_blueprint.route('/orders/', methods=['GET'])
def orders():
    return render_template('orders.html')


@order_blueprint.route('/user_orders/', methods=['GET'])
@is_login
def user_orders():
    # 查看order
    orders = Order.query.filter(Order.user_id == session['user_id'])
    # 序列化
    orders_info = [order.to_dict() for order in orders]
    return jsonify(code=status_code.SUCCESS, orders_info=orders_info)


@order_blueprint.route('/lorders/', methods=['GET'])
def lorders():

    return render_template('/lorders.html')


@order_blueprint.route('/user_lorders', methods=['GET'])
@is_login
def user_lorders():
    # 先获取当前用户发布的房源的house_id
    houses = House.query.filter(House.user_id == session['user_id'])
    houses_ids = [house.id for house in houses]
    # 根据house_id去查询订单
    orders = Order.query.filter(Order.house_id.in_(houses_ids)).order_by(Order.id.desc()).all()
    orders_info = [order.to_dict() for order in orders]

    return jsonify(code=status_code.OK, orders_info=orders_info)


@order_blueprint.route('/orders/', methods=['PATCH'])
def change_orders_status():
    # 查看状态与id
    status = request.form.get('status')
    order_id = request.form.get('order_id')
    # 查询订单
    order = Order.query.get(order_id)
    order.status = status
    if status == 'REJECTED':
        order.comment = request.form.get('comment')
    # 过滤
    try:
        order.add_update()
    except:
        db.session.rollback()
        return jsonify(status_code.DATABASE_ERROR)
    return jsonify(status_code.SUCCESS)



