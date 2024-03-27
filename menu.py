import rules

def main():
	while True:

		ch = input('\n1.Ввести значения\n2.Выход\n')
		if ch == '2':
			return
		if ch == '1':
			s = input("\nСкорость км\ч : ")
			d = input("Расстояние м. : ")
			rules.controller.input['speed'] = int(s)
			rules.controller.input['distance'] = int(d)

			rules.controller.compute()
			print("\nУправляющее воздействие:", rules.controller.output['action'])
			action_number = rules.controller.output['action']

			if(action_number <36):
				print("\nСистема рекомендует - " + rules.print_actions[0])
			elif (action_number < 42):
				print("Система рекомендует - " + rules.print_actions[1])
			elif (action_number < 50):
				print("Система рекомендует - " + rules.print_actions[2])
			elif (action_number < 70):
				print("Система рекомендует - " + rules.print_actions[3])
			else:
				print("Система рекомендует - " + rules.print_actions[4])
			rules.action.view(sim=rules.controller)

if __name__ == "__main__":
	main()