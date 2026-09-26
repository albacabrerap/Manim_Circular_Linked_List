from manim import *


class CircularLinkedListDemo(Scene):
    def construct(self):
        intro_text = Text("Recordando: Lista Simplemente Enlazada", font_size=26, color=BLUE)
        self.play(Write(intro_text))
        self.play(intro_text.animate.to_edge(UP))

        # initial nodes
        n1 = Square(side_length=0.8, fill_opacity=0.2).shift(LEFT * 3)
        n2 = Square(side_length=0.8, fill_opacity=0.2).shift(LEFT * 1)
        n3 = Square(side_length=0.8, fill_opacity=0.2).shift(RIGHT * 1)

        l1 = Text("A", font_size=20).move_to(n1.get_center())
        l2 = Text("B", font_size=20).move_to(n2.get_center())
        l3 = Text("C", font_size=20).move_to(n3.get_center())

        nodes_group = VGroup(n1, n2, n3, l1, l2, l3)
        self.play(Create(nodes_group), runtime=3)
        self.wait(1.5)

        som_text = Text("Nodos que tienen un valor y apuntan al nodo siguiente", font_size=22, color=YELLOW)
        som_text.to_edge(DOWN*2)
        self.play(Write(som_text))
        self.wait(1)

        arr1=Arrow(start=n1.get_right(), end=n2.get_left(), buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.3)
        arr2=Arrow(start=n2.get_right(), end=n3.get_left(), buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.3)
        null_box= Rectangle(width=0.6, height=0.4, fill_opacity=0, stroke_opacity=0, background_stroke_opacity=0).shift(RIGHT * 3.5)
        null_text=Text("NULL", font_size=16, color=RED).move_to(null_box.get_center())
        null_pointer= VGroup(null_box, null_text)
        arr3 =Arrow(start= n3.get_right(), end=null_pointer.get_left(), buff=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.3)

        head_label = Text("HEAD", font_size=18, color= YELLOW).next_to(n1, UP, buff=0.3)
        tail_label = Text("TAIL", font_size=18, color=YELLOW).next_to(n3, UP, buff=0.3)

        ot_text=Text("El último nodo apunta a null",font_size=22, color=YELLOW)
        ot_text.to_edge(DOWN)


        self.play(GrowArrow(arr1), GrowArrow(arr2), FadeIn(head_label), FadeIn(tail_label),FadeIn(ot_text),runtime=1.5)
        self.play(GrowArrow(arr3), Create(null_pointer), runtime=1.5)
        self.play(FadeOut(som_text))
        self.wait(1.5)

        circ_text = Text("Circular Singly: Todos los nodos tienen un next válido", font_size=22, color=GREEN)
        circ_text.to_edge(UP)


        self.play(FadeOut(null_pointer), FadeOut(arr3), FadeOut(ot_text), Transform(intro_text, circ_text), runtime=3)

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
        self.wait(2.5)

        self.play(
            FadeOut(nodes_group), FadeOut(arr1), FadeOut(arr2), FadeOut(circular_arrow),
            FadeOut(head_label), FadeOut(tail_label), FadeOut(intro_text)
        )
        self.wait(1.5)

        op_title = Text("Circular Singly: Inserción y Eliminación", font_size=24, color=BLUE)
        op_title.to_edge(UP)
        self.play(Write(op_title))

        # primer nodo
        first=Text("El primer nodo es la cabeza, y apunta a sí mismo", font_size=18, color=GREEN)
        first.to_edge(DOWN)

        node1_s1 = Square(side_length=0.8, fill_opacity=0.2).move_to(ORIGIN)
        label1_s1 = Text("10", font_size=20).move_to(node1_s1.get_center())
        group_s1 = VGroup(node1_s1, label1_s1)
        lbl_s1 = Text("HEAD/TAIL", font_size=16, color=YELLOW).next_to(group_s1, UP, buff=0.3)
        loop_s1 = CurvedArrow(node1_s1.get_top() + LEFT * 0.2, node1_s1.get_top() + RIGHT * 0.2, angle=-TAU / 1.2,
                              color=YELLOW)

        self.play(FadeIn(first), FadeIn(node1_s1))
        self.wait(1.5)
        self.play(Create(group_s1), FadeIn(lbl_s1), Create(loop_s1))
        self.wait(1.5)

        # segundo nodo (Inserción al inicio)
        ins_note = Text("Al insertar al inicio, el nuevo nodo se vuelve la cabeza y apunta al anterior", font_size=18,
                        color=GREEN)
        ins_note.to_edge(DOWN)
        self.play(FadeOut(first), FadeIn(ins_note))
        self.wait(1)

        node2_s2 = Square(side_length=0.8, fill_opacity=0.2).move_to(LEFT * 1.5)
        label2_s2 = Text("20", font_size=20).move_to(node2_s2.get_center())
        g2_s2 = VGroup(node2_s2, label2_s2)

        node1_s2 = Square(side_length=0.8, fill_opacity=0.2).move_to(RIGHT * 1.5)
        label1_s2 = Text("10", font_size=20).move_to(node1_s2.get_center())
        g1_s2 = VGroup(node1_s2, label1_s2)

        h_s2 = Text("HEAD", font_size=16, color=YELLOW).next_to(g2_s2, UP, buff=0.3)
        t_s2 = Text("TAIL", font_size=16, color=YELLOW).next_to(g1_s2, UP, buff=0.3)

        arr_21_s2 = Arrow(start=g2_s2.get_right(), end=g1_s2.get_left(), buff=0.1, color=GREEN, stroke_width=3,
                          max_tip_length_to_length_ratio=0.3)

        r1_s2 = g1_s2.get_right()
        l2_s2 = g2_s2.get_left()
        b2_s2 = g2_s2.get_bottom()
        circ_s2 = VGroup(
            Line(start=r1_s2, end=r1_s2 + RIGHT * 0.3, color=GREEN),
            Line(start=r1_s2 + RIGHT * 0.3, end=[r1_s2[0] + 0.3, b2_s2[1] - 0.4, 0], color=GREEN),
            Line(start=[r1_s2[0] + 0.3, b2_s2[1] - 0.4, 0], end=[l2_s2[0] - 0.3, b2_s2[1] - 0.4, 0], color=GREEN),
            Line(start=[l2_s2[0] - 0.3, b2_s2[1] - 0.4, 0], end=[l2_s2[0] - 0.3, l2_s2[1], 0], color=GREEN),
            Arrow(start=[l2_s2[0] - 0.3, l2_s2[1], 0], end=l2_s2, stroke_width=2.5, max_tip_length_to_length_ratio=0.7,
                  color=GREEN)
        )

        self.play(
            ReplacementTransform(group_s1, g1_s2),
            FadeOut(lbl_s1), FadeOut(loop_s1),
            Create(g2_s2), FadeIn(h_s2), FadeIn(t_s2),
            GrowArrow(arr_21_s2), Create(circ_s2), run_time=3)
        self.wait(2)

        # tercer nodo
        node1_s3 = Square(side_length=0.8, fill_opacity=0.2).move_to(LEFT * 2.5)
        label1_s3 = Text("10", font_size=20).move_to(node1_s3.get_center())
        g1_s3 = VGroup(node1_s3, label1_s3)

        node2_s3 = Square(side_length=0.8, fill_opacity=0.2).move_to(ORIGIN)
        label2_s3 = Text("20", font_size=20).move_to(node2_s3.get_center())
        g2_s3 = VGroup(node2_s3, label2_s3)

        node3_s3 = Square(side_length=0.8, fill_opacity=0.2).move_to(RIGHT * 2.5)
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
            FadeOut(h_s2), FadeOut(t_s2), FadeOut(arr_21_s2), FadeOut(circ_s2),
            Create(g3_s3), FadeIn(h_s3), FadeIn(t_s3),
            GrowArrow(arr_12_s3), GrowArrow(arr_23_s3), Create(circ_s3), run_time=4.5
        )
        self.wait(2)
        self.play(FadeOut(ins_note))

        # eliminar head
        del_note = Text("Eliminar al inicio: HEAD avanza, TAIL apunta al nuevo HEAD", font_size=18, color=RED)
        del_note.to_edge(DOWN)
        self.play(FadeIn(del_note))
        self.wait(1.5)

        self.play(node1_s3.animate.set_color(RED))
        self.wait(0.5)

        node2_s4 = Square(side_length=0.8, fill_opacity=0.2).move_to(LEFT * 1.5)
        label2_s4 = Text("20", font_size=20).move_to(node2_s4.get_center())
        g2_s4 = VGroup(node2_s4, label2_s4)

        node3_s4 = Square(side_length=0.8, fill_opacity=0.2).move_to(RIGHT * 1.5)
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
            GrowArrow(arr_23_s4), Create(circ_s4), run_time=5
        )
        self.wait(2.5)

        self.play(
            FadeOut(g2_s4), FadeOut(g3_s4), FadeOut(h_s4), FadeOut(t_s4),
            FadeOut(arr_23_s4), FadeOut(circ_s4), FadeOut(op_title), FadeOut(del_note)
        )
        self.wait(1)

        limit_text1 = Text("¿Para retroceder, eliminar al final o insertar en medio?", font_size=22, color=YELLOW)
        self.play(Write(limit_text1))
        self.wait(2)
        self.play(limit_text1.animate.shift(DOWN))

        n_demo1 = Square(side_length=0.8, fill_opacity=0.2).shift(LEFT * 2)
        n_demo2 = Square(side_length=0.8, fill_opacity=0.2).shift(RIGHT * 2)
        d_l1 = Text("A", font_size=20).move_to(n_demo1.get_center())
        d_l2 = Text("B", font_size=20).move_to(n_demo2.get_center())
        demo_nodes = VGroup(n_demo1, n_demo2, d_l1, d_l2)

        f_arr = Arrow(start=n_demo1.get_right(), end=n_demo2.get_left(), buff=0.1)
        self.play(Create(demo_nodes), GrowArrow(f_arr))
        self.wait(1)

        q_arrow = Arrow(start=n_demo2.get_left() + DOWN * 0.2, end=n_demo1.get_right() + DOWN * 0.2, color=RED,
                        buff=0.1)
        q_mark = Text("?", font_size=24, color=RED).next_to(q_arrow, DOWN, buff=0.1)

        limit_text = Text("Necesitamos el nodo anterior", font_size=22, color=YELLOW).shift(DOWN*1.5)
        self.play(Write(limit_text),GrowArrow(q_arrow), FadeIn(q_mark))
        self.wait(2)

        solution_text = Text("Solución: Enlaces dobles", font_size=24, color=GREEN)
        solution_text.to_edge(UP)
        self.play(FadeOut(limit_text1),Transform(limit_text, solution_text))

        b_arr = Arrow(start=n_demo2.get_left() + DOWN * 0.2, end=n_demo1.get_right() + DOWN * 0.2, color=GREEN,
                      buff=0.1)
        self.play(Transform(q_arrow, b_arr), FadeOut(q_mark))
        self.wait(2)

        self.play(
            FadeOut(limit_text),
            FadeOut(solution_text),
            FadeOut(demo_nodes),
            FadeOut(f_arr),
            FadeOut(q_arrow)
        )
        self.wait(1.5)

        doubly_title = Text("Circular Doubly: Inserción y Eliminación", font_size=24, color=GREEN)
        doubly_title.to_edge(UP)
        self.play(Write(doubly_title))
        self.wait(2)

        first = Text("El primer nodo es la cabeza, y apunta a sí mismo en ambas direcciones", font_size=18, color=GREEN)
        first.to_edge(DOWN)

        # primer nodo
        dn1_s1 = Square(side_length=0.8, fill_opacity=0.2).move_to(ORIGIN)
        dnl1_s1 = Text("10", font_size=20).move_to(dn1_s1.get_center())
        dg1_s1 = VGroup(dn1_s1, dnl1_s1)
        dlbl_s1 = Text("HEAD/TAIL", font_size=14, color=YELLOW).next_to(dg1_s1, UP, buff=0.3)

        d_loop_f = CurvedArrow(dn1_s1.get_top() + LEFT * 0.15, dn1_s1.get_top() + RIGHT * 0.15, angle=-TAU,
                               color=GREEN)
        d_loop_b = CurvedArrow(dn1_s1.get_bottom() + RIGHT * 0.15, dn1_s1.get_bottom() + LEFT * 0.15, angle=-TAU,
                               color=RED)

        self.play(Write(first),Create(dg1_s1), FadeIn(dlbl_s1), Create(d_loop_f), Create(d_loop_b), runtime=5)
        self.wait(3)

        # segundo nodo
        ins_d_note = Text("Para añadir un segundo nodo, la cabeza apunta al nodo insertado en ambas direcciones,", font_size=18, color=GREEN)
        ins_d_note2= Text(" y el nodo insertado apunta a la cabeza en ambas direcciones", font_size=18, color=GREEN)
        ins_d_note.to_edge(DOWN*2)
        ins_d_note2.to_edge(DOWN)
        self.play(FadeOut(first))
        self.play(FadeIn(ins_d_note), FadeIn(ins_d_note2))
        self.wait(1.5)

        dn1_s2 = Square(side_length=0.8, fill_opacity=0.2).move_to(LEFT * 1.5)
        dnl1_s2 = Text("10", font_size=20).move_to(dn1_s2.get_center())
        dg1_s2 = VGroup(dn1_s2, dnl1_s2)

        dn2_s2 = Square(side_length=0.8, fill_opacity=0.2).move_to(RIGHT * 1.5)
        dnl2_s2 = Text("20", font_size=20).move_to(dn2_s2.get_center())
        dg2_s2 = VGroup(dn2_s2, dnl2_s2)

        dlbl_h2 = Text("HEAD", font_size=14, color=YELLOW).next_to(dg1_s2, UP, buff=0.3)
        dlbl_t2 = Text("TAIL", font_size=14, color=YELLOW).next_to(dg2_s2, UP, buff=0.3)

        df_12 = Arrow(start=dg1_s2.get_right() + UP * 0.15, end=dg2_s2.get_left() + UP * 0.15, buff=0.1, color=GREEN)
        db_21 = Arrow(start=dg2_s2.get_left() + DOWN * 0.15, end=dg1_s2.get_right() + DOWN * 0.15, buff=0.1, color=RED)

        r2_2 = dg2_s2.get_right()
        l1_2 = dg1_s2.get_left()
        t_2 = dg1_s2.get_top()[1] + 0.5
        b_2 = dg1_s2.get_bottom()[1] - 0.5

        wrap_f2 = VGroup(
            Line(start=r2_2, end=[r2_2[0] + 0.3, r2_2[1], 0], color=GREEN),
            Line(start=[r2_2[0] + 0.3, r2_2[1], 0], end=[r2_2[0] + 0.3, t_2, 0], color=GREEN),
            Line(start=[r2_2[0] + 0.3, t_2, 0], end=[l1_2[0] - 0.3, t_2, 0], color=GREEN),
            Line(start=[l1_2[0] - 0.3, t_2, 0], end=[l1_2[0] - 0.3, l1_2[1], 0], color=GREEN),
            Arrow(start=[l1_2[0] - 0.3, l1_2[1], 0], end=l1_2, stroke_width=2.5, max_tip_length_to_length_ratio=0.7,
                  color=GREEN)
        )
        wrap_b2 = VGroup(
            Line(start=l1_2, end=[l1_2[0] - 0.3, l1_2[1], 0], color=RED),
            Line(start=[l1_2[0] - 0.3, l1_2[1], 0], end=[l1_2[0] - 0.3, b_2, 0], color=RED),
            Line(start=[l1_2[0] - 0.3, b_2, 0], end=[r2_2[0] + 0.3, b_2, 0], color=RED),
            Line(start=[r2_2[0] + 0.3, b_2, 0], end=[r2_2[0] + 0.3, r2_2[1], 0], color=RED),
            Arrow(start=[r2_2[0] + 0.3, r2_2[1], 0], end=r2_2, stroke_width=2.5, max_tip_length_to_length_ratio=0.7,
                  color=RED)
        )

        self.play(FadeOut(ins_d_note), FadeOut(ins_d_note2))
        self.play(
            ReplacementTransform(dg1_s1, dg1_s2),
            FadeOut(dlbl_s1), FadeOut(d_loop_f), FadeOut(d_loop_b),
            Create(dg2_s2), FadeIn(dlbl_h2), FadeIn(dlbl_t2),
            GrowArrow(df_12), GrowArrow(db_21), Create(wrap_f2), Create(wrap_b2), runtime=4
        )
        self.wait(3)


        ins_d_note3 = Text("Para añadir un siguiente nodo, la cola apunta al nodo insertado,", font_size=18, color=GREEN)
        ins_d_note4 = Text("la nueva cola apunta a la cola anterior y a la cabeza", font_size=18, color=GREEN)
        ins_d_note3.to_edge(DOWN * 2)
        ins_d_note4.to_edge(DOWN)

        self.play(FadeIn(ins_d_note3), FadeIn(ins_d_note4))
        self.wait(2.5)

        dn1_s3 = Square(side_length=0.8, fill_opacity=0.2).move_to(LEFT * 2.5)
        dnl1_s3 = Text("10", font_size=20).move_to(dn1_s3.get_center())
        dg1_s3 = VGroup(dn1_s3, dnl1_s3)

        dn2_s3 = Square(side_length=0.8, fill_opacity=0.2).move_to(ORIGIN)
        dnl2_s3 = Text("20", font_size=20).move_to(dn2_s3.get_center())
        dg2_s3 = VGroup(dn2_s3, dnl2_s3)

        dn3_s3 = Square(side_length=0.8, fill_opacity=0.2).move_to(RIGHT * 2.5)
        dnl3_s3 = Text("30", font_size=20).move_to(dn3_s3.get_center())
        dg3_s3 = VGroup(dn3_s3, dnl3_s3)

        dlbl_h3 = Text("HEAD", font_size=14, color=YELLOW).next_to(dg1_s3, UP, buff=0.3)
        dlbl_t3 = Text("TAIL", font_size=14, color=YELLOW).next_to(dg3_s3, UP, buff=0.3)

        df_12_3 = Arrow(start=dg1_s3.get_right() + UP * 0.15, end=dg2_s3.get_left() + UP * 0.15, buff=0.1, color=GREEN)
        db_21_3 = Arrow(start=dg2_s3.get_left() + DOWN * 0.15, end=dg1_s3.get_right() + DOWN * 0.15, buff=0.1,
                        color=RED)
        df_23_3 = Arrow(start=dg2_s3.get_right() + UP * 0.15, end=dg3_s3.get_left() + UP * 0.15, buff=0.1, color=GREEN)
        db_32_3 = Arrow(start=dg3_s3.get_left() + DOWN * 0.15, end=dg2_s3.get_right() + DOWN * 0.15, buff=0.1,
                        color=RED)

        r3_3 = dg3_s3.get_right()
        l1_3 = dg1_s3.get_left()
        t_3 = dg1_s3.get_top()[1] + 0.5
        b_3 = dg1_s3.get_bottom()[1] - 0.5

        wrap_f3 = VGroup(
            Line(start=r3_3, end=[r3_3[0] + 0.3, r3_3[1], 0], color=GREEN),
            Line(start=[r3_3[0] + 0.3, r3_3[1], 0], end=[r3_3[0] + 0.3, t_3, 0], color=GREEN),
            Line(start=[r3_3[0] + 0.3, t_3, 0], end=[l1_3[0] - 0.3, t_3, 0], color=GREEN),
            Line(start=[l1_3[0] - 0.3, t_3, 0], end=[l1_3[0] - 0.3, l1_3[1], 0], color=GREEN),
            Arrow(start=[l1_3[0] - 0.3, l1_3[1], 0], end=l1_3, stroke_width=2.5, max_tip_length_to_length_ratio=0.7,
                  color=GREEN)
        )
        wrap_b3 = VGroup(
            Line(start=l1_3, end=[l1_3[0] - 0.3, l1_3[1], 0], color=RED),
            Line(start=[l1_3[0] - 0.3, l1_3[1], 0], end=[l1_3[0] - 0.3, b_3, 0], color=RED),
            Line(start=[l1_3[0] - 0.3, b_3, 0], end=[r3_3[0] + 0.3, b_3, 0], color=RED),
            Line(start=[r3_3[0] + 0.3, b_3, 0], end=[r3_3[0] + 0.3, r3_3[1], 0], color=RED),
            Arrow(start=[r3_3[0] + 0.3, r3_3[1], 0], end=r3_3, stroke_width=2.5, max_tip_length_to_length_ratio=0.7,
                  color=RED)
        )

        self.play(
            ReplacementTransform(dg1_s2, dg1_s3),
            ReplacementTransform(dg2_s2, dg2_s3),
            FadeOut(dlbl_h2), FadeOut(dlbl_t2), FadeOut(df_12), FadeOut(db_21), FadeOut(wrap_f2), FadeOut(wrap_b2),
            Create(dg3_s3), FadeIn(dlbl_h3), FadeIn(dlbl_t3),
            GrowArrow(df_12_3), GrowArrow(db_21_3), GrowArrow(df_23_3), GrowArrow(db_32_3),
            Create(wrap_f3), Create(wrap_b3), runtime=5
        )
        self.wait(2.5)
        self.play(FadeOut(ins_d_note3), FadeOut(ins_d_note4))
        self.wait(1.5)

        # eliminar un nodo

        del_mid_note = Text("Eliminar un nodo (20): Se conoce la posicion del nodo,", font_size=18, color=RED)
        del_mid_note2= Text("también se conoce el anterior y el siguiente,", font_size=18, color=RED)
        del_mid_note3=Text("entonces se enlazan directamente y se elimina el nodo", font_size=18, color=RED)
        del_mid_note.to_edge(DOWN*3)
        del_mid_note2.to_edge(DOWN*2)
        del_mid_note3.to_edge(DOWN)
        del_mid_notes=VGroup(del_mid_note, del_mid_note2, del_mid_note3)

        self.play(FadeIn(del_mid_notes))
        self.wait(1)

        self.play(dn2_s3.animate.set_color(RED))
        self.wait(1)


        dn1_s4 = Square(side_length=0.8, fill_opacity=0.2).move_to(LEFT * 1.5)
        dnl1_s4 = Text("10", font_size=20).move_to(dn1_s4.get_center())
        dg1_s4 = VGroup(dn1_s4, dnl1_s4)

        dn3_s4 = Square(side_length=0.8, fill_opacity=0.2).move_to(RIGHT * 1.5)
        dnl3_s4 = Text("30", font_size=20).move_to(dn3_s4.get_center())
        dg3_s4 = VGroup(dn3_s4, dnl3_s4)

        dlbl_h4 = Text("HEAD", font_size=14, color=YELLOW).next_to(dg1_s4, UP, buff=0.3)
        dlbl_t4 = Text("TAIL", font_size=14, color=YELLOW).next_to(dg3_s4, UP, buff=0.3)

        df_13_4 = Arrow(start=dg1_s4.get_right() + UP * 0.15, end=dg3_s4.get_left() + UP * 0.15, buff=0.1, color=GREEN)
        db_31_4 = Arrow(start=dg3_s4.get_left() + DOWN * 0.15, end=dg1_s4.get_right() + DOWN * 0.15, buff=0.1,
                        color=RED)

        r3_4 = dg3_s4.get_right()
        l1_4 = dg1_s4.get_left()
        t_4 = dg1_s4.get_top()[1] + 0.5
        b_4 = dg1_s4.get_bottom()[1] - 0.5

        wrap_f4 = VGroup(
            Line(start=r3_4, end=[r3_4[0] + 0.3, r3_4[1], 0], color=GREEN),
            Line(start=[r3_4[0] + 0.3, r3_4[1], 0], end=[r3_4[0] + 0.3, t_4, 0], color=GREEN),
            Line(start=[r3_4[0] + 0.3, t_4, 0], end=[l1_4[0] - 0.3, t_4, 0], color=GREEN),
            Line(start=[l1_4[0] - 0.3, t_4, 0], end=[l1_4[0] - 0.3, l1_4[1], 0], color=GREEN),
            Arrow(start=[l1_4[0] - 0.3, l1_4[1], 0], end=l1_4, stroke_width=2.5, max_tip_length_to_length_ratio=0.7,
                  color=GREEN)
        )
        wrap_b4 = VGroup(
            Line(start=l1_4, end=[l1_4[0] - 0.3, l1_4[1], 0], color=RED),
            Line(start=[l1_4[0] - 0.3, l1_4[1], 0], end=[l1_4[0] - 0.3, b_4, 0], color=RED),
            Line(start=[l1_4[0] - 0.3, b_4, 0], end=[r3_4[0] + 0.3, b_4, 0], color=RED),
            Line(start=[r3_4[0] + 0.3, b_4, 0], end=[r3_4[0] + 0.3, r3_4[1], 0], color=RED),
            Arrow(start=[r3_4[0] + 0.3, r3_4[1], 0], end=r3_4, stroke_width=2.5, max_tip_length_to_length_ratio=0.7,
                  color=RED)
        )

        self.play(
            ReplacementTransform(dg1_s3, dg1_s4),
            FadeOut(dg2_s3), FadeOut(dlbl_h3),
            ReplacementTransform(dg3_s3, dg3_s4),
            FadeOut(dlbl_t3), FadeOut(df_12_3), FadeOut(db_21_3), FadeOut(df_23_3), FadeOut(db_32_3), FadeOut(wrap_f3),
            FadeOut(wrap_b3),
            FadeIn(dlbl_h4), FadeIn(dlbl_t4),
            GrowArrow(df_13_4), GrowArrow(db_31_4), Create(wrap_f4), Create(wrap_b4), runtime=10
        )
        self.wait(4)

        self.play(
            FadeOut(doubly_title), FadeOut(del_mid_notes), FadeOut(dg1_s4), FadeOut(dg3_s4),
            FadeOut(dlbl_h4), FadeOut(dlbl_t4), FadeOut(df_13_4), FadeOut(db_31_4),
            FadeOut(wrap_f4), FadeOut(wrap_b4), runtime=5.5
        )
        self.wait(4)

        sum_title = Text("Resumen de Complejidad", font_size=26, color=BLUE)
        sum_title.to_edge(UP)
        self.play(Write(sum_title))
        self.wait(1.5)

        # Left Column: Circular Singly Summary
        s_box = Square(side_length=0.5, color=YELLOW_B, fill_opacity=0.2)
        s_text = Text("CS", font_size=14).move_to(s_box.get_center())
        s_mini = VGroup(s_box, s_text).to_edge(LEFT*1.7, buff=1.5).shift(UP * 1.5)

        s_desc = VGroup(
            Text("• Circular Singly", font_size=18, color=GREEN),
            Text("Ins./Elim. (pos. conocida): O(1)", font_size=14),
            Text("Búsqueda / Recorrido: O(n)", font_size=14),
            Text("Solo dirección siguiente", font_size=14, color=GRAY)
        ).arrange(DOWN, aligned_edge=LEFT*1.7, buff=0.15).next_to(s_mini, DOWN, buff=0.3)

        # Right Column: Circular Doubly Summary
        d_box = Square(side_length=0.5, color=YELLOW_B,fill_opacity=0.2)
        d_text = Text("CD", font_size=14).move_to(d_box.get_center())
        d_mini = VGroup(d_box, d_text).to_edge(RIGHT*1.7, buff=1.5).shift(UP * 1.5)

        d_desc = VGroup(
            Text("• Circular Doubly", font_size=18, color=GREEN),
            Text("Ins./Elim. (pos. conocida): O(1)", font_size=14),
            Text("Búsqueda / Recorrido: O(n)", font_size=14),
            Text("Bidireccional completo", font_size=14, color=GRAY)
        ).arrange(DOWN, aligned_edge=LEFT*1.7, buff=0.15).next_to(d_mini, DOWN, buff=0.3)

        footer_note = Text("* O(1) requiere referencia directa al nodo.", font_size=14, color=GRAY)
        footer_note.to_edge(DOWN)

        self.play(
            Create(s_mini), Write(s_desc),
            Create(d_mini), Write(d_desc),
            FadeIn(footer_note), runtime=10
        )

        self.play(
            FadeOut(sum_title), FadeOut(s_mini), FadeOut(s_desc),
            FadeOut(d_mini), FadeOut(d_desc), FadeOut(footer_note), runtime=4.5
        )
