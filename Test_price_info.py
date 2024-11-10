import price_info
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }
quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}

def test_total_cost_shopping():
        
        test=price_info.total_cost_shopping()
        result=46.75
        assert(test==result)

def test_cost_of_fruit():
        test=price_info.cost_of_fruits('orange',10)
        result=14
        assert(test==result)
