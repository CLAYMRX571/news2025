from .models import Category, Tag, Article

def get_main_context(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    latest_news = Article.objects.filter()[:4]

    context = {
        "tags": tags,
        "categories": categories,
        "latest_news": latest_news,
    }
    return context 