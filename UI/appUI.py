import os
import time
import flet
from flet import (
    Page,
    Event,
    LongPressEndEvent,
    Ref,
    TextField,
    Text,
    Icon,
    icons,
    ElevatedButton,
    Row,
    ThemeMode,
    ListTile,
    AlertDialog,
    dropdown,
    Dropdown,
    FilePicker,
    FilePickerFileType,
    FilePickerResultEvent
)
from Core.AiCore import image_detection, video_detection


def main(page: Page):
    page.title = "POD Project"
    page.window_width = 800
    page.window_height = 600
    page.theme_mode = ThemeMode.SYSTEM
    page.window_center()
    page.update()

    def onclick_tile(event: Event):
        os.startfile(event.control.subtitle.value)

    def type_checker(inp_file: str):
        file_ext = os.path.basename(inp_file).split(".")[-1]
        if file_ext in ["mp4", "avi", "wmv", "mkv"]:
            return icons.VIDEO_FILE

        elif file_ext in ["png", "jpg", "jpeg"]:
            return icons.IMAGE

        else:
            return icons.DEVICE_UNKNOWN

    def select_tile(event: LongPressEndEvent):

        if event.control.selected == True:
            event.control.selected = False
            detect_btn.disabled = True
            remove_btn.disabled = True
        else:
            event.control.selected = True
            detect_btn.disabled = False
            remove_btn.disabled = False
        page.update()

    def remove_selected(event: Event):
        for item in page.controls:
            if isinstance(item, ListTile) and item.selected == True:
                page.remove(item)
            else:
                ...
                # detect_btn.disabled = True
                # remove_btn.disabled = True
        page.update()

    def add_files(event: Event):
        if not detection_mode.value:
            alert_message.open = True
            page.update()
        else:
            if detection_mode.value == "Image":
                file_picker.pick_files("Upload Image", file_type=FilePickerFileType.IMAGE)
            elif detection_mode.value == "Video":
                file_picker.pick_files("Upload Video", file_type=FilePickerFileType.VIDEO)

    def on_file_result(event: FilePickerResultEvent):
        file_name = "".join(map(lambda f: f.name, event.files))
        file_path = "".join(map(lambda f: f.path, event.files))
        page.add(
            ListTile(
                title=Text(file_name),
                subtitle=Text(file_path),
                leading=Icon(type_checker(file_name)),
                trailing=Text(time.ctime()),
                on_click=onclick_tile,
                on_long_press=select_tile,
            )
        )

    def start_detection(event: Event):
        file_path = "".join(map(lambda f: f.path, file_picker.result.files))
        page.window_always_on_top = False
        page.update()
        if detection_mode.value == "Image":
            image_detection(file_path)

        elif detection_mode.value == "Video":
            video_detection(file_path)

    def alert_actions(event: Event):
        alert_message.open = False
        page.update()

    file_picker = FilePicker(on_result=on_file_result)
    page.overlay.append(file_picker)

    """ Remove Button """
    remove_btn = ElevatedButton(icon=icons.DELETE, text="Remove", on_click=remove_selected, disabled=True)

    """ Detection Button """
    detect_btn = ElevatedButton(icon=icons.START, text="Start Detection", on_click=start_detection, disabled=True)

    """ Upload Button """
    upload_btn = ElevatedButton(icon=icons.ADD, text="Add File", on_click=add_files)

    """ Alert Dialog """
    alert_message = AlertDialog(
        title=Text("Message"),
        actions=[ElevatedButton(text="OK", on_click=alert_actions)],
        content=Text("Please choose detect mode first!")
    )
    page.dialog = alert_message

    """ Detection Mode """
    detection_mode = Dropdown(
        hint_text="Choose Detection Mode",
        options=[
            dropdown.Option("Image"),
            dropdown.Option("Video"),
            dropdown.Option("Webcam"),
        ]
    )

    page.add(
        Row(
            controls=[
                detection_mode,
                upload_btn,
                detect_btn,
                remove_btn
            ]
        )
    )


def run_app():
    flet.app(target=main)


if __name__ == "__main__":
    run_app()
