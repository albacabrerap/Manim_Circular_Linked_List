from manim import *


class CircularLinkedListDemo(Scene):
    def construct(self):
        intro_text = Text("Recordando: Lista Simplemente Enlazada", font_size=26, color=BLUE)
        intro_text.to_edge(UP)
        self.play(Write(intro_text))
        self.wait(1)

        # initial nodes
        n1 = Square(side_length=0.8, color=WHITE).shift(LEFT * 3)
        n2 = Square(side_length=0.8, color=WHITE).shift(LEFT * 1)
        n3 = Square(side_length=0.8, color=WHITE).shift(RIGHT * 1)

        l1 = Text("A", font_size=20).move_to(n1.get_center())
        l2 = Text("B", font_size=20).move_to(n2.get_center())
        l3 = Text("C", font_size=20).move_to(n3.get_center())

        nodes_group = VGroup(n1, n2, n3, l1, l2, l3)
        self.play(Create(nodes_group))
        self.wait(1)

        arr1=Arrow(start=n1.get_right(), end=n2.get_left(), buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.3)
        arr2=Arrow(start=n2.get_right(), end=n3.get_left(), buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.3)
        null_box= Rectangle(width=0.6, height=0.4, color=WHITE).shift(RIGHT * 3.5)
        null_text=Text("NULL", font_size=16).move_to(null_box.get_center())
        null_pointer= VGroup(null_box, null_text)
        arr3 =Arrow(start= n3.get_right(), end=null_pointer.get_left(), buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.3)

        head_label = Text("HEAD", font_size=18, color= YELLOW).next_to(n1, UP, buff=0.3)
        tail_label = Text("TAIL", font_size=18, color=YELLOW).next_to(n3, UP, buff=0.3)

        self.play(GrowArrow(arr1), GrowArrow(arr2), FadeIn(head_label), FadeIn(tail_label))
        self.play(GrowArrow(arr3), Create(null_pointer))
        self.wait(1)

        circ_text = Text("Circular Singly: Todos los nodos tienen un next válido", font_size=22, color=GREEN)
        circ_text.to_edge(UP)
        self.play(Transform(intro_text, circ_text))
        self.wait(2)

        self.play(FadeOut(null_pointer), FadeOut(arr3))
        self.wait(1)

        n3_r = n3.get_right()
        n1_l = n1.get_left()
        n1_b = n1.get_bottom()

        circular_arrow = VGroup(
            Line(start=n3_r, end=n3_r + RIGHT * 0.4, color=GREEN),
            Line(start=n3_r + RIGHT * 0.4, end=[n3_r[0] + 0.4, n1_b[1] - 0.5, 0], color=GREEN),
            Line(start=[n3_r[0] + 0.4, n1_b[1] - 0.5, 0], end=[n1_l[0] - 0.4, n1_b[1] - 0.5, 0], color=GREEN),
            Line(start=[n1_l[0] - 0.4, n1_b[1] - 0.5, 0], end=[n1_l[0] - 0.4, n1_l[1], 0], color=GREEN),
            Arrow(start=[n1_l[0] - 0.4, n1_l[1], 0], end=n1_l, stroke_width=2.5,
                  max_tip_length_to_length_ratio=0.7, color=GREEN)
        )
        self.play(Create(circular_arrow))
        self.wait(2)

        self.play(
            FadeOut(nodes_group), FadeOut(arr1), FadeOut(arr2), FadeOut(circular_arrow),
            FadeOut(head_label), FadeOut(tail_label), FadeOut(intro_text)
        )
        self.wait(3)

        op_title = Text("Circular Singly: Inserción y Eliminación", font_size=24, color=BLUE)
        op_title.to_edge(UP)
        self.play(Write(op_title))

        # primer nodo
        node1_s1 = Square(side_length=0.8, color=WHITE).move_to(ORIGIN)
        label1_s1 = Text("10", font_size=20).move_to(node1_s1.get_center())
        group_s1 = VGroup(node1_s1, label1_s1)
        lbl_s1 = Text("HEAD/TAIL", font_size=16, color=YELLOW).next_to(group_s1, UP, buff=0.3)
        loop_s1 = CurvedArrow(node1_s1.get_top() + LEFT * 0.2, node1_s1.get_top() + RIGHT * 0.2, angle=-TAU / 1.2,
                              color=YELLOW)

        self.play(Create(group_s1), FadeIn(lbl_s1), Create(loop_s1))
        self.wait(1)

        # segundo nodo
        ins_note = Text("Insertar nodos al final actualiza las referencias", font_size=18, color=GREEN)
        ins_note.to_edge(DOWN)
        self.play(FadeIn(ins_note))
        self.wait(0.6)

        node1_s2 = Square(side_length=0.8, color=WHITE).move_to(LEFT * 1.5)
        label1_s2 = Text("10", font_size=20).move_to(node1_s2.get_center())
        g1_s2 = VGroup(node1_s2, label1_s2)

        node2_s2 = Square(side_length=0.8, color=WHITE).move_to(RIGHT * 1.5)
        label2_s2 = Text("20", font_size=20).move_to(node2_s2.get_center())
        g2_s2 = VGroup(node2_s2, label2_s2)

        h_s2 = Text("HEAD", font_size=16, color=YELLOW).next_to(g1_s2, UP, buff=0.3)
        t_s2 = Text("TAIL", font_size=16, color=YELLOW).next_to(g2_s2, UP, buff=0.3)
        arr_12_s2 = Arrow(start=g1_s2.get_right(), end=g2_s2.get_left(), buff=0.1, color=GREEN, stroke_width=3, max_tip_length_to_length_ratio=0.3)

        r2_s2 = g2_s2.get_right()
        l1_s2 = g1_s2.get_left()
        b1_s2 = g1_s2.get_bottom()
        circ_s2 = VGroup(
            Line(start=r2_s2, end=r2_s2 + RIGHT * 0.3, color=GREEN),
            Line(start=r2_s2 + RIGHT * 0.3, end=[r2_s2[0] + 0.3, b1_s2[1] - 0.4, 0], color=GREEN),
            Line(start=[r2_s2[0] + 0.3, b1_s2[1] - 0.4, 0], end=[l1_s2[0] - 0.3, b1_s2[1] - 0.4, 0], color=GREEN),
            Line(start=[l1_s2[0] - 0.3, b1_s2[1] - 0.4, 0], end=[l1_s2[0] - 0.3, l1_s2[1], 0], color=GREEN),
            Arrow(start=[l1_s2[0] - 0.3, l1_s2[1], 0], end=l1_s2, stroke_width=2.5, max_tip_length_to_length_ratio=0.7,
                  color=GREEN)
        )

        self.play(
            ReplacementTransform(group_s1, g1_s2),
            FadeOut(lbl_s1), FadeOut(loop_s1),
            Create(g2_s2), FadeIn(h_s2), FadeIn(t_s2),
            GrowArrow(arr_12_s2), Create(circ_s2)
        )
        self.wait(2)

        # tercer nodo
        node1_s3 = Square(side_length=0.8, color=WHITE).move_to(LEFT * 2.5)
        label1_s3 = Text("10", font_size=20).move_to(node1_s3.get_center())
        g1_s3 = VGroup(node1_s3, label1_s3)

        node2_s3 = Square(side_length=0.8, color=WHITE).move_to(ORIGIN)
        label2_s3 = Text("20", font_size=20).move_to(node2_s3.get_center())
        g2_s3 = VGroup(node2_s3, label2_s3)

        node3_s3 = Square(side_length=0.8, color=WHITE).move_to(RIGHT * 2.5)
        label3_s3 = Text("30", font_size=20).move_to(node3_s3.get_center())
        g3_s3 = VGroup(node3_s3, label3_s3)

        h_s3 = Text("HEAD", font_size=16, color=YELLOW).next_to(g1_s3, UP, buff=0.3)
        t_s3 = Text("TAIL", font_size=16, color=YELLOW).next_to(g3_s3, UP, buff=0.3)
        arr_12_s3 = Arrow(start=g1_s3.get_right(), end=g2_s3.get_left(), buff=0.1, color=GREEN, stroke_width=3, max_tip_length_to_length_ratio=0.3)
        arr_23_s3 = Arrow(start=g2_s3.get_right(), end=g3_s3.get_left(), buff=0.1, color=GREEN, stroke_width=3, max_tip_length_to_length_ratio=0.3)

        r3_s3 = g3_s3.get_right()
        l1_s3 = g1_s3.get_left()
        b1_s3 = g1_s3.get_bottom()
        circ_s3 = VGroup(
            Line(start=r3_s3, end=r3_s3 + RIGHT * 0.3, color=GREEN),
            Line(start=r3_s3 + RIGHT * 0.3, end=[r3_s3[0] + 0.3, b1_s3[1] - 0.4, 0], color=GREEN),
            Line(start=[r3_s3[0] + 0.3, b1_s3[1] - 0.4, 0], end=[l1_s3[0] - 0.3, b1_s3[1] - 0.4, 0], color=GREEN),
            Line(start=[l1_s3[0] - 0.3, b1_s3[1] - 0.4, 0], end=[l1_s3[0] - 0.3, l1_s3[1], 0], color=GREEN),
            Arrow(start=[l1_s3[0] - 0.3, l1_s3[1], 0], end=l1_s3, stroke_width=2.5, max_tip_length_to_length_ratio=0.7,
                  color=GREEN)
        )

        self.play(
            ReplacementTransform(g1_s2, g1_s3),
            ReplacementTransform(g2_s2, g2_s3),
            FadeOut(h_s2), FadeOut(t_s2), FadeOut(arr_12_s2), FadeOut(circ_s2),
            Create(g3_s3), FadeIn(h_s3), FadeIn(t_s3),
            GrowArrow(arr_12_s3), GrowArrow(arr_23_s3), Create(circ_s3)
        )
        self.wait(2)

        # eliminar head
        self.play(FadeOut(ins_note))
        del_note = Text("Eliminar al inicio: HEAD avanza, TAIL redirige al nuevo HEAD", font_size=18, color=RED)
        del_note.to_edge(DOWN)
        self.play(FadeIn(del_note))
        self.wait(2)

        node2_s4 = Square(side_length=0.8, color=WHITE).move_to(LEFT * 1.5)
        label2_s4 = Text("20", font_size=20).move_to(node2_s4.get_center())
        g2_s4 = VGroup(node2_s4, label2_s4)

        node3_s4 = Square(side_length=0.8, color=WHITE).move_to(RIGHT * 1.5)
        label3_s4 = Text("30", font_size=20).move_to(node3_s4.get_center())
        g3_s4 = VGroup(node3_s4, label3_s4)

        h_s4 = Text("HEAD", font_size=16, color=YELLOW).next_to(g2_s4, UP, buff=0.3)
        t_s4 = Text("TAIL", font_size=16, color=YELLOW).next_to(g3_s4, UP, buff=0.3)
        arr_23_s4 = Arrow(start=g2_s4.get_right(), end=g3_s4.get_left(), buff=0.1, color=GREEN, stroke_width=3, max_tip_length_to_length_ratio=0.3)

        r3_s4 = g3_s4.get_right()
        l2_s4 = g2_s4.get_left()
        b2_s4 = g2_s4.get_bottom()
        circ_s4 = VGroup(
            Line(start=r3_s4, end=r3_s4 + RIGHT * 0.3, color=GREEN),
            Line(start=r3_s4 + RIGHT * 0.3, end=[r3_s4[0] + 0.3, b2_s4[1] - 0.4, 0], color=GREEN),
            Line(start=[r3_s4[0] + 0.3, b2_s4[1] - 0.4, 0], end=[l2_s4[0] - 0.3, b2_s4[1] - 0.4, 0], color=GREEN),
            Line(start=[l2_s4[0] - 0.3, b2_s4[1] - 0.4, 0], end=[l2_s4[0] - 0.3, l2_s4[1], 0], color=GREEN),
            Arrow(start=[l2_s4[0] - 0.3, l2_s4[1], 0], end=l2_s4, stroke_width=2.5, max_tip_length_to_length_ratio=0.7,
                  color=GREEN)
        )

        self.play(
            FadeOut(g1_s3), FadeOut(h_s3), FadeOut(arr_12_s3), FadeOut(circ_s3),
            ReplacementTransform(g2_s3, g2_s4),
            ReplacementTransform(g3_s3, g3_s4),
            FadeOut(t_s3), FadeOut(arr_23_s3),
            FadeIn(h_s4), FadeIn(t_s4),
            GrowArrow(arr_23_s4), Create(circ_s4)
        )
        self.wait(2.5)

        self.play(
            FadeOut(g2_s4), FadeOut(g3_s4), FadeOut(h_s4), FadeOut(t_s4),
            FadeOut(arr_23_s4), FadeOut(circ_s4), FadeOut(op_title), FadeOut(del_note)
        )
        self.wait(1)