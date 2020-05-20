#!/usr/bin/env python3
"""
Script:	recaman_sequence_visualised.py
Date:	2020-05-20	

Platform: macOS/Windows/Linux

Description:
Recamán sequence of numbers visualised with turtle
"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2020, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'

import argparse
import turtle
import colorsys

def main():
    if options.max_length is None:
        # Get sequence until a value (or above is reached)
        draw_sequence(options.length)
    else:
        # Get sequence of fixed length
        draw_sequence(options.max_length)

    print('Drawing complete')

    if options.file is None:
        turtle.getscreen()._root.mainloop()
    else:
        turtle.getscreen().getcanvas().postscript(file=options.file.name)


def draw_sequence(length=None, max_value=0):
    # Set the window screen and bounds
    width, height = options.width, options.height
    turtle.getscreen().setup(width, height)
    turtle.setworldcoordinates(0, -height / 2, width, height / 2)

    # Setup the pen
    turtle.bgcolor((*options.colour_back))
    turtle.pencolor((*options.colour_line))
    turtle.pensize(options.line_width)
    if options.shape is None:
        turtle.hideturtle()
    else:
        turtle.shape(options.shape)

    # Setup drawing speeds
    turtle.speed(0)
    if options.file is None:
        print('Window opened')
        turtle.tracer(int(max(length, max_value)/100))
    else:
        print('Turning off screen updates for file output')
        turtle.tracer(False)

    # Set drawing speed and angle to draw at
    turtle.left(90)

    # Initialise counters and bool
    hue = 0
    counter = 0
    sequence = [0]
    even = True
    while True:
        if options.colour_rainbow:
            r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
            hue += 0.9 / max(length, max_value)
            turtle.pencolor((r, g, b))

        counter += 1
        digit = sequence[-1] - counter

        if length is None:
            if max_value <= sequence[-1]:
                break
        else:
            if counter > length:
                break

        # If the digit is less than zero or will intersect it move forward
        if digit < 0 or digit in sequence:
            sequence.append(sequence[-1] + counter)
        else:
            sequence.append(sequence[-1] - counter)

        # Draw the arcs
        difference = sequence[-1] - sequence[-2]
        # Turn the linear growth of sides on the circles to a curve, increase 5 for more linear change
        # Speeds up circle drawing at the sacrifice of minimal quality perception
        steps = int((counter * 3.14 / (5 + counter)) * options.quality) + 1
        if even:
            turtle.circle(- difference * options.scale, 180, steps=steps)
        else:
            turtle.circle(difference * options.scale, 180, steps=steps)
        even = False if even else True


if __name__ == '__main__':
    def parser_formatter(format_class, **kwargs):
        """
        Use a raw parser to use line breaks, etc
        :param format_class: (class) formatting class
        :param kwargs: (dict) kwargs for class
        :return: (class) formatting class
        """
        try:
            return lambda prog: format_class(prog, **kwargs)
        except TypeError:
            return format_class


    parser = argparse.ArgumentParser(description='Recamán sequence of numbers visualised with turtle',
                                     formatter_class=parser_formatter(argparse.RawTextHelpFormatter,
                                                                      indent_increment=4, max_help_position=12,
                                                                      width=160))

    # FILE
    parser.add_argument('-o', '--out-file', type=argparse.FileType('w'),
                        action='store', dest='file', default=None,
                        metavar='PATH',
                        help='Export to file instead, postscript (.ps)'
                             '\nDefault: %(default)s')

    # Visualisation size (drawn/saved)
    size = parser.add_mutually_exclusive_group()
    size.add_argument('-l', '--length', type=int,
                      action='store', dest='length', default=112,
                      metavar='INTEGER',
                      help='The amount of numbers to calculate'
                           '\nDefault: %(default)s')
    size.add_argument('-m', '--max-length', type=int,
                      action='store', dest='max_length', default=None,
                      metavar='INTEGER',
                      help='Calculate up to, and stop, after number is reached')
    parser.add_argument('-s', '--scale', type=int,
                        action='store', dest='scale', default=2,
                        metavar='SCALE',
                        help='Scale of the visuals, 2 is double'
                             '\nDefault: %(default)s')
    parser.add_argument('-w', '--line_width', type=int,
                        action='store', dest='line_width', default=1,
                        metavar='INTEGER',
                        help='Scale of the visuals, 2 is double'
                             '\nDefault: %(default)s')
    parser.add_argument('-q', '--quality', type=int,
                        action='store', dest='quality', default=10,
                        metavar='QUALITY',
                        help='Quality of the curves, 1 is base'
                             '\nDefault: %(default)s')
    parser.add_argument('-e', '--end',
                        action='store', dest='shape', default=None,
                        choices=['arrow', 'turtle', 'circle', 'square', 'triangle', None],
                        metavar='SHAPE',
                        help='Symbol to appear at the end of the draw'
                             '\nDefault: %(default)s')
    parser.add_argument('-b', '--colour-back', type=float,
                        action='store', dest='colour_back', default=[1.0, 1.0, 1.0], nargs=3,
                        metavar='DECIMAL',
                        help='3 RGB values of 0.0-1.0'
                             'Note: Does no apply to saved files, change in post'
                             '\nDefault: %(default)s')
    parser.add_argument('-f', '--colour-line', type=float,
                        action='store', dest='colour_line', default=[0.0, 0.0, 0.0], nargs=3,
                        metavar='DECIMAL',
                        help='3 RGB values of 0.0-1.0'
                             '\nDefault: %(default)s')
    parser.add_argument('-r', '--colour-rainbow',
                        action='store_true', dest='colour_rainbow', default=False,
                        help='Rainbow gradient'
                             'Note: Overrides pen colour and works better with -length'
                             '\nDefault: %(default)s')

    # Window size
    parser.add_argument('-x', '--width', type=int,
                        action='store', dest='width', default=1024,
                        metavar='WIDTH',
                        help='Width of the window'
                             '\nDefault: %(default)s')
    parser.add_argument('-y', '--height', type=int,
                        action='store', dest='height', default=720,
                        metavar='HEIGHT',
                        help='Height of the window'
                             '\nDefault: %(default)s')

    options = parser.parse_args()

    main()
