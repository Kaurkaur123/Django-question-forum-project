
from .forms import  NewResponseForm, NewReplyForm, NewQuestionForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Response#, Choice


def questionPage(request, id):
    response_form = NewResponseForm()
    reply_form = NewReplyForm()

    if request.method == 'POST':
        try:
            response_form = NewResponseForm(request.POST)
            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.user = request.user
                response.question = Question(id=id)
                response.save()
                return redirect('/question/'+str(id)+'#'+str(response.id))
        except Exception as e:
            print(e)
            raise

    #choices = Choice.objects.get(question=id)
    question = Question.objects.get(id=id)
    #if question.body == 'Choice':
        #if request.method == 'POST':
            #try:


    context = {
        'question': question,
        'response_form': response_form,
        'reply_form': reply_form,
        #'choices': choices,
    }
    return render(request, 'question.html', context)


#@login_required(login_url='register')
def replyPage(request):
    if request.method == 'POST':
        try:
            form = NewReplyForm(request.POST)
            if form.is_valid():
                question_id = request.POST.get('question')
                parent_id = request.POST.get('parent')
                reply = form.save(commit=False)
                reply.user = request.user
                reply.question = Question(id=question_id)
                reply.parent = Response(id=parent_id)
                reply.save()
                return redirect('/question/'+str(question_id)+'#'+str(reply.id))
        except Exception as e:
            print(e)
            raise

    return redirect('index')


@login_required(login_url='register')
def newQuestionPage(request):
    form = NewQuestionForm()

    if request.method == 'POST':
        try:
            form = NewQuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user
                question.save()
        except Exception as e:
            print(e)
            raise

    context = {'form': form}
    return render(request, 'makequestion.html', context)
#def post_detail(request, slug):
 #   template_name = 'post_detail.html'
  #  post = get_object_or_404(Question, slug=slug)
   # comments = post.comments.filter(active=True)
    #new_comment = None
    ## Comment posted
    #if request.method == 'POST':
     #   comment_form = CommentForm(data=request.POST)
      #  if comment_form.is_valid():
#
            # Create Comment object but don't save to database yet
 #           new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
  #          new_comment.post = post
            # Save the comment to the database
   #         new_comment.save()
    #else:
     #   comment_form = CommentForm()

    #return render(request, template_name, {'post': post,
     #                                      'comments': comments,
      #                                     'new_comment': new_comment,
       #                                    'comment_form': comment_form})


