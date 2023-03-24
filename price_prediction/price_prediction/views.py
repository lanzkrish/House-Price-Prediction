from django.shortcuts import render
from django.conf import settings
import numpy as np

def PredictorPage(request):
    return render(request,"BHP.html")

def PredictPrice(request):
    if request.method == "POST":
        location = request.POST.get("location")
        area_type  = request.POST.get("area_type")
        total_sqft = request.POST.get("total_sqft")
        bathroom = request.POST.get("bathrooms")
        bhk = request.POST.get("size")
        balcony = request.POST.get("balcony")
        a = ['Built-up  Area', 'Carpet  Area', 'Plot  Area',
       'Super built-up  Area']
        l = ['7th Phase JP Nagar', 'Banashankari', 'Bannerghatta Road',
       'Begur Road', 'Bellandur', 'Chandapura', 'Electronic City',
       'Electronic City Phase II', 'Electronics City Phase 1',
       'Haralur Road', 'Harlur', 'Hebbal', 'Hennur Road', 'Hoodi',
       'Hormavu', 'KR Puram', 'Kanakpura Road', 'Kasavanhalli', 'Kengeri',
       'Marathahalli', 'Raja Rajeshwari Nagar', 'Rajaji Nagar',
       'Ramamurthy Nagar', 'Sarjapur', 'Sarjapur  Road', 'Thanisandra',
       'Uttarahalli', 'Whitefield', 'Yelahanka', 'Yeshwanthpur']
        
        Parr = [a.index(area_type),l.index(location),bhk,total_sqft,bathroom,balcony]
        Parr1 = []
        for i in Parr:
            Parr1.append(int(i))
        Parr1 = np.array(Parr1).reshape(1,-1)

        
        model = settings.MODEL
        price = model.predict(Parr1)[0]
        price = round(price)
        if price<100:
            price=f"{price} Lakhs"
        else:
            price = price/100
            price = f"{price} Crore"
        return render(request,"BHP.html",{'price':price})




