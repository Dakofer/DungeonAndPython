dnd_game/
│
├── main.py
│
├── engine/                     ← Infraestructura del motor
│   ├── game.py                 ← Game loop principal
│   ├── scene_manager.py
│   ├── base_scene.py
│   ├── input.py
│   └── config.py
│
├── scenes/                     ← Pantallas del juego
│   ├── main_menu_scene.py
│   ├── character_creator_scene.py
│   └── combat_scene.py
│
├── core/                       ← Lógica pura (sin pygame)
│   ├── models/
│   │   ├── character.py
│   │   └── stats.py
│   │
│   ├── rules/
│   │   ├── modifiers.py
│   │   └── damage.py
│   │
│   ├── systems/
│   │   └── combat_system.py
│   │
│   └── services/
│       ├── xml_service.py
│       └── pdf_service.py
│
├── assets/
│   ├── images/
│   ├── fonts/
│   └── sounds/
│
└── saves/

Qué construir primero (orden exacto)
Paso 1 — engine/base_scene.py

Define una clase abstracta:

handle_event()

update()

render()

Todas las escenas heredarán de esto.

Paso 2 — engine/scene_manager.py

Clase que:

Guarda escena actual

Permite cambiar escena

Llama update/render

Paso 3 — engine/game.py

Aquí vive el game loop:

while running:
    handle_events()
    update()
    render()


Nada más.

Paso 4 — Crear MainMenuScene

Solo que muestre:

1. Crear personaje
2. Combate
3. Salir


Y permita cambiar de escena.

Paso 5 — Modelo básico

Crear en core/models:

Character:

name

hp

attack

defense

Sin XML todavía.
Sin PDF todavía.

Paso 6 — CombatSystem simple

En core/systems:

Método:

attack(attacker, defender)

Que reste HP usando reglas simples.

Sin animaciones.
Solo lógica.

diagrama de flujo 
main.py
   ↓
Game
   ↓
SceneManager
   ↓
MainMenuScene
   ↓
CombatScene
   ↓
CombatSystem (core)
   ↓
Character Model
