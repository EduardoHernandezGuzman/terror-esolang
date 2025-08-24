# Cómo colaborar en TERROR

¡Gracias por tu interés en contribuir a **TERROR**!  
Este proyecto está pensado para aprender, divertirse y rendir homenaje a los bolsilibros de terror.

---

## Cómo empezar
1. Haz un **fork** del repositorio en tu cuenta de GitHub.
2. Clona tu fork en tu ordenador:
   ```bash
   git clone https://github.com/<tu-usuario>/terror-esolang.git
   cd terror-esolang
   ```
3. Crea una rama para tu cambio:
   ```bash
   git checkout -b feature/mi-mejora
   ```

---

## Requisitos
- **Python 3.8+**
- **pytest** (para correr los tests)
  ```bash
  pip install pytest
  ```

---

## Buenas prácticas
- Añade ejemplos en la carpeta `examples/` si creas nuevas funciones.
- Añade tests en la carpeta `tests/` para validar tu cambio.
- Usa nombres claros para tus commits:
  - `feat: añadir RITUALES`
  - `fix: corregir error en lectura de SUSURRO`
  - `docs: mejorar README`

---

## Flujo de trabajo
1. Haz cambios en tu rama.
2. Comprueba que todo funciona:
   ```bash
   pytest
   ```
3. Haz commit y sube tus cambios:
   ```bash
   git add .
   git commit -m "feat: descripción del cambio"
   git push origin feature/mi-mejora
   ```
4. Abre un **Pull Request** en GitHub describiendo tu contribución.

---

## Ideas para colaborar
- Escribir más ejemplos narrativos en `.bolsi`.
- Mejorar los mensajes de error del intérprete.
- Implementar macros *RITUALES*.
- Añadir etiquetas *ESCENA/IR* para saltos.
- Crear un traductor TERROR → Brainfuck.

---

¡Toda ayuda es bienvenida!  
Aunque sea tu **primer PR**, siéntete libre de intentarlo.