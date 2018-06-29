from django.conf.urls import url

from axf import views

urlpatterns = [
    # 首页
    url(r'^home/', views.home, name='home'),
    # 个人中心
    url(r'^mine/', views.mine, name='mine'),
    # 闪购超市
    url(r'^market/$', views.market, name='market'),
    # 正则表达式(字符串中,前面一部分固定用正则匹配, 后面一部分固定用正则匹配, 中间这部分不固定,然后用括号把组括起来)
    url(r'^market/(\d+)/(\d+)/(\d+)/', views.user_market, name='market_params'),

    # 添加购物车
    url(r'^addCart/', views.add_Cart, name='addCart'),
    # 减少购物车
    url(r'^subCart/', views.sub_cart, name='subCart'),

    # 购物车页面
    url(r'^cart/', views.cart, name='cart'),

    # 修改购物车中商品的选择情况
    url(r'^changeSelectStatus/', views.change_select_status, name='change_select_status'),

    # 下单
    url(r'^generateOrder/', views.generate_order, name='generate_order'),

    # 修改订单状态
    url(r'^changeOrderStatus/', views.change_order_status, name='change_order_status'),

    # 代付款订单
    url(r'^waitPay/', views.order_wait_pay, name='order_wait_pay'),

    # 待收货
    url(r'^payed/', views.order_payed, name='order_payed'),

    # 代付款订单支付
    url(r'^waitPayToPayed/', views.wait_pay_to_payed, name='wait_pay_to_payed'),

    # 全选
    url(r'^changeCartAllSelect/', views.change_cart_all_select, name='change_cart_all_select'),

    # 总价
    url(r'^countPrice/', views.count_price, name='count_price'),

]