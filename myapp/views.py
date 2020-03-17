from django.shortcuts import render
from django.http import HttpResponse
from . models import *




# Create your views here.
 
def fn_admin(request):
    return render(request,'admin/adminsign.html') 

def fn_category(request):
    category = Category.objects.filter().order_by('id')
    return render(request, 'admin/category.html', {'categories': category})

def fn_subcat(request):
    category = Category.objects.filter().order_by('id')
    subcat = Subcategory.objects.filter().order_by('id')
    return render(request,'admin/subcat.html',{'categories': category,'subcats':subcat}) 

def fn_brand(request):
    brandtab = Brand.objects.filter().order_by('id')
    print(brandtab)
    subcat = Subcategory.objects.filter().order_by('id')
    return render(request,'admin/brand.html',{'subcats': subcat , 'brandtabs': brandtab })

def fn_product(request):
    cat = Category.objects.filter().order_by('id')
    subcat = Subcategory.objects.filter().order_by('id')
    brand = Brand.objects.filter().order_by('id')
    return render(request,'admin/product.html', {'cats':cat, 'subcats': subcat, 'brands': brand}) 

# def fn_subtable(request):
#     subcat = Subcategory.objects.filter().order_by('id')
#     return render(request,'admin/subcat.html',{'subcats': subcat})

def fn_home(request):
    category = Category.objects.filter().order_by('id')
    return render(request,'user/home.html',{'categories':category})



def fn_userlog(request):
    return render(request, 'user/userlog.html')

def fn_signin(request):
    return render(request, 'user/usersign.html')

def fn_signin1(request):
    return render(request, 'user/usersign1.html')

def fn_prolist(request):
    return render(request, 'user/productlist.html')

def fn_cart(request):
    return render(request, 'user/cart.html')


def fn_adminLog( request):
    admin_name = request.POST['admin']
    password = request.POST['password']
    try:
        if admin_name == 'admin' and password=='12345678':
            return render(request,'admin/category.html')
        return render(request,'admin/adminsign.html', {'msg':'oops!!! Try Again'})
    except:
        return render(request,'admin/adminsign.html', {'msg':'oops!!! Enter valid Username'})


####### Login ###########################

def fn_userLogin( request):
    uname = request.POST['username']
    password = request.POST['password']
    try:
        login_obj = UserLog.objects.get(username=uname)
        # print(login_obj.password)
        if password == login_obj.password:
            request.session['user_id'] = login_obj.id
            reg = UserSignup.objects.get(userlog=login_obj.id)
            # return render(request,'timeline.html',{'user':reg})
            # return HttpResponse('logined')
        return render(request,'user/home.html',{'user':reg})
        return HttpResponse('password error')
    except Exception as e:
        print(str(e))
        return HttpResponse('username error')
        # return render(request, 'login.html')


######## Registraion ######################
 
 
def fn_UserSgup(request):
    if request.method == 'POST':
        email = request.POST['username']
        user_exist = UserLog.objects.filter(username=email).exists()     
        if not user_exist:
            name = request.POST['name']
            phone = request.POST['phone']
            address = request.POST['address']
            password = request.POST['password']
            try:
                sign_obj = UserLog(username=email, password=password)
                sign_obj.save()
                if sign_obj.id > 0:
                    insert_data=UserSignup(name=name, phone_number=phone, address=address,userlog=sign_obj)
                    insert_data.save()
                    if insert_data.id > 0:
                        return render(request,'user/userlog.html')
                        # return HttpResponse('logined')
            except Exception as e:
                print(str(e))
                # return render(request,'index.html')
                return HttpResponse('no reg')
        return HttpResponse("username already exist")
    # return request(request,'index.html')
    return HttpResponse('invaid')


####### Category ##############

def fn_cat_add(request):
    try:
        if request.method == 'POST':
            cat_name = request.POST['cat_name']
            user_exist = Category.objects.filter(category_name=cat_name).exists()  
            if not user_exist:
                cat_desc = request.POST['cat_desc']
                cat_image = request.FILES['image_upload']
                cat_obj = Category(category_name = cat_name, description = cat_desc, image = cat_image)
                cat_obj.save()
                return render(request,'admin/category.html')
            return HttpResponse('already entered')
    except Exception as e:
        print(str(e))
        return HttpResponse('error')


###### Subcategory ##########

def fn_subcat_add(request):
    if request.method == 'POST':
        cat = request.POST['category']
        subcat = request.POST['subcat']
        try:
            cat_obj = Category.objects.get(id=cat)
            subcat_obj = Subcategory(subcategory_name = subcat, category = cat_obj)
            subcat_obj.save()
            # subtab = Subcategory.objects.filter().order_by('id')
            return render(request, 'admin/subcat.html')
        except Exception as e:
            print(str(e))
            return HttpResponse('error')



####### Brand #############

def fn_brand_add(request):
    if request.method == 'POST':
        # cat = request.POST['category']
        subcat = request.POST['subcat']
        brand = request.POST['brand']
        try:
            subcat_obj = Subcategory.objects.get(id=subcat)
            print(brand)
            print(subcat_obj.subcategory_name)
            print(subcat_obj.category.category_name)
            brand_obj = Brand(brand_name = brand, subcat = subcat_obj)
            brand_obj.save()
            return render(request, 'admin/brand.html')
        except Exception as e:
            print(str(e))
            return HttpResponse('error')


########### PRODUCTS  ###########

def fn_product_add(request):
    try:
        if request.method == 'POST':
            pro_cat = request.POST['cat']
            pro_subcat = request.POST['subcat']
            pro_brand = request.POST['brand']
            pro_name = request.POST['proname']
            pro_quantity = request.POST['quantity']
            pro_mrp = request.POST['mrp']
            pro_drp = request.POST['drp']
            user_exist = Product.objects.filter(product_name=pro_name, pro_quantity=pro_quantity).exists()  
            if not user_exist:
                pro_desc = request.POST['desc']
                pro_image = request.FILES['image']
                pro_obj = Product(pro_cat = pro_cat, pro_subcat= pro_subcat, pro_brand = pro_brand, pro_name=pro_name, 
                pro_quantity=pro_quantity, pro_mrp= pro_mrp, pro_drp= pro_dr, description =pro_desc, image = pro_image)
                pro_obj.save()
                return render(request,'admin/category.html')
            return HttpResponse('already entered')
    except Exception as e:
        print(str(e))
        return HttpResponse('error')


###############################################

  