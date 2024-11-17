1. Download all files into a single folder (In my case, it was named MP_folder

2. This egg game doesn't require you to input a game_level_file in the terminal, just run the "main.py" file and you're good to go!
  For example:
    davidfrancisco@Jesses-Laptop MP_folder % python3.12 main.py ✅
    davidfrancisco@Jesses-Laptop MP_folder % python3.12 main.py level_1.txt ❌
   
3. To create a game level file, follow this naming format:
   level_{number}.txt; eg. level_34.txt ✅
   
   The .txt file should contain this:
    The first row should be the number of rows of the game_level
    The second row should be the total number of moves that is allowed for the game level
    The third row should be display the game level's grid
