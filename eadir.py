import os

def scan_dir(path):
	dirs = os.listdir(path)

	if '@eaDir' in dirs:
		p = f'{path}@eaDir'.replace(' ', '\ ')
		os.system(f'rm -r {p}')
		print(f'{p}')

	for d in dirs:
		if os.path.isdir(f'{path}{d}'):
			scan_dir(f'{path}{d}/')

if __name__ == '__main__':
	scan_dir('./')
