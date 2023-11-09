# Get A Guitar 🎸

## Description
A Python implementation of the Karplus-Strong algorithm to mimic the sound of a guitar.

## Algorithm Used
The Karplus-Strong algorithm, a digital signal processing technique, models the sound of a plucked string instrument like a guitar. It generates a sound that closely resembles the sound of a string being plucked, using a combination of noise and filtering. The algorithm produces sounds similar to a guitar by creating a simple digital filter that acts as a low-pass filter. It essentially models the behavior of a vibrating string, considering factors such as decay and resonance. By combining white noise with a delay line, it generates a rich, plucked string sound.

## Set-up
1. Download all starter files from this link: [Guitar Starter Files](https://penoy.admu.edu.ph/~guadalupe154884/classes/csci30/guitar_files.zip)
2. Set up a Python virtual environment by running `python -m venv guitarenv`. Activate the environment:
    Linux/macOS: `source guitarenv/bin/activate`
    Windows: `guitarenv\Scripts\activate`
3. Install the required packages using `pip install -r requirements.txt`.
4. Verify the installed packages with `pip freeze`.
5. Test the stdaudio library by running `python stdaudio.py` in the terminal. Adjust the volume before running the script.
6. [For macOS users] Ensure [Homebrew](https://brew.sh/), Xcode Command Line Tools, and SDL dependencies are installed for PyGame.

## Strum away!
To run the program, navigate to the project folder and execute python guitar.py in the terminal. A black window should pop up. Press any character in `q2we4r5ty7u8i9op-[=]` to play a guitar string sound.
