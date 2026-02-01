from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from dgnago.shortcuts import get_object_or_404
from djnago.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, "tweets/index.html")

def tweet_list(request, tweet_id):
    tweets = Tweet.objects.all().order_by("-created_at")
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, "tweets/tweet_list.html", {"tweets": tweets, "tweet": tweet})

def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list", tweet_id=tweet.id)
    else:
        form = TweetForm()
    return render(request, "tweets/tweet_create.html", {"form": form})
    
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id ,user = request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list", tweet_id=tweet.id)
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweets/tweet_edit.html", {"form": form, "tweet": tweet})

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "tweets/tweet_delete.html", {"tweet": tweet})