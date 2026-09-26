from manim import *
from numpy.ma.core import size
from scipy.signal import square


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle)) # show the circle on screen



class CircularLinkedList(Scene):
    def construct(self):
        node1=Square(fill_opacity=0.2)
        node2=Square(fill_opacity=0.2)
        self.play(Create(node1))
        self.wait()


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

