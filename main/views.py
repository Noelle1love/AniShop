from shop import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, View, DetailView
from main.forms import ContactForm
from main.models import Main, AboutUs, Team, Blog, ContactSupport
from product.models import Category, Product
from django.contrib import messages
from django.core.paginator import Paginator


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *, object_list=None,  **kwargs):
        context = super().get_context_data(**kwargs)
        context["main"] = Main.objects.latest('id')
        context["categories"] = Category.objects.all()
        context["products"] = Product.objects.order_by('-id')[:3]
        context["blogs"] = Blog.objects.all()
        return context



class AboutUsView(TemplateView):
    template_name = "about-us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = AboutUs.objects.latest('id')
        context['teams']= Team.objects.all()
        return context

class BlogView(ListView):
    queryset = Blog.objects.all()
    template_name = 'blog.html'
    context_object_name = 'blogs'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Blogs'] = Blog.objects.all()
        return context

    def get(self, request, **args):
        query = request.GET.get('q')
        products = Blog.objects.filter(name__icontains=query) if query else Blog.objects.all()

        paginator = Paginator(products, self.paginate_by)
        page_number = request.GET.get('page')
        paginated_blogs = paginator.get_page(page_number)
        return render(request, self.template_name, {"blogs": paginated_blogs, 'query': query})

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog-details.html'
    context_object_name = 'blog'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()
        return context

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Blog,id = id)

class ContactView(View):
    template_name = 'contact.html'
    context_object_name = 'support'

    def get(self, request):
        form = ContactForm()
        support = ContactSupport.objects.latest('id')
        return render(request, self.template_name, {'form':form, 'support':support})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            send_mail(
                subject='Спасибо за обращение!',
                message='Мы получили ваше сообщение, и ответим вам в ближайшее время :)',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[contact_message.email],
                fail_silently=False
            )
            messages.success(request, 'Ваше сообщение отправлено!')
            return redirect('contact')
        messages.error(request, 'Ошибка! Пожалуйста исправьте ошибки в форме')





