import unittest

txt1=u"""
Title
------

Solve the equation \(x^3+y^3=z^3\)

"""


class TestMakdownMath(unittest.TestCase):
    def setUp(self):
        pass
    def testSimpleEquation(self):
        import markdown
        html=markdown.markdown(txt1, extensions=['mdx_math'])

        self.assertIn('<script type="math/tex">x^3+y^3=z^3</script>', html)
