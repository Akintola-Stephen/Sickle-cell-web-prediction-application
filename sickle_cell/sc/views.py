from django.shortcuts import render

# Create your views here.


def index(request, template_name="landing-page/index.html"):
    return render(request, template_name)


# I'll bring in my ML model to this functions so as to automate predictions
def question_prediction(request, template_name="diagnosis-questions/questions.html"):
    return render(request, template_name)


def acute_result(request, template_name="result/result_acute.html"):
    return render(request, template_name)
