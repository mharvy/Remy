import torch


def generate_recipe(generator, inputs):
	gen = torch.load(generator)
	with torch.no_grad():
	       return gen(inputs).tolist()


def main():
	for i in range(10):
		source = torch.randn(10)
		t = generate_recipe("remy.pt", source).detach().cpu()
		m = []
		s = []
		for i in range(10):
			idx = 0
			m.append(0)
			while idx < 10:
				f = t[i * 86 + idx]
				if f > t[m[-1]]:
					m[-1] = i * 86 + idx
				idx +=1
				m.append(0)
			while idx < 85 and idx >= 10:
				f = t[i * 86 + idx]
				if f > t[m[-1]]:
					m[-1] = i * 86 + idx
				idx += 1
			s.append(86 * i - 1)
			for i in range(10):
				idx = 0
				m.append(0)
				while idx < num_actions:
					f = t[10 * 86 + i * (num_actions + 2 + num_ingredients) + idx]
					if f > t[m[-1]]:
						m[-1] = 10 * 86 + i * (num_actions + 2 + num_ingredients) + idx
					idx += 1
				s.append(86 * 10 + (num_actions + 2 + num_ingredients) * i + num_actions)
				s.append(86 * 10 + (num_actions + 2 + num_ingredients) * i + num_actions + 1)
				m.append(0)
				while idx < (num_actions + 2 + num_ingredients) and idx > (num_actions + 2):
					f = t[10 * 86 + i * (num_actions + 2 + num_ingredients) + idx]
					if f > t[m[-1]]:
						m[-1] = 10 * 86 + i * (num_actions + 2 + num_ingredients) + idx
					idx += 1

		for i in range(len(t)):
			if i not in m and i not in s:
				t[i] = float(0)
			elif i in m:
				t[i] = float(1)

		for f in write_ingredients(t[:860])[0]:
			print(f)
		for f in write_steps(t[860:]):
			print(f)
		print("\n")


if __name__ == "__main__":
	main()
		
