from unicodedata import name
from webbrowser import get
from django.shortcuts import render
from .models import Categoria, Post
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
   queryset = request.GET.get('buscar')
   posts = Post.objects.filter(estado = True)
   if queryset:
      posts = Post.objects.filter(
         Q(titulo__icontains = queryset) | 
         Q(descripcion__icontains = queryset)
      ).distinct()
   paginator = Paginator(posts,1)
   page = request.GET.get('page')
   posts = paginator.get_page(page)
   contexto = {
      'posts':posts
   }
   return render(request,'index.html', contexto)

def detallePost(request, slug):
   post = get_object_or_404(Post, slug = slug)
   contexto = {
      'detalle_post':post
   }
   return render(request, 'post.html', contexto)

def proclamacion(request):
   queryset = request.GET.get('buscar')
   posts = Post.objects.filter(
      estado =True, 
      categoria = Categoria.objects.get(nombre__iexact = 'proclamacion'))
   if queryset:
      posts = Post.objects.filter(
         Q(titulo__icontains = queryset) |
         Q(descripcion__icontains = queryset),
         estado = True,
         categoria = Categoria.objects.get(nombre__iexact = 'proclamacion'),
      ).distinct()
   paginator = Paginator(posts,1)
   page = request.GET.get('page')
   posts = paginator.get_page(page)
   contexto = {
      'posts':posts
   }
   return render(request,'proclamacion.html', contexto)

def enceñanza(request):
   queryset = request.GET.get('buscar')
   posts = Post.objects.filter(
      estado = True,
      categoria = Categoria.objects.get(nombre__iexact = 'enceñanza')
   )
   if queryset:
      posts = Post.objects.filter(
         Q(titulo__icontains = queryset) |
         Q(categoria__icontains = queryset),
         estado = True,
         categoria = Categoria.objects.get(nombre__iexact = 'enceñanza'),
      ).distinct()
   paginator = Paginator(posts,1)
   page = request.GET.get('page')
   posts = paginator.get_page(page)
   contexto = {
      'posts':posts
   }
   return render(request, 'enceñanza.html', contexto)

def servicio(request):
   queryset = request.GET.get('buscar')
   posts = Post.objects.filter(
      estado = True,
      categoria = Categoria.objects.get(nombre__iexact = 'servicio')
   )
   if queryset:
      posts = Post.objects.filter(
         Q(titulo__icontains = queryset) |
         Q(categoria__icontains = queryset),
         estado = True,
         categoria = Categoria.objects.get(nombre__iexact = 'servicio'),
      ).distinct()
   paginator = Paginator(posts,1)
   page = request.GET.get('page')
   posts = paginator.get_page(page)
   contexto = {
      'posts':posts
   }
   return render(request, 'servicio.html', contexto)

def comunion(request):
   queryset = request.GET.get('buscar')
   posts = Post.objects.filter(
      estado = True,
      categoria = Categoria.objects.get(nombre__iexact = 'comunion')
   )
   if queryset:
      posts = Post.objects.filter(
         Q(titulo__icontains = queryset) |
         Q(categoria__icontains = queryset),
         estado = True,
         categoria = Categoria.objects.get(nombre__iexact = 'comunion'),
      ).distinct()
   paginator = Paginator(posts,1)
   page = request.GET.get('page')
   posts = paginator.get_page(page)
   contexto = {
      'posts':posts
   }
   return render(request, 'comunion.html', contexto)

def alavanza(request):
   queryset = request.GET.get('buscar')
   posts = Post.objects.filter(
      estado = True,
      categoria = Categoria.objects.get(nombre__iexact = 'alavanza')
   )
   if queryset:
      posts = Post.objects.filter(
         Q(titulo__icontains = queryset) |
         Q(categoria__icontains = queryset),
         estado = True,
         categoria = Categoria.objects.get(nombre__iexact = 'alavanza'),
      ).distinct()
   paginator = Paginator(posts,1)
   page = request.GET.get('page')
   posts = paginator.get_page(page)
   contexto = {
      'posts':posts
   }
   return render(request, 'alavanza.html', contexto)

def recursos(request):
   queryset = request.GET.get('buscar')
   posts = Post.objects.filter(
      estado = True,
      categoria = Categoria.objects.get(nombre__iexact = 'recursos')
   )
   if queryset:
      posts = Post.objects.filter(
         Q(titulo__icontains = queryset) |
         Q(categoria__icontains = queryset),
         estado = True,
         categoria = Categoria.objects.get(nombre__iexact = 'recursos'),
      ).distinct()
   paginator = Paginator(posts,1)
   page = request.GET.get('page')
   posts = paginator.get_page(page)
   contexto = {
      'posts':posts
   }
   return render(request, 'recursos.html', contexto)
