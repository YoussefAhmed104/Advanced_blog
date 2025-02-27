from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage




def paginate_queryset(queryset, request, per_page=5):
    paginator = Paginator(queryset, per_page)  
    page_num = request.GET.get('page', 1)  

    try:
        paginated_data = paginator.page(page_num)
    except PageNotAnInteger:
        paginated_data = paginator.page(1)  
    except EmptyPage:
        paginated_data = paginator.page(paginator.num_pages)  

    return paginated_data

# ✅ عرض الصفحة الرئيسية مع التصفح
def home(request):
    posts_list = Post.objects.all().order_by('-created_at')  # ترتيب الأحدث أولًا
    posts = paginate_queryset(posts_list, request)  # استخدام الدالة المستقلة

    username = request.user.username if request.user.is_authenticated else "Guest"
    return render(request, 'pages/home.html', {'posts': posts, 'username': username})

# ✅ عرض التفاصيل وإضافة التعليقات
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)  

    return render(request, 'pages/post_details.html', {'post': post, 'comments': comments, 'form': form})


def about(request):
    about_page = AboutPage.objects.all().first()
    return render(request,'pages/about.html',{ 'about_page' : about_page})



def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id) 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Comment.objects.create(post=post , name=name, email=email, content=message )
            return redirect('post_detail',post_id=post.id)  # استبدلها بصفحة النجاح المناسبة

    return redirect('post_detail',post_id=post.id)  # استبدلها بالصفحة التي تحتوي على التعليقات



def contact(request):
    contact_page = ContactPage.objects.all().first()
    if request.method =='POST':
        name = request.POST.get('name', 'Unknown')  # إذا لم يُرسل الاسم، سيكون "Unknown"
        email = request.POST.get('email', 'No Email Provided')
        message = request.POST.get('message', 'No Message')

        
        subject = f"New Message from {name}"
        full_message = f"Sender: {name}\nEmail: {email}\n\nMessage:\n{message}"
        email_message = EmailMessage(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,  # ✅ يبقى بريدك المرسل
            [settings.DEFAULT_TO_EMAIL],
            reply_to=[email],  # ✅ يجعل زر "رد" يوجه الرد إلى البريد الذي أدخله المستخدم
        )
        email_message.send(fail_silently=False)
    return render(request, 'pages/contact.html',{'contact_page':contact_page})


def all_posts(request):
    posts_list = Post.objects.all().order_by('-created_at') # ترتيب الأحدث أولًا
    return render(request, 'pages/posts.html', {'posts': posts_list})