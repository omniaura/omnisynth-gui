import os

# create omnisynth whl if not already there
# omnisynth_dist_loc = '../omnisynth-dev/omnisynth/'
os.system('cd ../omnisynth-dev/omnisynth/ && python -m build')

# install all deps
os.system("pip install -r requirements.txt")

# post install commands
os.system('garden install graph && garden install matplotlib')