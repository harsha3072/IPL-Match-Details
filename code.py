def write_result(name_comand, result, results_list):


	if len(results_list) > 0:
		for i in range(len(results_list)):
			if results_list[i][0] == name_comand:
				results_list[i][1] = [a + b for a, b in zip(results_list[i][1], result)]
				return results_list
	results_list.append([name_comand, result])
	return results_list


while True:
	try:
		games = int(input())
		if games < 0:
			print()
			continue
	except ValueError:
		print()
		continue
	matches_score = list()
	while games > 0:
		tmp = input().split(sep=';')
		if len(tmp) != 3 or tmp[2] not in ['loss', 'draw', 'win']:
			print('incorrect input. must be \"first team;second team;result\"')
		else:
			matches_score.append(tmp)
			games -= 1
	break
res = list()
w = [1, 1, 0, 0, 3]
l = [1, 0, 1, 0, 0]
d = [1, 0, 0, 1, 1]
for i in range(len(matches_score)):
	if matches_score[i][2] == 'win':
		res = write_result(matches_score[i][0], w, res)
		res = write_result(matches_score[i][1], l, res)
	elif matches_score[i][2] == 'loss':
		res = write_result(matches_score[i][0], l, res)
		res = write_result(matches_score[i][1], w, res)
	else:
		res = write_result(matches_score[i][0], d, res)
		res = write_result(matches_score[i][1], d, res)
res.sort(key=lambda i: i[1][4], reverse=True)
if len(res) == 0:
	print('No Output')
else:
	for el in res:
		print('Team: {}, Matches Played: {}, Won: {}, Lost: {}, Draw: {}, Points: {}'.format(el[0],*el[1]))
