
from .models import Store, Menu
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import DeleteView
from .forms import StoreForm, MenuForm, OrderForm
from django.contrib import messages

# Create your views here.
class HomeView(View):
    def get(self, request):
        context ={}
        # add the dictionary during initialization
        context["stores"] = Store.objects.all().order_by('-updated_at')
            
        return render(request, "home.html", context)

class StoreView(View):
    def get(self, request):
        form = StoreForm()  
        return render(request,'stores.html',{'form':form}) 
    
    def post(self, request):
        form = StoreForm(request.POST)  
        if form.is_valid():   
            form.save()
            messages.success(request, "New Store Created.")  
            return redirect('/')  


class StoreUpdateView(View):
    def get(self, request, id):
        context = {}
        context["stores"] = Store.objects.get(id=id)
        print('store',context)
        return render(request, "update_store.html", context)
    
    def post(self, request, id):
        store = Store.objects.get(id=id)  
        form = StoreForm(request.POST, instance = store)  
        if form.is_valid():  
            form.save()
            messages.success(request, "Updated Successfully.")   
            return redirect("/")  
        return render(request, 'update_store.html', {'stores': store})
    

class StoreDeleteView(DeleteView):
    model = Store
    success_url ="/"
    template_name = "storemodel_confirm_delete.html" 
        
            

class MenuView(View):
    def get(self, request, id):
        context ={}
        # add the dictionary during initialization
        context["menus"] = Menu.objects.filter(store__id=id).order_by('-updated_at')
        context["store_id"] = id
        print(context)
        return render(request, "menu.html", context)
        


class NewMenu(View):
    
    def get(self, request, id):
        form = MenuForm()  
        return render(request,'add_menu.html',{'form':form, 'store_id':id}) 
    
    def post(self, request, id):
        form = MenuForm(request.POST)  
        print(request.POST)
        if form.is_valid():  
            try: 
                print('valid') 
                menu = form.save(commit=False)
                menu.store = Store.objects.get(id=id)
                menu.save()
                messages.success(request, "New Menu Created.") 
                return redirect(f'/menu/{menu.store.id}') 
            except Exception as _e:  
                print(_e)
        else:
            print('not valid')
            print(form.errors)
            


class MenuUpdateView(View):
    def get(self, request, id):
        context = {}
        context["menu"] = Menu.objects.get(id=id)
        return render(request, "update_menu.html", context)
    
    def post(self, request, id):
        menu = Menu.objects.get(id=id)  
        print('ss',id)
        form = MenuForm(request.POST, instance = menu)  
        if form.is_valid():  
            form.save()  
            print('ss',menu.store.id)
            messages.success(request, "Updated successfully.") 
            return redirect(f"/menu/{menu.store.id}") 
        print(form.errors) 
        return render(request, 'update_menu.html', {'menu': menu})
    

class MenuDeleteView(DeleteView):
    model = Menu
    success_url ="/"
    template_name = "storemodel_confirm_delete.html" 
    
    
class OrderView(View):
    def get(self, request, id):
        form = OrderForm()  
        return render(request,'order.html',{'form':form, 'menu_id':id})
    
    def post(self, request, id):
        form = OrderForm(request.POST)  
        print(request.POST)
        if form.is_valid():  
            try: 
                print('valid') 
                customer = form.save(commit=False)
                customer.menu = Menu.objects.get(id=id)
                customer.save()
                messages.success(request, "Order Placed") 
                return redirect(f'/menu/{customer.menu.store.id}') 
            except Exception as _e:  
                print(_e)
        else:
            print('not valid')
            print(form.errors)