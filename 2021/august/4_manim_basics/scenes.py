from manim import *


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
