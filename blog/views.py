from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment, Question, Exam, ExamTemplate, Option
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm, QuestionForm, ExamForm, ExamTemplateForm, OptionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
           # post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)

@permission_required('blog.question_detail',raise_exception=True)
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    num_options = question.exam.template.questions
    num_options_done = Option.objects.filter(question=pk).count()
    if num_options_done > 0:
        options = Option.objects.filter(question=pk)
    num_options_todo = num_options - num_options_done
    todo = []
    done = []

    for i in range(num_options_done):
        done.append(chr(ord('a')+i))
    
    for i in range(num_options_todo):
        todo.append(chr(ord('a')+i+num_options_done))

    return render(request, 'blog/question_detail.html', {'question': question, 'todo': todo,
     'options': options, 'done':done})

@permission_required('blog.question_list',raise_exception=True)
def question_list(request, pk):
    questions = Question.objects.filter(exam=pk)
    return render(request, 'blog/question_list.html', {'questions': questions})

@permission_required('blog.add_question',raise_exception=True)
def question_new(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_form = form.save()
            return HttpResponseRedirect(reverse(question_detail, args=(new_form.pk,)))
    else:
        form = QuestionForm()
    return render(request, 'blog/question_edit.html', {'form': form})

@permission_required('blog.add_question',raise_exception=True)
def option_new(request, pk):
    if request.method == "POST":
        form = OptionForm(request.POST)
        if form.is_valid():
            option = form.save(commit=False)
            option.question = get_object_or_404(Question, pk=pk)
            option.save()
            return HttpResponseRedirect(reverse(question_detail, args=(pk,)))
    else:
        form = OptionForm()
    return render(request, 'blog/option_edit.html', {'form': form})

@permission_required('blog.add_exam',raise_exception=True)
def exam_new(request):
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():

            exam = form.save(commit=False)
            exam.author = request.user
           # post.published_date = timezone.now()
            exam.save()
            return redirect('blog.views.exam_new')
    else:
        form = ExamForm()
    return render(request, 'blog/exam_edit.html', {'form': form})

@permission_required('blog.exam_detail',raise_exception=True)
def exam_detail(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    return render(request, 'blog/question_list.html', {'exam': exam})

@permission_required('blog.exam_list')
def exam_list(request):
    exams = Exam.objects.filter(author=request.user)
    return render(request, 'blog/exam_list.html', {'exams': exams})    

@permission_required('blog.add_examtemplate',raise_exception=True)
def exam_template_new(request):
    if request.method == "POST":
        form = ExamTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog.views.exam_template_new')
    else:
        form = ExamTemplateForm()
    return render(request, 'blog/exam_template_edit.html', {'form': form})

@permission_required('blog.exam_template_detail',raise_exception=True)
def exam_template_detail(request, pk):
    exam_template = get_object_or_404(ExamTemplate, pk=pk)
    return render(request, 'blog/exam_template_detail.html', {'exam_template': exam_template})

@login_required
def notfinisehd_exams(request):
    return render(request, 'blog/not_finished_exams.html')

@login_required
def finisehd_exams (request):    
    return render(request, 'blog/finished_exams.html')


