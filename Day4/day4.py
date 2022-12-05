

def is_fully_contained(nums1, nums2):
    [min1, max1] = nums1
    [min2, max2] = nums2
    return (min2 >= min1) and (max2 <= max1)

def is_overlapping(nums1, nums2):
    [min1, max1] = nums1
    [min2, max2] = nums2
    return (min2 <= min1 <= max2) or (min2 <= max1 <= max2)


# DAY 4 - PART ONE

with open("input.txt") as my_file:
    lines = my_file.read().splitlines()
    total_contained = 0
    for line in lines:
        [split1, split2] = line.split(",")
        
        text1 = split1.split("-")
        num1 = [int(txt) for txt in text1]
        
        text2 = split2.split("-")
        num2 = [int(txt) for txt in text2]

        if (is_fully_contained(num1, num2) or (is_fully_contained(num2, num1))):
            total_contained += 1
    
    print(total_contained)


 # DAY 4  - PART TWO
with open("input.txt") as my_file:
    lines = my_file.read().splitlines()
    total_overlapping = 0
    for line in lines:
        [split1, split2] = line.split(",")
        
        text1 = split1.split("-")
        num1 = [int(txt) for txt in text1]
        
        text2 = split2.split("-")
        num2 = [int(txt) for txt in text2]

        if is_overlapping(num1, num2) or is_overlapping(num2,num1):
            total_overlapping += 1

    print(total_overlapping)