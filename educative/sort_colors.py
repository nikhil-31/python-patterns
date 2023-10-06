

def sort_colors(nums):

    red = 0
    white = 0
    blue = len(nums) - 1

    while white <= blue:
        if nums[white] == 0:
            if nums[red] != 0:
                nums[red], nums[white] = nums[white], nums[red]
        
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            if nums[blue] != 2:
                nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
    return nums

print(sort_colors([2,1,0,0,1,2,0]))
