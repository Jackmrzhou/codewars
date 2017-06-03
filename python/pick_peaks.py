'''
In this kata, you will write a func that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak in position 3 with a value of 5 (arr[3] equals 5).

The output will be returned as a struct (PosPeaks) with two properties: Pos and Peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be {Pos: [], Peaks: []}.

Example: PickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) returns {Pos: [3, 7], Peaks: [6, 3]}

All input arrays will be valid numeric arrays (although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus! [1, 2 , 2 , 2 , 1] has a peak while [1, 2, 2, 2, 3] does not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: PickPeaks([1, 2, 2, 2, 1]) returns {Pos: [1], Peaks: [2]}
'''
def pick_peaks(arr):
	peaks=[]
	pos=[]
	if not arr:
		return {"pos":pos, "peaks":peaks}
	peak = 0
	lenth = len(arr)
	is_up = False
	is_plateau =False
	posible_pos=0
	for _pos,height in enumerate(arr):
		if _pos == lenth -1:
			break
		elif height < arr[_pos+1]:
			if is_up == False:
				is_up = True
			if is_plateau == True:
				is_plateau = False
		elif height > arr[_pos+1] and is_up:
			peaks.append(height)
			if is_plateau == False:
				pos.append(_pos)
			else:
				pos.append(posible_pos)
			is_plateau = False
			is_up = False
		elif height == arr[_pos+1] and height != arr[_pos-1]:
			is_plateau = True
			posible_pos = _pos
	return {"pos":pos, "peaks":peaks}

#other people's solution
def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}

