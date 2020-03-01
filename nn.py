################################################################################################
# Remy
# This file is HEAVILY based on https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html
################################################################################################

import numpy as np
import torch
from torch import nn, optim, utils
from time import gmtime, strftime
from math import sqrt
from enumerator import num_ingredients, num_actions
from recipe_steps import write_steps
from 


# num_ingredients = total types of ingredients
# num_actions = total number of actions
INGREDIENTS = 10
STEPS = 10
NUM_FEATURES = INGREDIENTS * (86) + STEPS * (num_actions + 2 + num_ingredients)
NUM_INPUTS = 10


class Discriminator(nn.Module):
	def __init__(self):
		super(Discriminator, self).__init__()

		self.main = nn.Sequential(
			nn.Linear(NUM_FEATURES, NUM_FEATURES // 2),
			nn.LeakyReLU(),
			nn.Linear(NUM_FEATURES // 2, NUM_FEATURES // 4),
			nn.LeakyReLU(),
			nn.Linear(NUM_FEATURES // 4, NUM_FEATURES // 8),
			nn.LeakyReLU(),
			nn.Linear(NUM_FEATURES // 8, 1),
			nn.Sigmoid()
		)

	def forward(self, input):
		return self.main(input)


class Generator(nn.Module):
	def __init__(self):
		super(Generator, self).__init__()

		self.main = nn.Sequential(
			nn.Linear(NUM_INPUTS, NUM_FEATURES // 8),
			nn.LeakyReLU(),
			nn.Linear(NUM_FEATURES // 8, NUM_FEATURES // 4),
			nn.LeakyReLU(),
			nn.Linear(NUM_FEATURES // 4, NUM_FEATURES // 2),
			nn.LeakyReLU(),
			nn.Linear(NUM_FEATURES // 2, NUM_FEATURES),
			nn.LeakyReLU()
		)

	def forward(self, input):
		return self.main(input)


def fit(lr, epochs, stats_interval, recipe_inteval, train_file, batch_size):

	if torch.cuda.is_available():
		device = torch.device("cuda")
	else:
		device = torch.device("cpu")

	discriminator = Discriminator().to(device)
	generator = Generator().to(device)

	criterion = nn.BCELoss()
	fixed_noise = torch.randn(10, device=device)

	real_label = 1
	fake_label = 0

	optimizerD = optim.Adam(discriminator.parameters(), lr=lr, weight_decay=0)
	optimizerG = optim.Adam(generator.parameters(), lr=lr, weight_decay=0)

	d_losses = []
	g_losses = []
	recipe_list = []
	iters = 0

	train_set = torch.zeros(10000, 4440)
	with open(train_file, "r") as file:
		i = 0
		for line in file.readlines():
			values = line.split(",")
			for j in range(4440):
				train_set[i, j] = float(values[j])
			i += 1 

	#print(train_set)

	print("Starting Training")
	for epoch in range(epochs):

		train_loader = utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True)
		#print(train_loader)

		for num, data in enumerate(train_loader, 0):
			#print(data)

			### Update discriminator

			# Train with real batch
			discriminator.zero_grad()
			#real_dev = data[0].to(device)
			#batch_size = real_dev.size(0)

			# These will both have a length of batch_size
			label = torch.full((batch_size,), real_label, device=device)
			output = discriminator(data).view(-1)

			error_d_real = criterion(output, label)
			error_d_real.backward()
			D_x = output.mean().item()

			# Train with fake batch
			noise = torch.randn(batch_size, 10)
			fake_out = generator(noise)
			
			label.fill_(fake_label)
			output = discriminator(fake_out.detach()).view(-1)  # This part is pretty key

			error_d_fake = criterion(output, label)
			error_d_fake.backward()
			D_G_z1 = output.mean().item()

			error_d = error_d_real + error_d_fake

			optimizerD.step()

			### Update generator

			generator.zero_grad()
			label.fill_(real_label)

			output = discriminator(fake_out).view(-1)

			error_g = criterion(output, label)
			error_g.backward()
			D_G_z2 = output.mean().item()

			optimizerG.step()

			### Training statistics

			if num % stats_interval == 0:
				print("%s[%d/%d][%d/%d]\tLoss_D: %.4f\tLoss_G: %.4f\tD(x): %.4f\tD(G(z)): %.4f / %.4f" % (strftime("%H:%M:%S", gmtime()), epoch, epochs, num, len(data), error_d.item(), error_g.item(), D_x, D_G_z1, D_G_z2))

			# Save losses for later
			d_losses.append(error_d.item())
			g_losses.append(error_g.item())


			if iters % recipe_inteval == 0:
				with torch.no_grad():
					fake = generator(fixed_noise).detach().cpu()
				fake_floats = fake.tolist()
				print(write_steps(fake_floats[:86]))
				print(write_steps(fake_floats[86:]))
				recipe_list.append(fake)

			iters += 1


def main():
	fit(0.001, 20, 20, 100, "ex.txt", 50)


if __name__ == "__main__":
	main()
