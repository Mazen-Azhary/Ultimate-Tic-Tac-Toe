# Ultimate Tic Tac Toe by Mazen Azhary

## Overview

This is a modular PyQt5 implementation of Ultimate Tic Tac Toe. The project features a clean, maintainable architecture using signals and slots, robust theme support, and a user-friendly interface. The game logic and UI are fully separated for clarity and extensibility.

## File Descriptions

- **singleButton.py**

  - Implements the `SingleButton` class, representing each cell in a small board. Handles click events, updates its appearance based on the current theme and active state, and emits signals upward which propagate along the application hierarchy delivering info such as the location of button pressed , player pressing , etc...
    Prevents interaction after being conquered by a player.
- **singleBoard.py**

  - Implements the `SingleBoard` class, representing each 3x3 small board. Handles local win detection, button activation, and propagates button click signals upward. Ensures only valid moves are allowed and updates the UI for active/inactive states. The single board being conquered is represented by a 3*3 matrix where i search inside it for 1's or 0's which indicate x winning or y winning respectively , instead of iterating and checking on the button object itself which is more expensive.
- **largerBoard.py**

  - Implements the `LargerBoard` class, which manages the 3x3 grid of smaller boards. Handles board activation/deactivation, win detection for the overall game, and propagates signals upward to main script. Tracks conquered boards and their winner labels for theme updates. It has the 3*3 matrix idea similar to smaller board.
- **main.py**

  - Entry point for the application. Sets up the main window, top controls (theme toggle, new game burron, player turn label, tutorial page button), and manages the overall game state. Handles player turn logic, end-of-game UI, and theme switching. All signal/slot connections to the main game logic are managed here.
- **uiComp/**

  - Contains UI resources, such as the main icon (`Ultimate_Tic_Tac_Toe.png`) and the Qt Designer `.ui` file for the tutorial page.
- **tutorialPage.py**

  - Loads and displays the tutorial UI, providing instructions for new players.

## Good Practices Followed

- **Modular Design:** Each class is in its own file, with clear responsibilities and no circular imports.
- **Signal/Slot Pattern:** All communication between widgets is via PyQt signals and slots, ensuring effecient communication between classes.
- **Single Source of Truth:** Player turn logic and game state are managed only at the top level (`main.py`), with all lower components emitting signals upward.
- **Theme Support:** A global theme token and `updateTheme` methods in each widget allow for robust, consistent theme switching, including conquered boards.
- **Player static var in singleButton** Same idea as Theme Support , instead of passing the player X or O from main to button , we create a static var visible to the 81 buttons and toggling it through 1 method only , mirroring the actual player turn pattern .
- **UI/Logic Separation:** Game logic is separated from UI code, making it easy to extend or refactor frontend or backend alone.
- **Resource Handling:** All resources are loaded using relative paths for compatibility with PyInstaller packaging.
- **Error Handling:** Defensive checks and try/except blocks prevent runtime errors from deleted widgets or late signals.
- **User Experience:** The UI provides clear feedback for active/inactive boards, winner display, and allows restarting or toggling theme at any time.

## How to Run

1. Install requirements: `pip install PyQt5`
2. Run the game: `python main.py`
3. To package as an executable, use PyInstaller:
   ```
   pyinstaller --onefile --add-data "uiComp;uiComp" main.py
   ```

Enjoy playing Ultimate Tic Tac Toe!

## Overview

This is a modular PyQt5 implementation of Ultimate Tic Tac Toe, created by Mazen Azhary. The project features a clean, maintainable architecture using signals and slots, robust theme support, and a user-friendly interface. The game logic and UI are fully separated for clarity and extensibility.

## Author

**Mazen Azhary**

## File Descriptions

- **main.py**

  - Entry point for the application. Sets up the main window, top controls (theme toggle, new game, player turn label, tutorial), and manages the overall game state. Handles player turn logic, end-of-game UI, and theme switching. All signal/slot connections to the main game logic are managed here.
- **largerBoard.py**

  - Implements the `LargerBoard` class, which manages the 3x3 grid of smaller boards. Handles board activation/deactivation, win detection for the overall game, and propagates signals upward. Tracks conquered boards and their winner labels for theme updates.
- **singleBoard.py**

  - Implements the `SingleBoard` class, representing each 3x3 small board. Handles local win detection, button activation, and propagates button click signals upward. Ensures only valid moves are allowed and updates the UI for active/inactive states.
- **singleButton.py**

  - Implements the `SingleButton` class, representing each cell in a small board. Handles click events, updates its appearance based on the current theme and active state, and emits signals upward. Prevents interaction after being conquered or deleted.
- **uiComp/**

  - Contains UI resources, such as the main icon (`Ultimate_Tic_Tac_Toe.png`) and the Qt Designer `.ui` file for the tutorial page.
- **tutorialPage.py**

  - Loads and displays the tutorial UI, providing instructions for new players.

## Good Practices Followed

- **Modular Design:** Each class is in its own file, with clear responsibilities and no circular imports.
- **Signal/Slot Pattern:** All communication between widgets is via PyQt signals and slots, ensuring decoupled and maintainable code.
- **Single Source of Truth:** Player turn logic and game state are managed only at the top level (`main.py`), with all lower components emitting signals upward.
- **Theme Support:** A global theme token and `updateTheme` methods in each widget allow for robust, consistent theme switching, including conquered boards.
- **UI/Logic Separation:** Game logic is separated from UI code, making it easy to extend or refactor.
- **Resource Handling:** All resources are loaded using relative paths for compatibility with PyInstaller packaging.
- **Error Handling:** Defensive checks and try/except blocks prevent runtime errors from deleted widgets or late signals.
- **User Experience:** The UI provides clear feedback for active/inactive boards, winner display, and allows restarting or toggling theme at any time.

## How to Run

1. Install requirements: `pip install PyQt5`
2. Run the game: `python main.py`
3. To package as an executable, use PyInstaller:
   ```
   pyinstaller --onefile --add-data "uiComp;uiComp" main.py
   ```

Enjoy playing Ultimate Tic Tac Toe!
