from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import BlogPostForm, BlogPostModelForm
from .models import BlogPost


# def blog_post_detail_page(request, slug):
# 	print("DJANGO SAYS", request.method, request.path, request.user)
# 	# queryset = BlogPost.objects.filter(slug=slug)
# 	# if queryset.count() == 0:
# 	# 	raise Http404
	
# 	obj = get_object_or_404(BlogPost, slug=slug)
# 	template_name = 'blog_post_detail.html'
# 	context = {"object": obj} #{"title": obj.title}
# 	return render(request, template_name, context)



# CRUD

# GET -> Retrieve / List

# POST -> Create / Update / DELETE

# Create Retrieve Update Delete


def blog_post_list_view(request):
	# list out objects
	# coud be search
	# qs = BlogPost.objects.filter(title__icontains='title')      
	qs = BlogPost.objects.all()
	template_name = 'blog/list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
	# create objects
	# ? use a form
	form = BlogPostModelForm(request.POST or None)
	if form.is_valid():
		# obj = BlogPost.objects.create(**form.cleaned_data)
		obj = form.save(commit=False)
		# obj.title = form.cleaned_data.get("title") + "0"
		obj.save()
		form = BlogPostModelForm()
	template_name = 'form.html'
	context = {'form': form}
	return render(request, template_name, context)


def blog_post_detail_view(request, slug):
	# 1 object -> detail view
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog/detail.html'
	context = {"object": obj} 
	return render(request, template_name, context)
	
	

def blog_post_update_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog/update.html'
	context = {"object": obj, 'form': None} 
	return render(request, template_name, context)



def blog_post_delete_view(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog/delete.html'
	context = {"object": obj} 
	return render(request, template_name, context)