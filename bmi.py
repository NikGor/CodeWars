# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    bmi = weight / (height ** 2)
    bmi_ranges = {
        (0, 18.5): "Underweight",
        (18.5, 25): "Normal",
        (25, 30): "Overweight",
        (30, float('inf')): "Obese"
    }

    for (low, high), label in bmi_ranges.items():
        if low < bmi <= high:
            return label
