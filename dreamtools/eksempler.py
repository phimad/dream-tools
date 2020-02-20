import dreamtools as dt


# Åben gdx fil
gdx = dt.Gdx("test.gdx")

# Hent sets fra gdx
s, i, t = gdx.get("s", "i", "t")

# Hent variable fra gdx
qY, qBNP, qI_s = gdx.get("qY", "qBNP", "qI_s")

# Plot variabel
qBNP.plot()

# Plot variabel i begrænset periode
qBNP.plot(2010, 2020)

# Plot variabel begrænset til et enkelt element eller set
qY["tot"].plot()
qY[s].plot()

# Plot flere variable sammen
dt.plot(qY[s], qBNP, start=2010, end=2020)

# Hvis en serie har flere dimensioner, skal vi skrive .loc for at begrænse med på mere end første dimension. Fx:
qI_s.loc[i,s]

# Vi kan stadig begænse på første dimension uden .loc
qI_s[i]

# Hvis vi begrænser første dimnension til et enkelt element kan vi derefter begrænse anden dimension uden .loc
qI_s["IB"]["bol"] == qI_s.loc["IB","bol"]
# Generelt er det en god idé at skrive .loc hvis man er i tvivl
# (det gør det eksplicit at vi vil bruge 'label based indexing' fremfor et numerisk indeks)

# Sæt globalt standard startår og slutår
dt.time(2010, 2040)

# Gang to variable sammen
vY = gdx["pY"]*qY
# Divider med variablens værdi i 2010
vY /= vY[:,'2010']
# Plot med en overskrift tilføjet
vY[s].plot(title="pY*qY, index=2010")

# Check at der eksisterer en 'images' mappe og opret den hvis den ikke gør
import os
if not os.path.exists("images"):
  os.mkdir("images")

# Plot som statisk billed, fx som svg, pdf eller png. Bemærk at mange billed-formater kan åbnes direkte i PyCharm
qBNP.plot(file="images/plot.svg")
# Dette kræver at man har Orca installeret - spørg evt. Lucas eller undertegnede for hjælp


# Skift om der renderes til browser, pdf, png etc. som standard
import plotly.io as pio
pio.renderers.default = "browser"


