def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
#Add code here to calculate BMI
    bmi = weight/(height*height)
#Add code here to display calculate BMI
    print(f"BMI = {bmi}")
    if bmi < 18.5:
        print("Under Weight")
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Over Weight")


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    
          


def calc_average(num_list):
    avg = sum(num_list)/len(num_list)
    print(f"Average: {avg}")

    return avg
          
def get_user_input():
    userInput = input().split(",")
   
    return userInput

def find_min_max(num_list):

    min_max = [min(num_list), max(num_list)]
    return min_max

def sort_temperature(num_list):
    sortedList = sorted(num_list)

    return sortedList

def calc_median_temperature(num_list):

    if (len(num_list) % 2 == 0):

        median = (num_list[len(num_list)//2] + num_list[len(num_list)//2 -1])/2 
        return median
    
    elif (len(num_list) % 2 != 0):
        median = (num_list[len(num_list)//2 ] )
        return median


def main():
    
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    calculate_bmi(weight=57, height=1.73)
    display_main_menu()
    num_list = get_user_input()
    for i in range(len(num_list)):
        num_list[i] = float(num_list[i])
    calc_average(num_list)
    min_max = find_min_max(num_list)
    print(f"Min number: {int(min_max[0])}")
    print(f"Max number: 3,{int(min_max[1])}")
    sortedList = sort_temperature(num_list)
    print(f"Sorted List: {sortedList}")
    median = calc_median_temperature(sortedList)
    
    print(f"Median: {median}")


if __name__ == "__main__":
    main()