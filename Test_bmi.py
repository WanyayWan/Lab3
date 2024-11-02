import Lab2.bmi as bmi
def test_bmi_overweight() : 
    assert bmi.calculate_bmi(173, 85) == 1
    
def test_bmi_normal_weight() :
    assert bmi.calculate_bmi(173, 70) == 0

def test_bmi_underweight() :
    assert bmi.calculate_bmi(173, 50) == -1