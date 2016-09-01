#-------------------------------------------------------------------------------
# Name:        module2
# Purpose: Computes the percent needed on a final exam to achieve a certain grade
#
# Author:      Andrea
#
# Created:     3/12/2015
# Copyright:   (c) Andrea 2015
#------------------------------------------------------------------------------
def average_in_category(nested_list):
    average_list = []
    for row in nested_list:
        sum_of_row = 0
        for n in row:
            sum_of_row += n
        row_average = float(sum_of_row) / len(row)
        average_list.append(row_average)
    return average_list


def weighted_average_list(weights, nested_list):
    """weights is a list of weights for each category
    a nested list contains a list of scores separated by categories """
    a_list = average_in_category(nested_list)
    new_list = []
    for i in range(len(a_list)):
        a = weights[i] * a_list[i]
        new_list.append(a)
    return new_list

def make_weighted_average(list_of_floats):
    """ The input of this function is a list of weighted averages"""
    final_sum = 0
    for i in list_of_floats:
        final_sum += i
    return final_sum

def can_i_pass(amount_earned, final_weight):
    """ amount earned is grade earned if final is not taken
    it is a number between 0 and 1
    final weight is a number representing how a final is weighted in the final grade"""
    percents = []
    for x in range(101):
        percents.append(x / 100.0)
    grade_contributions = []
    for score in percents:
        grade_contributions.append(score * final_weight)
    possible_grades = []
    for g in grade_contributions:
        possible_grades.append(g+ amount_earned)
    if (amount_earned >= 1 or final_weight >= 1):
        print "All inputs are less than 1"
    elif amount_earned <= 0 or final_weight <= 0:
        print "No negative grades, stupid"
    else:
        a_display = False
        a_minus_display = False
        b_plus_display = False
        b_display = False
        b_minus_display = False
        c_plus_display = False
        c_display = False
        c_minus_display = False
        d_plus_display = False
        d_display = False
        d_minus_display = False
        f_display = False
        for grade in possible_grades:
            int_percent = int(grade * 100)
            score = int(float(grade - amount_earned)/0.004)
            if int_percent >= 94 and not a_display:
                print "You will get an A, if you get above %d%%" % score
                a_display = True
            elif int_percent >= 90 and not a_minus_display:
                print "You will get an A-, if you get above %d%%" % score
                a_minus_display = True
            elif int_percent >= 87 and not b_plus_display:
                print "You will get an B+, if you  get above %d%%" % score
                b_plus_display = True
            elif int_percent >= 83 and (not b_display):
                print "You will get an B, if you get above %d%%" % score
                b_display = True
            elif int_percent >= 80 and not b_minus_display:
                print "You will get an B-, if you get above %d%%" % score
                b_minus_display = True
            elif int_percent >= 77 and not c_plus_display:
                print "You will get an C+, if you get above %d%%" % score
                c_plus_display = True
            elif int_percent >= 73 and not c_display:
                print "You will get an C, if you get above %d%%" % score
                c_display = True
            elif int_percent >= 70 and not c_minus_display:
                print "You will get an C-, if you get above %d%%" % score
                c_minus_display = True
            elif int_percent >= 67 and not d_plus_display and score != 0:
                print "You will get an D+, if you get above %d%%" % score
                d_plus_display = True
            elif int_percent >= 63 and not d_display and score != 0:
                print "You will get an D, if you get above %d%%" % score
                d_display = True
            elif int_percent >= 60 and not d_minus_display and score != 0:
                print "You will get an D-, if you get above %d%%" % score
                d_minus_display = True
            elif int_percent == 59 and not f_display and score != 0:
                print "You FAIL!, if you get below a %d%%" % score
                f_display = True


def main():
  





if __name__ == '__main__':
    main()
