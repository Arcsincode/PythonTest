import argparse


def test_for_sys(year, name, body):
    print('the year is', type(year))
    print('the name is', name)
    print('the body is', type(body))

def from_ter():
	print(1111)
	parser = argparse.ArgumentParser(description='Test for argparse')
	parser.add_argument('--name', '-n', help='name 属性，非必要参数')
	parser.add_argument('--year', '-y', help='year 属性，非必要参数，但是有默认值', default=2017)
	parser.add_argument('--body', '-b', help='body 属性，必要参数', required=True)
	args = parser.parse_args()
	return args
 
if __name__ == '__main__':
    args=from_ter()

    try:
        test_for_sys(args.year, args.name, args.body)
    except Exception as e:
        print(e)
