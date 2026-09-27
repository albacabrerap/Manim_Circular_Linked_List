from manim import *

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


class MultiPlayerZoom(Scene):

    def construct(self):
        def make_player(
            scale_factor=1.0, color=BLUE, track_text="Track 1", center=ORIGIN
        ):
          player_card = (
              Rectangle(
                  width=5,
                  height=6,
                  color=color,
                  fill_opacity=0.2,
                  stroke_width=3,
              )
              .scale(scale_factor)
              .move_to(center)
          )

          another = (
              Rectangle(fill_opacity=0.2, width=4, height=4, color=color)
              .scale(scale_factor)
              .move_to(player_card.get_center() + UP * 0.5 * scale_factor)
          )

          p1 = (
              Triangle(color=WHITE, fill_opacity=1)
              .scale(0.2 * scale_factor)
              .rotate(PI / 2)
          )
          p2 = (
              Triangle(color=WHITE, fill_opacity=1)
              .scale(0.2 * scale_factor)
              .rotate(PI / 2)
              .next_to(p1, LEFT, buff=-0.1 * scale_factor)
          )
          prev_btn = VGroup(p1, p2).move_to(
              player_card.get_center()
              + DOWN * 2.2 * scale_factor
              + LEFT * 1.3 * scale_factor
          )

          play_btn = (
              Triangle(color=WHITE, fill_opacity=1)
              .scale(0.25 * scale_factor)
              .rotate(-PI / 2)
          )
          play_btn.move_to(
              player_card.get_center() + DOWN * 2.2 * scale_factor
          )

          n1 = (
              Triangle(color=WHITE, fill_opacity=1)
              .scale(0.2 * scale_factor)
              .rotate(-PI / 2)
          )
          n2 = (
              Triangle(color=WHITE, fill_opacity=1)
              .scale(0.2 * scale_factor)
              .rotate(-PI / 2)
              .next_to(n1, RIGHT, buff=-0.1 * scale_factor)
          )
          next_btn = VGroup(n1, n2).move_to(
              player_card.get_center()
              + DOWN * 2.2 * scale_factor
              + RIGHT * 1.3 * scale_factor
          )

          song_title = (
              Text(
                  track_text,
                  font_size=int(28 * scale_factor),
                  weight=BOLD,
                  opacity=0.4,
              )
              .move_to(player_card.get_center() + DOWN * scale_factor)
          )

          controls = VGroup(prev_btn, play_btn, next_btn, song_title)
          return VGroup(player_card, another, controls)

        scale_f = 0.35
        positions = [UP * 2.2 + LEFT * 3.8,UP * 2.2 + ORIGIN,UP * 2.2 + RIGHT * 3.8,DOWN * 2.2 + LEFT * 3.8,DOWN * 2.2+ ORIGIN,DOWN * 2.2 + RIGHT * 3.8,]

        cards = VGroup(
            *[make_player(scale_f, BLUE, f"Track {i+1}" if i != 4 else "Track 1", pos)
                for i, pos in enumerate(positions)])

        self.play(FadeIn(cards), run_time=1.2)
        self.wait(0.8)
        target_card = cards[4]
        other_cards = VGroup(*[cards[i] for i in range(6) if i != 4])
        self.play(
            FadeOut(other_cards),
            target_card.animate.scale(1 / scale_f).move_to(ORIGIN),
            run_time=1.5,
        )
        self.wait(3)

class IntroText(Scene):
    def construct(self):
        text1=Text("Listas Circularmente Enlazadas", color=BLUE_A)
        self.play(Write(text1))
        self.wait(4)
        self.play(text1.animate.shift(UP))
        textCS=Text("- Listas Circulares simplemente enlazadas", color=BLUE_B, font_size=24)
        textCD = Text("- Listas Circulares doblemente enlazadas", color=BLUE_B, font_size=24)
        textCS.move_to(ORIGIN)
        textCD.move_to(ORIGIN+DOWN*0.5)

        self.play(FadeIn(textCS), FadeIn(textCD))
        self.wait(5)
        self.play(textCS.animate.set_fill(YELLOW_B),textCD.animate.set_fill(BLUE_D), run_time=1.5)
        self.wait(5)
        self.play(textCS.animate.set_fill(BLUE_D), textCD.animate.set_fill(YELLOW_B),run_time = 1.5)
        self.wait(5)
        self.play(textCS.animate.set_fill(BLUE_B), textCD.animate.set_fill(BLUE_B), run_time=1.5)
        self.wait(5)
        self.play(FadeOut(textCD), FadeOut(textCS))


