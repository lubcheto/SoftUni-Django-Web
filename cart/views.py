from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from cart.models import Cart
from meals.models import RestaurantMeals

@login_required
def cart_view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {
            'cart': cart,
        }
    else:
        no_items_in_cart = "Your cart is empty"
        context = {
            'empty_message': no_items_in_cart,
            'empty': True,
        }

    return render(request, 'cart/view.html', context)


@login_required
def update_cart(request, pk):
    request.session.set_expiry(1200)  # seconds
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)
    request.session['cart_id'] = cart.id

    try:
        meal = RestaurantMeals.objects.get(pk=pk)
    except RestaurantMeals.DoesNotExist:
        pass

    if not meal in cart.products.all():
        cart.products.add(meal)
        meal.is_eatable=False  #change the state of the meal so it is not visible for search
        meal.save()
    else:
        cart.products.remove(meal)
        meal.is_eatable = True #change the state of the meal so it is  visible for search
        meal.save()

    updated_total = 0.00
    for meal in cart.products.all():
        updated_total += float(meal.price)
    request.session['meals_total'] = cart.products.count()
    cart.total = updated_total
    cart.save()
    return HttpResponseRedirect(reverse('cart'))



@login_required
def checkout(request,pk):
    if request.session['cart_id'] == pk:
        cart = Cart.objects.get(id=pk)
        user = request.user.userprofile

        if (cart.total)>(user.balance):
            error_message = "Not enough money"
            context = {
                'cart': cart,
                'error_message':error_message,
                'not_enough':True
            }
            return render(request, 'cart/view.html', context)
        else:
            success_message = "Successful purchase"
            user.balance-=cart.total
            user.save()

            updated_total = 0.00
            for meal in cart.products.all():
                updated_total += float(meal.price)
                meal.creator.sales_or_purchase+=1
                meal.creator.balance+=meal.price
                meal.creator.save()
                user.sales_or_purchase+=1
                cart.products.remove(meal)
                meal.delete()
            cart.total = updated_total

            cart.save()
            user.save()
            request.session['meals_total'] = cart.products.count()
            context = {
                'cart': cart,
                'success_message':success_message,

            }
            return render(request, 'cart/view.html', context)
















    #
    #
    # return HttpResponseRedirect(reverse('cart'))

#
# @login_required
# def like_pet(request, pk):
#     like = Like.objects.filter(user_id = request.user.userprofile.id, pet_id = pk).first()      #check if the user.userprofile.id is in the likes
#     if like:
#         like.delete()
#     else:
#         pet = Pet.objects.get(pk=pk)
#         like = Like(test=str(pk), user = request.user.userprofile)      #here we set the user to be the userprofile of the request.user
#         like.pet = pet
#         like.save()
#     return redirect('pet details', pk)