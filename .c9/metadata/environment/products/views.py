{"filter":false,"title":"views.py","tooltip":"/products/views.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":1,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["","# Create your views here.",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":6,"column":67},"action":"insert","lines":["from .models import Product","","# Create your views here.","def all_products(request):","    products = Product.objects.all()","    return render(request, \"products.html\", {\"products\": products})"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":67},"end":{"row":6,"column":67},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567329459195,"hash":"ad7b7cf4f18a0660ba0c3cd7f121ee029f0ad58a"}