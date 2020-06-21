import pygame
import pygame.font
from diamondquest.view.window import Window, View
from functools import reduce
from random import randint
from diamondquest.common.mode import ModeType
from diamondquest.common.loader import load_font
from diamondquest.common import color


""" Deals with MathView
"""
# window.draw_shadow()
# TODO:


class PuzzleView:

    @classmethod
    def update(cls):
        # Load latest view
        cls.view = Window.get_view(ModeType.PUZZLE)
        #cls.view.surface.fill(color.BLACK)
        #Window._draw_shadow()

        rendered_problem = cls.draw_puzzle()
        problem_display_area = rendered_problem.get_rect()
        cls.view.blit(rendered_problem, problem_display_area)

    @classmethod
    def draw_puzzle(cls):
        pygame.font.init()
        font = load_font("Cascadia" , 60 )
        problem, answer = cls.puzzle_string(2,2,2)
        rendered_problem = font.render(problem, True, color.WHITE)
        
        return rendered_problem
        # surface = Window.get_surface(Views.MATH)

        # Get Transparent Background
        # Window.draw_shadow()
        # draw on surface

        # surface.blit(rendered_problem, problem_display_area)
        # Window.redraw_window()
    @classmethod
    def depth_range(cls, depth):
        # defines range of numbers based on depth
        # increases the range with increasing depth
        if 0 <= depth <= 7:
            return randint(1, 10)
        elif 8 <= depth <= 15:
            return randint(11, 100)
        elif 16 <= depth <= 23:
            return randint(101, 1000)
        elif 24 <= depth <= 31:
            return randint(1001, 5000)
        elif 32 <= depth <= 39:
            return randint(5001, 10000)
        elif 40 <= depth <= 47:
            return randint(10001, 50000)
        elif 48 <= depth <= 55:
            return randint(50001, 100000)
        elif 56 <= depth <= 63:
            return randint(100001, 200000)

    @classmethod
    def depth_numberofterms(cls, depth):
        # defines range of numbers based on depth
        # increases the range with increasing depth
        if 0 <= depth <= 7:
            return 2
        elif 8 <= depth <= 15:
            return 2
        elif 16 <= depth <= 23:
            return 3
        elif 24 <= depth <= 31:
            return 3
        elif 32 <= depth <= 39:
            return 4
        elif 40 <= depth <= 47:
            return 4
        elif 48 <= depth <= 55:
            return 5
        elif 56 <= depth <= 63:
            return 5

    @classmethod
    def power_level_operators(cls, powerlevel, numberofterms, depth):
        listofNumbers = list()
        for i in range(numberofterms):
            i = cls.depth_range(depth)
            listofNumbers.append(i)
        if powerlevel == 1:
            answer = sum(listofNumbers)
            return listofNumbers, answer, "+"
        elif powerlevel == 2:
            answer = reduce((lambda x, y: x - y), listofNumbers)
            return listofNumbers, answer, "-"
        elif powerlevel == 3:
            answer = reduce((lambda x, y: x * y), listofNumbers)
            return listofNumbers, answer, "*"
        elif powerlevel == 4:
            answer = reduce((lambda x, y: x / y), listofNumbers)
            return listofNumbers, answer, "/"
        elif powerlevel == 5:
            pass
        elif powerlevel == 6:
            pass
        elif powerlevel == 7:
            pass
        elif powerlevel == 8:
            pass
    
    @classmethod
    def tool_difficulty(cls, tool, powerlevel, depth):
        # Pickaxe two terms one operator
        # drill multiple terms one operator
        # tnt multiple terms multiple operator
        # operators depend on power level
        if tool == "pickaxe":
            numberofterms = 2
            cls.power_level_operators(powerlevel, numberofterms, depth)
        elif tool == "drill":
            numberofterms = cls.depth_numberofterms(depth)
            cls.power_level_operators(powerlevel, numberofterms, depth)
        elif tool == "tnt":
            pass
    
    @classmethod
    def puzzle_string(cls, powerlevel, numberofterms, depth):
        # Convert list of Numbers to String and add Operators
        # return it to pygame fonts to render on screen
        listofNumbers, answer, operator = cls.power_level_operators(
            powerlevel, numberofterms, depth
        )
        listofString = [str(number) for number in listofNumbers]
        if operator == "+":
            puzzleString = "+".join(listofString)
        elif operator == "-":
            puzzleString = "-".join(listofString)
        elif operator == "*":
            puzzleString = "*".join(listofString)
        elif operator == "/":
            puzzleString = "/".join(listofString)

        # implement scorer
        return puzzleString, answer

    @classmethod
    def player_input(cls):
        playerInput = input("Enter Answer")
        print("Answer" + playerInput)
        return int(playerInput)

    @classmethod
    def scorer(cls, answer, score):
        check_answer = cls.answer_check(cls.player_input(), answer)
        if check_answer == True:
            score = score + 1
            # level or points increase
            pass
        elif check_answer == False:
            score = score
            # level stays same points stay same
            pass
        return score

    @classmethod
    def answer_check(cls, userresponse, correctanswer):
        # Returns a bool
        # Increase level for true
        # Display Incorrect for false
        if userresponse == correctanswer:
            return True
        else:
            return False

    @classmethod
    def bubble_puzzles(cls, spectrum):
        # Future Task: Deals with in game Maths Puzzles with bubbles.
        # This can also use puzzle generator with changing spectrum
        pass
