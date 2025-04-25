from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
import re
from django.core.paginator import Paginator
from xiaomijiaju.models import Product, InstallationRequest

def product_list(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    price = request.GET.get('price', '')

    products = Product.objects.all()

    if query:
        products = products.filter(Q(name__icontains=query))
    if category:
        products = products.filter(category=category)
    if price:
        if price == '0-1000':
            products = products.filter(price__gte=0, price__lte=1000)
        elif price == '1000-2000':
            products = products.filter(price__gte=1000, price__lte=2000)
        elif price == '2000+':
            products = products.filter(price__gte=2000)

    paginator = Paginator(products.order_by('id'), 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product_list.html', {'page_obj': page_obj, 'query': query, 'category': category, 'price': price})


def category_nav(request):
    categories = {
        '厨房储物': ['橱柜', '储物柜', '置物架', '吊柜', '酒柜'],
        '厨房桌台': ['岛台', '吧台', '折叠桌', '餐边柜', '推车'],
    }
    return render(request, 'category_nav.html', {'categories': categories})

def kitchen_furniture(request):
    features = [
        {'title': '智能控制', 'description': '通过小米智能家居APP远程操控。', 'image': 'img/znkz.jpg'},
    ]
    products = [
        {'name': '小米厨房家具橱柜', 'price': '¥2499', 'image': 'img/chug.jpg'},
    ]
    return render(request, 'kitchen_furniture.html', {'features': features, 'products': products})

def installation(request):
    if request.method == 'POST':
        messages.success(request, '预约提交成功！')
        return render(request, 'installation.html')
    return render(request, 'installation.html')

def about(request):
    return render(request, 'about.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # 登录成功，传递 login_success
            return render(request, 'login.html', {'login_success': True, 'next': request.POST.get('next', 'product_list')})
        else:
            # 登录失败，传递 login_error
            return render(request, 'login.html', {'login_error': True, 'next': request.POST.get('next', '')})
    return render(request, 'login.html', {'next': request.GET.get('next', '')})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, '两次密码不一致')
            return render(request, 'register.html')

        if not re.match(r'^[A-Za-z0-9_]{3,20}$', username):
            messages.error(request, '用户名需3-20位，包含字母、数字或下划线')
            return render(request, 'register.html')

        if not re.match(r'^1[3-9]\d{9}$', phone):
            messages.error(request, '请输入有效的11位手机号')
            return render(request, 'register.html')

        if len(password) < 6:
            messages.error(request, '密码至少6位')
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, '用户名已存在')
            return render(request, 'register.html')

        try:
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            user.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, '注册成功！')
            return redirect('product_list')
        except Exception as e:
            messages.error(request, '注册失败，请稍后再试')
            return render(request, 'register.html')

    return render(request, 'register.html')

def delete_account(request):
    if not request.user.is_authenticated:
        messages.error(request, '请先登录')
        return redirect('login')

    if request.method == 'POST':
        user = request.user
        try:
            user.delete()
            logout(request)
            messages.success(request, '账号已成功删除')
            return redirect('home')
        except Exception as e:
            messages.error(request, '删除账号失败，请稍后再试')
            return render(request, 'delete_account.html')

    return render(request, 'delete_account.html')
def custom_logout(request):
    logout(request)
    messages.success(request, '已成功退出登录')
    return redirect('home')
def installation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        product = request.POST.get('product')
        date = request.POST.get('date')
        notes = request.POST.get('notes', '')
        InstallationRequest.objects.create(
            name=name,
            phone=phone,
            address=address,
            product=product,
            date=date,
            notes=notes
        )
        messages.success(request, '预约提交成功！')
        return render(request, 'installation.html')
    return render(request, 'installation.html')
