import arcade.gui
import arcade
import json
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load values from .env file
load_dotenv()


WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.5


class ScoreView(arcade.View):
    def __init__(self):
        super().__init__()
        self.scroll_offset = 0
        self.scroll_speed = 1
        self.nb_lines_to_display = 15
        self.text_color = arcade.color.BLACK
        self.isEmailSent = False
        self.data = []
        self.button_style = {
            "font_name": ("Comic Sans MS"),
            "font_size": 20,
            "font_color": arcade.color.BLACK,
            "border_width": 2,
            "border_color": None,
            "bg_color": arcade.color.GRULLO,
        }
        with open("../score.json", "r") as json_file:
            self.data = json.load(json_file)
        self.data = sorted(self.data, key=lambda x: x["score"], reverse=True)
        self.arrow_up_texture = arcade.load_texture(
            ":resources:onscreen_controls/shaded_dark/up.png"
        )
        self.arrow_down_texture = arcade.load_texture(
            ":resources:onscreen_controls/shaded_dark/down.png"
        )
        self.exit_texture = arcade.load_texture(":resources:images/tiles/signExit.png")

        self.arrow_button_width = self.arrow_up_texture.width
        self.arrow_button_height = self.arrow_up_texture.height

    def on_show_view(self):
        background_color = (255, 228, 181)
        self.text_color = arcade.color.BLACK
        arcade.set_background_color(background_color)
        self.window.on_key_press = self.on_key_press
        self.window.on_key_release = self.on_key_release

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(
            WIDTH - 650,
            HEIGHT - 420,
            self.exit_texture.width,
            self.exit_texture.height,
            self.exit_texture,
        )

        arcade.draw_text(
            "Highest scores : ",
            WIDTH / 2,
            HEIGHT / 1.25,
            self.text_color,
            font_size=40,
            anchor_x="center",
        )
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        if self.isEmailSent == False:
            email_button = arcade.gui.UIFlatButton(
                text="Send email", width=200, height=50, style=self.button_style
            )
            email_button.on_click = self.sendEmail
            self.uimanager.add(
                arcade.gui.UIAnchorWidget(
                    anchor_x="center_x", align_y=-250, child=email_button
                )
            )
        else:
            arcade.draw_text(
                "Email sent !",
                150,
                50,
                arcade.color.GREEN,
                font_size=35,
            )
        start_index = self.scroll_offset
        end_index = start_index + self.nb_lines_to_display

        y = HEIGHT - 150
        for i in range(start_index, min(end_index, len(self.data))):
            item = self.data[i]
            name = item["name"]
            score = item["score"]

            data_line = f" {name}, Score: {score}"

            arcade.draw_text(
                data_line,
                WIDTH / 2,
                y,
                arcade.color.BLACK,
                font_size=16,
                anchor_x="center",
                anchor_y="center",
            )

            y -= 20

        if len(self.data) > self.nb_lines_to_display:
            arcade.draw_texture_rectangle(
                WIDTH - 60,
                HEIGHT - 60,
                self.arrow_button_width,
                self.arrow_button_height,
                self.arrow_up_texture,
            )

            arcade.draw_texture_rectangle(
                WIDTH - 60,
                60,
                self.arrow_button_width,
                self.arrow_button_height,
                self.arrow_down_texture,
            )

        self.uimanager.draw()

    def scrollUp(self):
        self.scroll_offset += self.scroll_speed
        self.scroll_offset = max(0, min(self.scroll_offset, len(self.data) - 1))

    def sendEmail(self, event):
        if self.isEmailSent == False:
            email_username = os.getenv("SMTP_USERNAME")
            email_password = os.getenv("SMTP_PWD")
            to_email = "martinmille@outlook.fr"
            smtp_server = "smtp-mail.outlook.com"
            smtp_port = 587
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(email_username, email_password)
            top_5_scores = self.data[:5]
            subject = "Highest scores"
            email_content = "Here are the highest scores:\n\n"
            for i, score_data in enumerate(top_5_scores, start=1):
                player_name = score_data["name"]
                player_score = score_data["score"]
                email_content += f"Joueur {i}: {player_name} - {player_score}\n"
            msg = MIMEMultipart()
            msg["From"] = email_username
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(email_content, "plain"))
            server.sendmail(email_username, to_email, msg.as_string())
            server.quit()
            self.isEmailSent = True

    def scrollDown(self):
        self.scroll_offset -= self.scroll_speed
        self.scroll_offset = max(0, min(self.scroll_offset, len(self.data) - 1))

    def on_mouse_press(self, x, y, button, modifiers):
        if (
            WIDTH - 650 - self.exit_texture.width / 2
            <= x
            <= WIDTH - 650 + self.exit_texture.width / 2
            and HEIGHT - 420 - self.exit_texture.height / 2
            <= y
            <= HEIGHT - 420 + self.exit_texture.height / 2
        ):
            from menu import MainMenuView

            menu_view = MainMenuView()
            self.window.show_view(menu_view)

        if len(self.data) > self.nb_lines_to_display:
            if button == arcade.MOUSE_BUTTON_LEFT:
                if (
                    WIDTH - 60 - self.arrow_button_width / 2
                    <= x
                    <= WIDTH - 60 + self.arrow_button_width / 2
                    and HEIGHT - 60 - self.arrow_button_height / 2
                    <= y
                    <= HEIGHT - 60 + self.arrow_button_height / 2
                ):
                    self.scrollDown()

                elif (
                    WIDTH - 60 - self.arrow_button_width / 2
                    <= x
                    <= WIDTH - 60 + self.arrow_button_width / 2
                    and 60 - self.arrow_button_height / 2
                    <= y
                    <= 60 + self.arrow_button_height / 2
                ):
                    self.scrollUp()
