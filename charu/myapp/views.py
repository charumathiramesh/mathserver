from django.shortcuts import render
def trianglearea(request):
    context={}
    context['area'] = "0"
    context['h'] = "0"
    context['b'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        h = request.POST.get('height','0')
        b = request.POST.get('base','0')
        print('request=',request)
        print('Height=',h)
        print('Base=',b)
        area = (int(h) * int(b))/2
        context['area'] = area
        context['h'] = h
        context['b'] = b
        print('Area=',area)
    return render(request,'myapp/math.html',context)