class Credits(Scene):

    def construct(self):

        pellets = VGroup(*[Dot(radius=0.08, color=BLUE_B).shift(RIGHT * x)for x in range(-5, 6)])
        self.play(FadeIn(pellets, shift=UP * 0.2))

        pacman_sector = Sector(radius=0.5, start_angle=PI / 4, angle=1.5 * PI, color=YELLOW_E, fill_opacity=1)
        pacman_eye = Dot(radius=0.07, color=BLACK).move_to(pacman_sector.get_center() + UP * 0.25 + RIGHT * 0.05)
        pacman = VGroup(pacman_sector, pacman_eye).move_to(LEFT*6)



        box = Rectangle(height=9, width=13, color=BLACK, fill_opacity=1, fill_color=BLACK)

        box_text = Text("Elaborado por:", font_size=16, color=YELLOW).move_to(
            box.get_top() + DOWN*2
        )

        box_text1 = Text("Ary Sanchez", font_size=16, color=YELLOW).move_to(
            box.get_top()+DOWN*3
        )
        box_text2 = Text("Sebastián Falvy", font_size=16, color=YELLOW).move_to(
            box.get_top() + DOWN * 4
        )
        box_text3 = Text("Alba Cabrera", font_size=16, color=YELLOW).move_to(
            box.get_top() + DOWN*5
        )

        cover_box = VGroup(box,box_text, box_text1, box_text2, box_text3)
        cover_box.move_to(pacman.get_center())

        cover_box.add_updater(lambda m: m.move_to(pacman.get_center()+LEFT*6))

        self.play(FadeIn(cover_box), FadeIn(pacman))

        self.play(
            pacman.animate.shift(RIGHT * 12), run_time=4, rate_func=linear
        )

        cover_box.clear_updaters()

        self.play(
            FadeOut(pacman),
            FadeOut(pellets),
        )
        self.play(FadeOut(cover_box))
        self.wait(10)
        self.play(FadeOut(box_text))

class PacmanChomp(Scene):

    def construct(self):

        mouth_angle = ValueTracker(0.8)
        pacman = always_redraw(
            lambda: Sector(
                radius=1.2,
                start_angle=mouth_angle.get_value() / 2,
                angle=TAU - mouth_angle.get_value(),
                color=YELLOW_E,
                fill_opacity=1,
            )
        )
        eye = Dot(radius=0.12, color=BLACK).move_to(
            pacman.get_center() + UP * 0.5 + RIGHT * 0.1
        )
        pacman_group = VGroup(pacman, eye)
        self.play(FadeIn(pacman_group))

        for _ in range(3):
          self.play(
              mouth_angle.animate.set_value(0.05),
              run_time=0.3,
              rate_func=linear,
          )
          self.play(
              mouth_angle.animate.set_value(0.9),
              run_time=0.3,
              rate_func=linear,
          )

        self.wait(1)

        self.play(FadeOut(pacman_group))



class ExtraText(Scene):
    def construct(self):
        text1=Text("Inserción al inicio: O(1)", font_size=25, color=YELLOW).move_to(ORIGIN+DOWN*0.2)
        self.play(Write(text1))
        self.wait(4)



class VeryExtraText(Scene):
    def construct(self):
        texttitle=Text("Aprendiendo sobre estructuras de datos", font_size=25, color=YELLOW).move_to(ORIGIN)
        self.play(Write(texttitle))
        self.wait(4)

