import mss
import mss.tools

def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)

        mss.tools.to_png(
            screenshot.rgb,
            screenshot.size,
            output="screen.png"
        )


if __name__ == "__main__":
    capture_screen()
    print("Pantalla capturada correctamente.")