from manim import *

config.media_width = "50vw"
config.verbosity = "CRITICAL"


class MyFirstAnimation(Scene):
    def construct(self):
        # Create basic mobjects
        star = Star(n=5, fill_color=RED, stroke_color=BLUE)
        circle = Circle(fill_color=DARK_BLUE, fill_opacity=.8, stroke_color=BLUE)

        # Animate Fade in of the star that takes 2 seconds
        self.play(FadeIn(star, run_time=2))
        # Wait for a second
        self.wait()
        # Transform star into a circle
        self.play(Transform(star, circle))
        self.wait(0.5)
        # Remove the circle by fading it out
        self.play(FadeOut(circle))


class ShowCoordinates(Scene):
    def construct(self):
        # place a dot at the origin
        dot = Dot(radius=0.16, color=RED)  # twice the usual size
        # Add the dot to the screen
        self.add(dot)
        # Create 4 different mobjects
        square = Square().shift(2 * LEFT)
        triangle = Triangle().shift(2 * RIGHT)
        circle = Circle().shift(2 * DOWN)
        star = Star(n=7).shift(2 * UP)
        # Add all to the screen
        self.add(square, triangle, circle, star)


class ShowCoords2(Scene):
    def construct(self):
        # place a dot at the origin
        dot = Dot(radius=0.16, color=RED)  # twice the usual size
        # Create 4 different mobjects and animate their shift
        new_locations = [2 * UL, 2 * UR, 2 * DL, 2 * DR]
        mobjects = [Square(), Triangle(), Circle(), Star(n=7)]
        for loc, mob in zip(new_locations, mobjects):
            self.play(mob.animate.shift(loc))

        # Add the dot with Create animation
        self.play(Create(dot))


class AnimateAttribs(Scene):
    def construct(self):
        # Create a simple square
        square = Square(side_length=2)

        # Scale to twice the size
        self.play(square.animate.scale(2))
        # Rotate
        self.play(square.animate.rotate(PI / 3))  # Rotate 60 degrees
        # Change the fill color and opacity
        self.play(square.animate.set_fill(RED, opacity=0.3))


class Graph(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-3.5,
            x_max=3.5,
            y_min=-5,
            y_max=5,
            graph_origin=ORIGIN,
            axes_color=BLUE,
            x_labeled_nums=range(-4, 4, 2),  # x tickers
            y_labeled_nums=range(-5, 5, 2),  # y tickers
            **kwargs
        )

    def construct(self):
        self.setup_axes(animate=False)

        # Draw graphs
        func_graph_cube = self.get_graph(lambda x: x ** 3, RED)
        func_graph_ncube = self.get_graph(lambda x: -x ** 3, GREEN)

        # Create labels
        graph_lab = self.get_graph_label(func_graph_cube, label="x^3")
        graph_lab2 = self.get_graph_label(func_graph_ncube, label="-x^3", x_val=-3)

        # Create a vertical line
        vert_line = self.get_vertical_line_to_graph(1.5, func_graph_cube, color=YELLOW)
        label_coord = self.input_to_graph_point(1.5, func_graph_cube)
        text = MathTex(r"x=1.5")
        text.next_to(label_coord)

        self.add(func_graph_cube, func_graph_ncube, graph_lab, graph_lab2, vert_line, text)
        self.wait()
