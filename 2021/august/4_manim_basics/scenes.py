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
        # Animate Fade Out of the star
        self.play(FadeOut(star))
        self.wait(0.5)
        # Do the same for the circle
        self.play(FadeIn(circle, run_time=2))
        self.wait()
        self.play(FadeOut(circle))
