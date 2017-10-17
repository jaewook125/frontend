from django.shortcuts import render, get_object_or_404, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post, Comment

class PostListView(ListView):
	model = Post
	template_name = 'blog/index.html'
	paginate_by= 10

index = PostListView.as_view()


jquery = ListView.as_view(model=Post, template_name='blog/jquery.html')


post_new = CreateView.as_view(model=Post, fields='__all__')

post_detail = DetailView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')

class PostDeleteView(DeleteView):
	model=Post
	success_url = reverse_lazy('blog:index')	

post_delete = PostDeleteView.as_view()

class CommentCreateView(CreateView):
	model = Comment
	fields = ['message']
	# 필드는 메세지만 나타낸다

	def form_valid(self, form):
		commit = form.save(commit=False)
		# 현재 오브젝트를 하나 받는다
		commit.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
		# kwargs(키워드 아규먼츠는) url 인자부분이다
		return super().form_valid(form)

	def get_success_url(self):
		#get_success_url는 뷰 전용 absolute는 모델 전용
		return resolve_url(self.object.post)
		#클래스기반 뷰는 셀프.오브젝트에 있고 이것의 포스트로 이동
comment_new = CommentCreateView.as_view()

class CommentUpdateView(UpdateView):
	model = Comment
	fields = ['message']

	def get_success_url(self):
		#get_success_url는 뷰 전용 absolute는 모델 전용
		return resolve_url(self.object.post)
		#클래스기반 뷰는 셀프.오브젝트에 있고 이것의 포스트로 이동

comment_edit = CommentUpdateView.as_view()

class CommentDeleteView(DeleteView):
	model=Comment

	def get_success_url(self):
		#get_success_url는 뷰 전용 absolute는 모델 전용
		return resolve_url(self.object.post)
		#클래스기반 뷰는 셀프.오브젝트에 있고 이것의 포스트로 이동

comment_delete = CommentDeleteView.as_view()