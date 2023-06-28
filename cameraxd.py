from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
from PIL import Image
from picamera import PiCamera

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the image using picamera and save it with a timestamp.
        '''
        camera = PiCamera()
        timestr = time.strftime("%Y%m%d_%H%M%S")
        image_path = "IMG_{}.png".format(timestr)
        camera.capture(image_path)
        camera.close()
        print("Captured image:", image_path)

        # Convert the captured image to PIL format (optional)
        pil_image = Image.open(image_path)
        # Do further processing with the PIL image if needed

        # Display the captured image in Kivy (optional)
        # You can add an Image widget to your layout and set its source to 'image_path'

        # Note: Make sure to handle exceptions, release the camera, and clean up properly


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()
