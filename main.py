import os, vk_api, random, time

def token_file():
	if os.path.exists('token_token.py'):
		from token_token import token
		global token
		pass
	else:
		print('Создайте файл token_token.py и создайте переменную token = "Тут Токен"\n')
		number = input('Создать файл автоматически(1) или Вы сами создадите файл(2)?')
		if str(number) == '1':
			token_file = open('token_token.py', 'w+')
			token_write = input('Ваш токен VK Admin\n')
			token_file.write('token = ' + '"' + str(token_write) + '"')
			print('Запустите скрипт заново!')
			input()
			exit()
			pass
		else:
			print('Нажмите Enter, чтобы выйти!')
			input()
			exit()
			pass
token_file()
try:
	#from token_token import token
	sessions = vk_api.VkApi(token = token)
	vksession = sessions.get_api()
except:
	exit()

def friendsDropOut2(user_id, like_min):
	friends = vksession.friends.get(user_id = user_id)
	user_number = 0
	While = True
	while While:
		try:
			posts = vksession.wall.get(owner_id = friends['items'][user_number], filter = 'owner')
			friend = friends['count']
			like = posts['items'][0]['likes']['count']
			user = posts['items'][0]['owner_id']
			usersget = vksession.users.get(user_ids = user)
			if int(like) <= int(like_min):
				try:
					userget = usersget[0]['first_name'] + ' ' + usersget[0]['last_name']
					vksession.friends.delete(user_id = user)
					print(f'Пользователь {userget}({user}) удален! Likes: {like}')
					user_number = int(user_number + 1)
					pass
				except:
					pass
				pass
			elif int(like) > int(like_min):
				try:
					print(f'ID: {user}\nFriends: {friendscount}')
					user_number = int(user_number + 1)
					#time.sleep(1)
					pass
				except:
					pass
				pass
		except:
			user_number = int(user_number + 1)
			pass

def friendsDropOut1(user_id, friends_min):
	friends = vksession.friends.get(user_id = user_id)
	user_number = 0
	While = True
	while While:
		try:
			posts = vksession.wall.get(owner_id = friends['items'][user_number], filter = 'owner')
			friend = friends['count']
			user = posts['items'][0]['owner_id']
			usersget = vksession.users.get(user_ids = user)
			friendscount = vksession.friends.get(user_id = user)
			friendscount = friendscount['count']
			if int(friendscount) <= int(friends_min):
				try:
					userget = usersget[0]['first_name'] + ' ' + usersget[0]['last_name']
					vksession.friends.delete(user_id = user)
					print(f'Пользователь {userget}({user}) удален! Friends: {friendscount}')
					user_number = int(user_number + 1)
					pass
				except:
					pass
				pass
			elif friendscount > 100:
				try:
					print(f'ID: {user}\nFriends: {friendscount}')
					user_number = int(user_number + 1)
					#time.sleep(1)
					pass
				except:
					pass
				pass
		except:
			user_number = int(user_number + 1)
			pass



#######################################################


def main():
	os.system("cls")
	banner = """
 ______________________
|[1] - Отсев по друзьям|
|[2] - Отсев по лайкам |
"""
	choice = input(banner + "\n/> ")

	if str(choice) == "1":
		friendsDropOut1(input('Айди вашей страницы: '), input('Минимальное количество друзей: '))
		pass
	elif str(choice) == "2":
		friendsDropOut2(input('Айди вашей страницы: '), input('Минимальное количество лайков: '))
		pass
	else:
		print("[-]> Неверное число")
		input()
		pass


main()