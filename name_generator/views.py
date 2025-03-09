# name_generator/views.py
from django.shortcuts import render
from .forms import BabyNameForm
from .services.ai_service import generate_baby_names

def home_view(request):
    if request.method == "POST":
        form = BabyNameForm(request.POST)
        if form.is_valid():
            # Extract and format data
            siblings = form.cleaned_data["siblings"]
            if isinstance(siblings, list):
                siblings = ', '.join(siblings)

            # Generate names
            ai_result = generate_baby_names(
                form.cleaned_data["father_name"],
                form.cleaned_data["mother_name"],
                siblings,
                form.cleaned_data["country"],
                form.cleaned_data["language"],
                form.cleaned_data["name_style"],
                form.cleaned_data["religion"],
                form.cleaned_data["gender"]
            )

            # Prepare context for the result page
            context = {
                "father_name": form.cleaned_data["father_name"],
                "mother_name": form.cleaned_data["mother_name"],
                "siblings": siblings,
                "country": form.cleaned_data["country"],
                "language": form.cleaned_data["language"],
                "name_style": form.cleaned_data["name_style"],
                "religion": form.cleaned_data["religion"],
                "gender": form.cleaned_data["gender"],
            }

            if isinstance(ai_result, dict):
                context["ai_names"] = ai_result
            else:
                context["error"] = ai_result

            return render(request, "result.html", context)
    else:
        form = BabyNameForm()
    return render(request, "home.html", {"form": form})