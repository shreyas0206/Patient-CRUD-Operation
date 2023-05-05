from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import Product,Category,Order
from .forms import SignUpform,LogInForm
from django.views.generic import View
from django.contrib import messages #for built in msges 
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from .middleware import auth_middleware,order_middleware
from django.utils.decorators import method_decorator
# Create your views here.
def index(request):
    return render(request,'index.html')

class AllProduct(View):
    def get(self,request):
        data=Product.objects.all()
        data1=Category.objects.all()
        print('You are =',request.session.get('email'))
        print('You are =',request.session.get('user.id'))
        
        # request.session.get('cart').clear()
        cart = request.session.get('cart')
        if not cart:
            request.session.cart ={}
        return render(request,'product.html',{'data':data,'data1':data1})

    def post(self,request):
        product = request.POST.get('product')
        print(product)
        remove= request.POST.get('remove')
        print(remove)
        cart = request.session.get('cart')
        if cart:
            quantity =  cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:    
                        cart[product] = quantity-1
                else: 
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart']=cart
        print('cart =',request.session['cart'])

        return redirect('/AllProduct')
        
class SignUpView(View):
    def get(self,request):
        form = SignUpform()
        return render(request,'sign_up.html',{'form':form})

    def post(self,request):
        form = SignUpform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Account Created Successfully !!!')
            return redirect('/login')
        else:
            return render(request,'sign_up.html',{'form':form})

class LogInView(View):
    return_url=None
    def get(self,request):
        LogInView.return_url=request.GET.get('return_url')
        form = LogInForm()
        
        return render(request,'log_in.html',{'form':form})
    
    def post(self,request):
        form=LogInForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username,password)
            # messages.success(request,f'Welcome {username}')
            user=authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                
                if LogInView.return_url:
                   return HttpResponseRedirect(LogInView.return_url)
                else:
                    LogInView.return_url = None
                    return redirect('/')


            else:
                return render(request,'log_in.html',{'form':form})

        else:
            return render(request,'log_in.html',{'form':form})
class Cart(View):
    @method_decorator( auth_middleware) #use middleware here
    
    def get(self,request):
        if request.session.get('cart') == None:
            request.session['cart'] = {}
        else:
            pass

        ids= list(request.session.get('cart').keys())
        print(list(request.session.get('cart').keys()))
        filter=Product.objects.filter(id__in=ids)
        print(filter)
        
        return render(request,'cart.html',{'filter':filter})
class UpdateUserView(UpdateView):
    model = User
    fields = ['username','email']
    template_name = 'Update.html'
    success_url = '/login'

class CheckOut(View,User):
    
    def post(self,request):
        print(request.POST)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        user =request.session.get('user_id')
        cart = request.session.get('cart')
        ids= list(request.session.get('cart').keys())
        print(list(request.session.get('cart').keys()))
        filter=Product.objects.filter(id__in=ids)
        print(address,phone,user,cart,filter)
        
        for allproducts in filter:
            order=Order(product = allproducts,
                        user = User(id=user),
                        price = allproducts.price,
                        address = address, 
                        phone = phone,
                        quantity = cart.get(str(allproducts.id)))
            order.save()
            # print(order.placeOrder())
        request.session['cart'] = {}
        return redirect('/cart')
class YourOrders(View):
    
    # @method_decorator( order_middleware) #use middleware here
    @method_decorator( auth_middleware) #use middleware here
    def get(Self,request):
        # if Order == 0:
        #     request.session.get('cart')
        # else:
        #     pass
        request.session.get('cart')
        user =request.session.get('user_id')
        orders = Order.get_orders_by_customer(user)
        print(orders)
        return render(request,'orders.html',{'orders':orders})

class logout(View):
    
    def get(self,request):
        
        request.session.clear()

#         Gesture control Bluetooth speakers using Arduino microcontroller boards are becoming increasingly popular. These speakers allow users to control the playback of music and adjust volume levels through hand gestures, making them an excellent choice for hands-free use.

# To create a gesture control Bluetooth speaker, an Arduino board is connected to a Bluetooth module, an amplifier, and a set of speakers. The board is then programmed with a code that uses an accelerometer or a gyroscope to detect hand gestures.

# The accelerometer or gyroscope senses the orientation and movement of the hand, and the Arduino code interprets these movements to determine the desired action. For example, a horizontal swipe may be used to skip to the next track, while a vertical swipe may be used to adjust the volume.

# The code can also be programmed to recognize different gestures based on the speed or direction of the hand movement. For example, a quick swipe to the left may result in a track being skipped forward, while a slow swipe to the left may result in a volume decrease.

# Once the Arduino board has interpreted the hand gesture, it sends the corresponding command to the Bluetooth module, which then transmits the signal to the connected device, such as a smartphone or tablet.

# Overall, gesture control Bluetooth speakers using Arduino boards are a fun and innovative way to enjoy music. They allow for hands-free use and provide a unique user experience. With their customizable code and ability to recognize a wide range of hand gestures, these speakers are sure to become even more popular in the future.




