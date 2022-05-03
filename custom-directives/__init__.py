"""
Custom admonitions.

From https://github.com/orgs/executablebooks/discussions/701
"""
from docutils.parsers.rst.directives.admonitions import Admonition, BaseAdmonition


class Exercise(Admonition):
    def run(self):
        # Add class to style it
        if "class" not in self.options:
            self.options["class"] = ["admonition-exercise"]
        else:
            self.options["class"].append("admonition-exercise")
        # Add `Exercise` to the title so we don't have to type it
        self.arguments[0] = f"Exercise: {self.arguments[0]}"
        # Now run the Admonition logic so it behaves the same way
        nodes = super().run()
        return nodes


class GoodPractice(Admonition):
    def run(self):
        # Add class to style it
        if "class" not in self.options:
            self.options["class"] = ["admonition-good-practice"]
        else:
            self.options["class"].append("admonition-good-practice")
        # Add `Good practice` to the title so we don't have to type it
        self.arguments[0] = f"Good practice: {self.arguments[0]}"
        # Now run the Admonition logic so it behaves the same way
        nodes = super().run()
        return nodes


def setup(app):
    app.add_directive("exercise", Exercise)
    app.add_directive("goodpractice", GoodPractice)

