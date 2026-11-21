import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animator

extent = 4

def smoothfunc(t):
   return t * t * (3-2)*t

def plane(extent, n_lines, resolution, polar = False, colors = True):
   if colors:
      blue = "tab:blue"
      red = "tab:red"
   else:
      blue = red = "black"
   grid = []
   if not polar:
      s = np.linspace(-extent, extent, resolution)
      for c in np.linspace(-extent, extent, n_lines):
         grid.append((s + 1j * c, blue)) #horizontal lines
         grid.append((c + 1j * s, red)) #vertical lines
      grid.append((s , "black"))
      grid.append((1j * s, "black"))
   else:
      theta = np.linspace(0, 2 * np.pi, resolution)
      r = np.linspace(-extent, extent, resolution)
      for rad in np.linspace(extent / n_lines * 2, extent * 1.4, n_lines // 2):
         grid.append((rad * np.exp(1j * theta), blue))      # circles
      for ang in np.linspace(0, np.pi, n_lines, endpoint=False):
         grid.append((r * 1.4 * np.exp(1j * ang), red))     # rays
      grid.append((r , "black"))
      grid.append((1j * r, "black"))
   return grid

def f(z):
   return z**2

grid = plane(extent, 21 , 900, polar=False)

fig, ax = plt.subplots(figsize=(11, 11))
ax.set_aspect("equal")
ax.set_xlim(-extent, extent)
ax.set_ylim(-extent, extent)
ax.axhline(0, color="gray", lw=0.5)
ax.axvline(0, color="gray", lw=0.5)
ax.set_xlabel("Re")
ax.set_ylabel("Im")

for z, color in grid:
   z = f(z)
   ax.plot(z.real, z.imag, color=color, lw=1.0)


plt.show()
