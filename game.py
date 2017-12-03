import random 

MAX_ERRORS=8

words = ["автомобиль", "авария", "колесо", "синхрофазатрон", "россия", "учитель", "учебник", "металлургия", "кровать", "одеяло"]

answer = "Y"

while answer == "Y":
	print("Добро пожаловать в игру Угадайка")
	print("Правила очень просты:")
	print("Система автоматически загадывает слово")
	print("Ваша задача это слово угадать вписывая буквы")
	print("Но будьте осторожны, у вас есть всего лишь 8 прав на ошибку")
	print("Удачи!")
	print("А вот и загаданное слово:")

	hidden_words = random.sample(words, 1)[0]

	user_word = ["*"] * len(hidden_words)
	print("".join(user_word))

	mistakes_counter = 0
	used_letter = []

	while True:
		letter = input("Введите букву: ")
		
		if len(letter) == 1 and letter.isalpha() and letter not in used_letter:
			used_letter.append(letter)
			if letter in hidden_words:
				for pos, _letter in enumerate(hidden_words):
					if _letter == letter:
						user_word[pos] = letter
				print("".join(user_word))
				if "*" not in user_word:
					print("Поздравляем! Вы выиграли!")
					answer = input("Хотите ли сыграть заново?(Y/N) ")
					if answer != "Y" or "y":
						break
			else:
				mistakes_counter += 1
				if mistakes_counter >= MAX_ERRORS:
					print("Вы проиграли")
					answer = input("Хотите ли сыграть заново?(Y/N) ")
					if answer != "Y" or "y":
						break
				print(f"Буквы {letter} нету!")
				print(f"Ваши ошибки: {mistakes_counter}")
		else:
			print("Вы ввели что-то не то")
			print("Возможно вам стоит поменять раскладку на клавиатуре или такая буква уже была вами использована")
			print(f"Использованные буквы {used_letter}")
