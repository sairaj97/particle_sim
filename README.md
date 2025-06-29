# 🧪 2D Particle Collision Simulator

A real-time physics-based simulation of particles moving and colliding in 2D space, built using **Python**, **Pygame**, and **NumPy**.

This project models elastic collisions and wall bounces with interactive visualization. It's ideal for exploring core physics concepts like conservation of momentum, force resolution, and kinematics.

---

## 🎥 Demo

https://www.linkedin.com/posts/sairaj-sawant-249127154_python-simulation-physics-activity-7345162947414917120-tOm6?utm_source=share&utm_medium=member_desktop&rcm=ACoAACUJnpkBUDGj8g_xVizRS-avPMVcFLzidXE

---

## 🚀 Features

- Realistic elastic collisions between particles
- Boundary (wall) collisions with reflection
- Randomized initial conditions (position, velocity, size)
- Real-time rendering at 60 FPS using `pygame`
- Easily extensible for forces, gravity, or user input

---

## 🛠️ Tech Stack

- Python 3.x
- Pygame
- NumPy

---

## 📦 Installation (WSL / Ubuntu)

```bash
# 1. Clone the repo
git clone https://github.com/sairaj97/particle_sim
cd particle_sim

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the simulation
python main.py
```

---

## 📁 File Structure

```
particle_sim/
│
├── particle.py        # Defines the Particle class and physics logic
├── main.py            # Pygame setup, rendering, and simulation loop
├── requirements.txt   # Dependencies: pygame, numpy
├── README.md          # This file
└── .gitignore         # Python + editor exclusions
```

---

## 📚 Physics Behind the Scenes

- **Elastic Collisions**: Implemented using momentum conservation and impulse formulas.
- **Wall Collisions**: Velocity inversion on boundary impact.
- **Overlap Resolution**: Prevents objects from sticking post-collision.
- **Vector Math**: Powered by NumPy for accurate and efficient computation.

---

## 💡 Future Improvements

- Add gravitational attraction or drag
- Support user-created particles via mouse clicks
- Display energy, velocity vectors, or collision counts
- Export simulation as a video or dataset for ML training

---

## 🤖 Why This Matters for LLMs

This project reflects the integration of physics simulation code with potential **LLM-driven agents** that can:
- Learn from collision outcomes (reward feedback)
- Adjust particle behavior (via code generation)
- Optimize or generate physical scenarios using reinforcement learning

Great base for combining physical simulations with **machine learning workflows**.

---


## 🧠 Author

**Saira** — [LinkedIn](https://www.linkedin.com/in/sairaj-sawant-249127154/) | [GitHub](https://github.com/sairaj97)

---

## 📝 License

MIT License — feel free to use, modify, and share!
