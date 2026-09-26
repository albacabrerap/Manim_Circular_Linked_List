from manim import *
from PIL import Image, ImageFilter

#scene1
class MusicPlayer(Scene):
    def construct(self):

        player_card = Rectangle(
            width=5,
            height=6,
            color=BLUE,
            fill_opacity=0.2,
            stroke_width=3
        )

        another=Rectangle(
            fill_opacity=0.2,
            width=4,
            height=4,
            color=BLUE,
        ).move_to(player_card.get_center() + UP * 0.5)

        p1 = Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(PI / 2)
        p2 = Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(PI / 2).next_to(p1, LEFT, buff=-0.1)
        prev_btn = VGroup(p1, p2).move_to(player_card.get_center() + DOWN * 2.2 + LEFT * 1.3)

        play_btn = Triangle(color=WHITE, fill_opacity=1).scale(0.25).rotate(-PI / 2)
        play_btn.move_to(player_card.get_center() + DOWN * 2.2)

        n1 = Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(-PI / 2)
        n2 = Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(-PI / 2).next_to(n1, RIGHT, buff=-0.1)
        next_btn = VGroup(n1, n2).move_to(player_card.get_center() + DOWN * 2.2 + RIGHT * 1.3)

        song_title = Text("Track 1", font_size=28, weight=BOLD, opacity=0.4).move_to(player_card.get_center() + DOWN)

        controls = VGroup(prev_btn, play_btn, next_btn, song_title)

        self.play(FadeIn(player_card), FadeIn(another), FadeIn(controls))
        self.wait(0.6)

        self.play(next_btn.animate.set_opacity(0.2), run_time=0.25)
        self.play(next_btn.animate.set_opacity(1.0), run_time=0.25)

        track_2 = Text("Track 2", font_size=28, weight=BOLD, opacity=0.4).move_to(song_title)
        self.play(
            player_card.animate.set_color(TEAL).set_fill(TEAL, opacity=0.2),
            another.animate.set_color(TEAL).set_fill(TEAL, opacity=0.2),
            Transform(song_title, track_2),
            run_time=1.2
        )
        self.wait(1)

        self.play(prev_btn.animate.set_opacity(0.2), run_time=0.25)
        self.play(prev_btn.animate.set_opacity(1.0), run_time=0.25)

        track_1_again = Text("Track 1", font_size=28, weight=BOLD).move_to(song_title)
        self.play(
            player_card.animate.set_color(BLUE).set_fill(BLUE, opacity=0.2),
            another.animate.set_color(BLUE).set_fill(BLUE, opacity=0.2),
            Transform(song_title, track_1_again),
            run_time=1.2
        )
        self.wait(1.2)

#scene2
class MusicPlayerZoom(MovingCameraScene):
    def construct(self):
        player_card = Rectangle(
            width=5,
            height=6,
            color=BLUE,
            fill_opacity=0.2,
            stroke_width=3
        )

        another = Rectangle(
            fill_opacity=0.2,
            width=4,
            height=4,
            color=BLUE,
        ).move_to(player_card.get_center() + UP * 0.5)

        p1 = Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(PI / 2)
        p2 = Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(PI / 2).next_to(p1, LEFT, buff=-0.1)
        prev_btn = VGroup(p1, p2).move_to(player_card.get_center() + DOWN * 2.2 + LEFT * 1.3)

        play_btn = Triangle(color=WHITE, fill_opacity=1).scale(0.25).rotate(-PI / 2)
        play_btn.move_to(player_card.get_center() + DOWN * 2.2)

        n1 = Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(-PI / 2)
        n2 = Triangle(color=WHITE, fill_opacity=1).scale(0.2).rotate(-PI / 2).next_to(n1, RIGHT, buff=-0.1)
        next_btn = VGroup(n1, n2).move_to(player_card.get_center() + DOWN * 2.2 + RIGHT * 1.3)

        song_title = Text("Track 1", font_size=28, weight=BOLD, opacity=0.4).move_to(player_card.get_center() + DOWN)

        player_group = VGroup(player_card,another, prev_btn,play_btn, next_btn, song_title)


        black_bg = Rectangle(width=14, height=8, color=BLACK, fill_opacity=1)
        black_bg.set_z_index(-10)

        self.add(black_bg)
        self.add(player_group)
        self.wait(1)

        self.play(
            self.camera.frame.animate.move_to(player_card.get_center()).scale(0.05),
            FadeOut(player_group),
            run_time=0.3,
            rate_func=linear
        )
        self.wait(2)


from manim import *

class Introduction(Scene):
    def construct(self):

        node1 = Square(color=BLUE, fill_opacity=0.2).scale(0.5).shift(LEFT * 1.8)
        node2 = Square(color=BLUE, fill_opacity=0.2).scale(0.5).move_to(ORIGIN)
        node3 = Square(color=BLUE, fill_opacity=0.2).scale(0.5).shift(RIGHT * 1.8)
        squares = VGroup(node1, node2, node3)

        arrow1 = Arrow(start=node1.get_right(),
                       end=node2.get_left(),
                       stroke_width=3, buff=-1, max_tip_length_to_length_ratio=0.3)
        arrow2 = Arrow(start=node2.get_right(),
                       end=node3.get_left(),
                       stroke_width=3, buff=-1, max_tip_length_to_length_ratio=0.3)

        arrow3 = VGroup(
            Line(start=node3.get_right(), end=node3.get_right() + RIGHT * 0.4),
            Line(start=node3.get_right() + RIGHT * 0.4,end=[node3.get_right()[0] + 0.4, node1.get_bottom()[1] - 0.4, 0]),
            Line(start=[node3.get_right()[0] + 0.4, node1.get_bottom()[1] - 0.4, 0],end=[node1.get_left()[0] - 0.4, node1.get_bottom()[1] - 0.4, 0]),
            Line(start=[node1.get_left()[0] - 0.4, node1.get_bottom()[1] - 0.4, 0],end=[node1.get_left()[0] - 0.4, node1.get_left()[1], 0]),
            Arrow(start=[node1.get_left()[0] - 0.4, node1.get_left()[1], 0], end=node1.get_left(), stroke_width=3, max_tip_length_to_length_ratio=0.6))

        arrows=VGroup(arrow1, arrow2, arrow3)
        self.play(FadeIn(arrows), FadeIn(squares))
        self.wait(1)



