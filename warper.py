import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animator

x_extent = 2
y_extent = 1.5
spacing = .2
n_frames = 90


def smoothfunc(t):
   return t * t * (3 - 2*t)

def plane(x_extent, y_extent, spacing, resolution, colors = True, polar = False, wide = True):
   if wide:
      x_extent = 2*x_extent
      y_extent = 2*y_extent
   if colors:
      blue = "tab:blue"
      red = "tab:red"
   else:
      blue = red = "black"
   grid = []
   if not polar:
      x = np.linspace(-x_extent, x_extent, resolution)
      y = np.linspace(-y_extent, y_extent, resolution)

      # number of rows and colums to mantain a square pattern
      nx = int(np.floor(x_extent / spacing + 1e-9))
      ny = int(np.floor(y_extent / spacing + 1e-9))

      #horizontal lines: [Im] constant and [Re] varies
      for m in range(-ny, ny + 1):
         if m != 0:
            grid.append((x + 1j * m * spacing, blue))

      #vertical lines: [Re] constant and [Im] varies
      for k in range(-nx, nx + 1):
         if k != 0:
            grid.append((k * spacing + 1j * y, red))

      #axes drawn in black
      grid.append((x , "black"))
      grid.append((1j * y, "black"))
   else:
      #number of rays
      n_rays = int(np.floor(24/spacing + 1e-9) + 1)

      # radius needed to cover the corners of the view window
      R = np.hypot(x_extent, y_extent)
      theta = np.linspace(0, 2 * np.pi, resolution)
      r = np.linspace(-R, R, resolution)

      # circles: radius = k * spacing
      for k in range(1, int(np.floor(R / spacing + 1e-9)) + 1):
         grid.append((k * spacing * np.exp(1j * theta), blue))

      # rays: straight lines through the origin, equal angle steps
      # n_rays must be even so that the Re and Im axes are among them
      for ang in np.linspace(0, np.pi, n_rays, endpoint=False):
         grid.append((r * np.exp(1j * ang), red))

      # axes
      grid.append((r + 0j, "black"))
      grid.append((1j * r, "black"))


   return grid

def f(z):
   return z**3

grid = plane(x_extent, y_extent, spacing, 900)

fig, ax = plt.subplots(figsize=(11, 11))

def updater(frame): #this function updates each frame
   t = frame / (n_frames - 1)
   ax.clear()
   ax.set_aspect("equal")
   ax.set_xlim(-x_extent, x_extent)
   ax.set_ylim(-y_extent, y_extent)
   ax.axhline(0, color="gray", lw=0.5)
   ax.axvline(0, color="gray", lw=0.5)
   ax.set_xlabel("Re")
   ax.set_ylabel("Im")

   for z, color in grid:
      z = z + smoothfunc(t)*(f(z) - z)
      ax.plot(z.real, z.imag, color=color, lw=1.0)


anim = animator.FuncAnimation(fig, updater, frames = n_frames, interval = 33)
plt.show()