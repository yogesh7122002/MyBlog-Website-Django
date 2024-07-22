# # from django.shortcuts import render
# # from .models import Tweet
# # from .forms import TweetForm
# # from django.shortcuts import get_object_or_404,redirect
# # # Create your views here.

# # def home(request):
# #     return render(request,"home.html")


# # def tweet_list(request):
# #     tweets = Tweet.objects.all().order_by('-created_at')
# #     return render(request,"tweet_list.html",{"tweets":tweets})

# # def tweet_create(request):
# #     if request.method == "POST":
# #         form = TweetForm(request.POST,request.FILE)
# #         if form.is_valid():
# #             tweet = form.save(commit=False)
# #             tweet.user = request.user
# #             tweet.save()
# #             return redirect('tweet_list')   
# #     else: 
# #         form= TweetForm()
# #     return render(request,"tweet_form.html",{"form":form})


# # def tweet_edit(request,tweet_id):
# #     tweet = get_object_or_404(Tweet,pk=tweet_id,user = request.user)
# #     if  request.method=="POST":
# #          form =TweetForm(request.POST,request.FILES,instance=tweet)
# #          if form.isvalid():
# #             tweet = form.save(commit=False)
# #             tweet.user= request.user
# #             tweet.save()
# #             return redirect('tweet_list')
# #     else:
# #         form= TweetForm()
# #     return render(request,"tweet_form.html",{"form":form})


# # def tweet_delete(request,tweet_id):
# #     tweet = get_object_or_404(Tweet,pk=tweet_id,user =request.user)
# #     if request.method=="POST":
# #         tweet.delete()
# #         return redirect('tweet_list')
# #     return render(request,'tweet_conform.html',{'tweet':tweet})


# from django.shortcuts import render
# from .models import Tweet
# from .forms import TweetForm
# from django.shortcuts import get_object_or_404, redirect

# # Create your views here.

# def home(request):
#     return render(request, "home.html")

# def tweet_list(request):
#     tweets = Tweet.objects.all().order_by('-created_time')
#     return render(request, "tweet_list.html", {"tweets": tweets})

# def tweet_create(request):
#     if request.method == "POST":
#         form = TweetForm(request.POST, request.FILES)  # Fix typo: request.FILE to request.FILES
#         if form.is_valid():
#             tweet = form.save(commit=False)
#             tweet.user = request.user
#             tweet.save()
#             return redirect('tweet_list')
#     else:
#         form = TweetForm()
#     return render(request, "tweet_form.html", {"form": form})

# def tweet_edit(request, tweet_id):
#     tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
#     if request.method == "POST":
#         form = TweetForm(request.POST, request.FILES, instance=tweet)
#         if form.is_valid():  # Fix typo: isvalid() to is_valid()
#             tweet = form.save(commit=False)
#             tweet.user = request.user
#             tweet.save()
#             return redirect('tweet_list')
#     else:
#         form = TweetForm(instance=tweet)  # Pass instance to the form
#     return render(request, "tweet_form.html", {"form": form})

# def tweet_delete(request, tweet_id):
#     tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
#     if request.method == "POST":
#         tweet.delete()
#         return redirect('tweet_list')
#     return render(request, 'tweet_confirm.html', {'tweet': tweet})  # Fix typo: conform.html to confirm.html



from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm,userRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login




def home(request):
    return render(request, "home.html")

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_time')
    return render(request, "tweet_list.html", {"tweets": tweets})
@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, "tweet_form.html", {"form": form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweet_form.html", {"form": form})
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm.html', {'tweet': tweet})

def register(request):
    if request.method=="POST":
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect("tweet_list")
    else:
        form = userRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# def tweet_search(request):
#     query  = request.get('query')
#     tweets = Tweet.objects.filter(text__icontains=query) if query else Tweet.objects.all()
#     tweets = Tweet.objects.filter(text__icontains=query) if query else Tweet.objects.all()
#     return render(request,"search_results.html",{"tweets":tweets,'query':query})

    
def tweet_search(request):
    query = request.GET.get('query', '')  # Fetch the search query
    tweets = Tweet.objects.filter(text__icontains=query) if query else Tweet.objects.all()  # Filter tweets based on query
    return render(request, 'search_result.html', {'tweets': tweets, 'query': query})
