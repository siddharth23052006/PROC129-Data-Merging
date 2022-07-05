import csv
import pandas as pd

df = pd.read_csv("Field_Brown_Dwarf_Stars.csv")
df = df[df["star_distance"].notna()]
df = df[df["star_mass"].notna()]
df = df[df["star_radius"].notna()]

masses = []
radii = []

for mass in df["star_mass"]: masses.append(float(mass)*0.000954588)
for radius in df["star_radius"]: radii.append(float(radius)*0.102763)

df["star_mass"] = masses
df["star_radius"] = radii
headers = ["star_names", "star_distance", "star_mass", "star_radius"]
df.pop('Unnamed: 0')

df.to_csv('Brown_Dwarfs_Masses_Radii.csv')