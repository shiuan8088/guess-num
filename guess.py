import random
start = input('請輸入最小數字: ')
end = input('請輸入最大數字: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('恭喜!你猜對囉!')
		print('你猜第', count, '次答對囉~')
		break
	elif num <r:
		print('比答案小')
	elif num >r:
		print('比答案大')
	print('你已經猜', count, '次囉~')