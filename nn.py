################################################################################################
# Remy
# This file is HEAVILY based on https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html
################################################################################################

import numpy as np
import torch
from torch import nn, optim, utils
from time import gmtime, strftime
from math import sqrt
from enumerator2 import num_ingredients, num_actions
from recipe_steps import write_steps
from recipe_ingredients import write_ingredients
#from tester import print_recipe


# num_ingredients = total types of ingredients
# num_actions = total number of actions
INGREDIENTS = 10
STEPS = 10
INGREDIENTS_TYPES = 10
MAX_INGREDIENTS_PER_TYPE = 77
INGREDIENTS_SPACE = INGREDIENTS_TYPES + MAX_INGREDIENTS_PER_TYPE + 1
STEPS_SPACE = num_actions + 2 + num_ingredients
NUM_FEATURES = INGREDIENTS * INGREDIENTS_SPACE + STEPS * STEPS_SPACE
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
            nn.Sigmoid()
        )

    def forward(self, input):
        output = self.main(input)
        return output



def fit(lr, epochs, stats_interval, recipe_inteval, train_file, batch_size, out_file):

    if torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    discriminator = Discriminator().to(device)
    generator = Generator().to(device)

    criterion = nn.BCELoss()

    real_label = 1
    fake_label = 0

    optimizerD = optim.Adam(discriminator.parameters(), lr=lr, weight_decay=0)
    optimizerG = optim.Adam(generator.parameters(), lr=lr*2, weight_decay=0)

    d_losses = []
    g_losses = []
    recipe_list = []
    iters = 0

    train_set = torch.zeros(500, NUM_FEATURES)
    with open(train_file, "r") as file:
        i = 0
        for line in file.readlines():
            if i >= 500:
                break
            values = line.split(",")
            for j in range(NUM_FEATURES):
                train_set[i, j] = float(values[j])
            i += 1 

    #print(train_set)
    train_set = train_set.cuda()

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
            optimizerD.step()

            # Train with fake batch
            discriminator.zero_grad()
            generator.zero_grad()
            noise = torch.randn(batch_size, 10).cuda()
            fake_out = generator(noise)
            
            label.fill_(fake_label)
            output = discriminator(fake_out.detach()).view(-1)  # This part is pretty key

            error_d_fake = criterion(output, label)
            error_d_fake.backward()
            D_G_z1 = output.mean().item()

            error_d = error_d_real + error_d_fake

            optimizerD.step()

            ### Update generator

            label.fill_(real_label)

            output = discriminator(fake_out).view(-1)

            error_g = criterion(output, label)
            error_g.backward()
            D_G_z2 = output.mean().item()

            optimizerG.step()

            ### Training statistics

            if iters % stats_interval == 0:
                print("%s[%d/%d][%d/%d]\tLoss_D: %.4f\tLoss_G: %.4f\tD(x): %.4f\tD(G(z)): %.4f / %.4f" % (strftime("%H:%M:%S", gmtime()), epoch, epochs, num, len(data), error_d.item(), error_g.item(), D_x, D_G_z1, D_G_z2))

            # Save losses for later
            d_losses.append(error_d.item())
            g_losses.append(error_g.item())


            if iters % recipe_inteval == 0:
                with torch.no_grad():
                    fixed_random = torch.randn(10, device=device).cuda()
                    print(fixed_random)
                    t = generator(fixed_random).detach().cpu()
                    m = []
                    s = []

                    for i in range(INGREDIENTS):
                        idx = 0
                        m.append(0)
                        while idx < INGREDIENTS_TYPES:
                            f = t[i * INGREDIENTS_SPACE + idx]
                            if f > t[m[-1]]:
                                m[-1] = i * INGREDIENTS_SPACE + idx
                            idx +=1
                        m.append(0)
                        while idx < INGREDIENTS_SPACE and idx >= INGREDIENTS_TYPES:
                            f = t[i * INGREDIENTS_SPACE + idx]
                            if f > t[m[-1]]:
                                m[-1] = i * INGREDIENTS_SPACE + idx
                            idx += 1
                        s.append(INGREDIENTS_SPACE * (i + 1) - 1)

                    for i in range(STEPS):
                        idx = 0
                        m.append(0)
                        while idx < num_actions:
                            f = t[INGREDIENTS * INGREDIENTS_SPACE + i * (num_actions + 2 + num_ingredients) + idx]
                            if f > t[m[-1]]:
                                m[-1] = INGREDIENTS * INGREDIENTS_SPACE + i * (num_actions + 2 + num_ingredients) + idx
                            idx += 1
                        idx = num_actions + 2
                        s.append(INGREDIENTS * INGREDIENTS_SPACE + (num_actions + 2 + num_ingredients) * i + num_actions)
                        s.append(INGREDIENTS * INGREDIENTS_SPACE + (num_actions + 2 + num_ingredients) * i + num_actions + 1)
                        m.append(INGREDIENTS * INGREDIENTS_SPACE + (num_actions + 2 + num_ingredients) * i + num_actions + 2)
                        while idx < (num_actions + 2 + num_ingredients) and idx >= (num_actions + 2):
                            f = t[INGREDIENTS * INGREDIENTS_SPACE + i * (num_actions + 2 + num_ingredients) + idx]
                            if f > t[m[-1]]:
                                m[-1] = INGREDIENTS * INGREDIENTS_SPACE + i * (num_actions + 2 + num_ingredients) + idx
                            idx += 1
    
                    for i in range(len(t)):
                        if i not in m and i not in s:
                            t[i] = float(0)
                        elif i not in s:
                            t[i] = float(1)

                    print(t)

                with open(out_file, "a") as outf:
                    s = ""
                    for f in t:
                        s += str(float(f)) + ", "
                    outf.write(s[:-2] + "\n")

                torch.save(generator, "remy.pt")

                recipe_list.append(t)

            iters += 1

    #print("Done training, here are some example recipes!")
    #for i in range(10):
    #   print(generator.forward([random.random() for i in range(10)]))


def main():
    fit(0.000005, 20000, 100, 1000, "recipes/encoded.txt", 100, "out.txt")


if __name__ == "__main__":
    main()
