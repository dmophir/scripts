import json

if __name__ == '__main__':
	subs = open('subs.txt', 'r')
	res = json.load(open('res.json'))

	# print(res['data']['RESoptions.filteReddit']['subreddits']['value'])

	res['data']['RESoptions.filteReddit']['subreddits']['value']
	for sub in subs:
		entry = [sub.strip(('\n'))]
		res['data']['RESoptions.filteReddit']['subreddits']['value'].append(entry)

	print(res['data']['RESoptions.filteReddit']['subreddits']['value'])

	outfile = open('res.resbackup', 'w')

	json.dump(res, outfile, indent=4)

	subs.close()
	outfile.close()