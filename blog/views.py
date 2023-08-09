from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Category, Tag, Comment, ReComment
from .forms import CommentForm, ReCommentForm
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def likes(request, pk):
    like_b = get_object_or_404(Post, pk=pk)
    if request.user in like_b.like.all():
        like_b.like.remove(request.user)
        like_b.like_count -= 1
        like_b.save()
    else:
        like_b.like.add(request.user)
        like_b.like_count +=1
        like_b.save()
    return redirect('/blog/' + str(pk))




class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
        



class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title','content','file_upload','category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            
            response = super(PostCreate, self).form_valid(form)
            
            # 입력한 POST값을 받아 tags_str에 지정
            tags_str = self.request.POST.get('tags_str')
            if tags_str:
                # 입력한 str 공백제거
                tags_str = tags_str.strip()

                # , ; 둘 다 가능하게 함
                tags_str = tags_str.replace(',',';')
                # ;를 구분자로 처리하고 tags_list에 담기
                tags_list = tags_str.split(';')
                print(tags_list)

                for t in tags_list:
                    # 입력한 태그 리스트를 for문돌리고 공백제거
                    t = t.strip()
                    print(t)

                    # tag 공백일 때는 pass(for문 첫문장으로 이동, 다음 요소로 수행)
                    if t == "":
                        continue
                    # 있으면 가져오고 없으면 만드는 함수
                    tag, is_tag_created = Tag.objects.get_or_create(name=t)
                    print(f'tag , is_tag_created: {tag}, {is_tag_created}')
                    # 만약 없는 태그값을 받아왔다면 만든다

                    if is_tag_created:
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    self.object.tags.add(tag)

            return response
        else:
            return redirect('/blog/')
        

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','content','file_upload','category','tags']

    template_name = 'blog/post_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        if self.object.tags.exists():
            tags_str_list = list()
            for t in self.object.tags.all():
                tags_str_list.append(t.name)
            context['tags_str_default'] = ';'.join(tags_str_list)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
        
    def form_valid(self, form):
        response = super(PostUpdate, self).form_valid(form)
        self.object.tags.clear()

        tags_str = self.request.POST.get('tags_str')
        if tags_str:
            # 입력한 str 공백제거
            tags_str = tags_str.strip()

            # , ; 둘 다 가능하게 함
            tags_str = tags_str.replace(',',';')
            tags_list = tags_str.split(';')

            for t in tags_list:
                t = t.strip()

                if t == "":
                    continue
                # 있으면 가져오고 없으면 만드는 함수
                tag, is_tag_created = Tag.objects.get_or_create(name=t)
                # 만약 없는 태그값을 받아왔다면 만든다
                if is_tag_created:
                    tag.slug = slugify(t, allow_unicode=True)
                    tag.save()
                self.object.tags.add(tag)

        return response



class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        # context['comment_count'] = Comment.objects.filter().count()

        # 가장 많은 views 수를 가진 게시물 5개
        context['most_viewed_posts'] = Post.objects.order_by('-views')[:5]
        return context
    
def category_page(request, slug):

    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request, 'blog/post_list.html',
        {
            'post_list' : post_list,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category' : category,
        }
    )

class PostSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q) | Q(tags__name__contains=q)
        ).distinct()
        return post_list
    
    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'
        return context
    

class PostDetail(DetailView):
    model = Post


    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        context['most_viewed_posts'] = Post.objects.order_by('-views')[:5]
        return context
    
def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(request, 'blog/post_list.html', {
        'post_list' : post_list,
        'tag' : tag,
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count(),
    })
    
def new_comment(request, pk):
    # 로그인했는지 확인
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        # method가 POST일경우 CommentForm 값을 불러온다
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                post.comment_count += 1
                post.save()
                comment.save()
                # 작성버튼 누르면 페이지로 리다이렉트
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        # 로그인하지 않았다면 PermissionDenied 권한이 거부됨
        raise PermissionDenied

@login_required
def create_recomment(request, post_id, comment_pk):
    post = get_object_or_404(Post, pk=post_id)
    parent_comment = get_object_or_404(Comment, pk=comment_pk)
    c_count = parent_comment.post

    if request.method == 'POST':
        recomment_form = ReCommentForm(request.POST)
        if recomment_form.is_valid():
            recomment = recomment_form.save(commit=False)
            recomment.post = post
            recomment.parent_comment = parent_comment
            recomment.author = request.user
            recomment.save()

            c_count.comment_count += 1
            c_count.save()

            return redirect(post.get_absolute_url())

    else:
        recomment_form = ReCommentForm()

    return render(request, 'create_recomment.html', {'recomment_form': recomment_form})




def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    c_count = comment.post
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        c_count.comment_count -= 1
        c_count.save()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied
    

def delete_recomment(request, pk):
    comment = get_object_or_404(ReComment, pk=pk)
    c_count = comment.post
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        c_count.comment_count -= 1
        c_count.save()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied
    

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated and request.user == post.author:
        post.delete()
        return redirect('/blog/')
    else:
        raise PermissionDenied



    

def comment_likes(request, pk):
    like_c = get_object_or_404(Comment, pk=pk)
    re = like_c.post
    if request.user in like_c.like.all():
        like_c.like.remove(request.user)
        like_c.like_count -= 1
        like_c.save()
    else:
        like_c.like.add(request.user)
        like_c.like_count +=1
        like_c.save()
    # return redirect('/blog/' + str(pk))
    return redirect(re.get_absolute_url())


