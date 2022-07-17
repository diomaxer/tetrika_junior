def append_interval(intervals, name):
	mini_array = []

	for i in range(len(intervals[name])):
		if i % 2 == 0:
			mini_array.append((intervals[name][i], name[0], 'join'))
		else:
			mini_array.append((intervals[name][i], name[0], 'out'))

	return mini_array

def appearance(intervals):
	array = []
	array += append_interval(intervals, 'lesson')
	array += append_interval(intervals, 'pupil')
	array += append_interval(intervals, 'tutor')

	array.sort(key=lambda x : x[0])

	tracker = {
		'l': 0,
		'p': 0,
		't': 0
	}

	start = ans = 0

	for elem in array:

		if elem[2] == 'join':
			tracker[elem[1]] += 1
		elif elem[2] == 'out':
			tracker[elem[1]] -= 1

		# print(tracker)


		if not 0 in (tracker.values()):
			start = elem[0]

		if 0 in (tracker.values()) and start != 0:
			# print(elem[0], '-', start)
			ans += elem[0] - start
			start = 0

	return ans




tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705147, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]



if __name__ == '__main__':
    for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
