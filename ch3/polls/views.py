from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Question
from polls.form import NameForm

# Create your views here.
def index(request): # 모델에서 가져옴
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context={'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)#pk=question_id 는 검색조건
    return render(request,'polls/detail.html',{'question':question})#템플릿에 넘겨주는 최종 파일
def vote(request,question_id):
    p=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=p.choice_set.get(pk=request.POST['choice'])#request.POST는 제출된 폼을 담고있음,choice.id 리턴
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{ #question 과 error를 detail.html로전달, 질문항목 다시 볼 수 있음
            'question':p,
            'error_message':"You didn't select a choice.",
        })
    else: # 예외 처리를 하지 않고 무조건 실행
        selected_choice.votes +=1
        selected_choice.save() #해당 Choice 테이블에 저장
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,))) #reverse 가 타겟 url 만들어줌 ex) /polls/3/results
        #result() 함수 뷰에서 호출

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/results.html',{'question':question})

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request,'name.html',{'form':form})