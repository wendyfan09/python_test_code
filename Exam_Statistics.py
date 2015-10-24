grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade
print "All of the grades:", print_grades(grades)
def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
print "All of the grades:", grades_sum(grades)   
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average
print "Average grade:", grades_average(grades)
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
        result =variance /float(len(scores))
    return result
print "Variance:", grades_variance(grades)

def grades_std_deviation(variance):
    result = variance ** 0.5
    return result
variance = grades_variance(grades)
print "Standard deviation:", grades_std_deviation(variance)