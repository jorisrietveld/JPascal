# Author: Joris Rietveld <jorisrietveld@gmail.com>
# Created: 20-08-2017 13:52
# Licence: GPLv3 - General Public Licence version 3
from enum import Enum

class ArithmeticOperator:
    """ ArithmeticOperator class

        This class is used to store arithmetic operator values and checking if they are valid.
    """

    ADDITION = '+'
    SUBTRACTION = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'

    @classmethod
    def is_addition(cls, character):
        return character == cls.ADDITION

    @classmethod
    def is_subtraction(cls, character):
        return character == cls.SUBTRACTION

    @classmethod
    def is_multiplication(cls, character):
        return character == cls.MULTIPLICATION

    @classmethod
    def is_division(cls, character):
        return character == cls.DIVISION

    @classmethod
    def _get_item(cls, operator, default=None, as_token=False):
        if cls.is_addition(operator) or operator == Token.Type.ADDITION:
            return Token.Type.ADDITION if as_token else cls.ADDITION

        if cls.is_subtraction(operator) or operator == Token.Type.SUBTRACTION:
            return Token.Type.SUBTRACTION if as_token else cls.SUBTRACTION

        if cls.is_multiplication(operator) or operator == Token.Type.MULTIPLICATION:
            return Token.Type.MULTIPLICATION if as_token else cls.MULTIPLICATION

        if cls.is_division(operator) or operator == Token.Type.DIVISION:
            return Token.Type.DIVISION if as_token else cls.DIVISION

        return default

    @classmethod
    def get_operator(cls, operator, default=None):
        return cls._get_item(operator, default=default)

    @classmethod
    def get_token_name(cls, operator, default=None):
        return cls._get_item(operator, default=default, as_token=True)

    @classmethod
    def is_valid(cls, operator):
        return cls._get_item(operator, default=False)


class ArithmeticOperation:
    @classmethod
    def add(cls, base, increase_by):
        return base + increase_by

    @classmethod
    def subtract(cls, base, decrease_by):
        return base - decrease_by

    @classmethod
    def multiply(cls, base, times):
        return base * times

    @classmethod
    def divide(cls, base, parts):
        return base / parts

    @classmethod
    def by_token_name(cls, name, base, modifier):
        if name == Token.Type.ADDITION:
            return cls.add(base, modifier)

        if name == Token.Type.SUBTRACTION:
            return cls.subtract(base, modifier)

        if name == Token.Type.MULTIPLICATION:
            return cls.multiply(base, modifier)

        if name == Token.Type.DIVISION:
            return cls.divide(base, modifier)


class Token(object):
    """ Token class

        This class defines an token that will be used to construct expressions. An token
        is an sequence of characters that are recognized as an valid language construct"
    """

    class Type(Enum):
        INTEGER = 'INTEGER'
        EOF = 'EOF'
        ADDITION = 'ADDITION'
        SUBTRACTION = 'SUBTRACTION'
        MULTIPLICATION = 'MULTIPLICATION'
        DIVISION = 'DIVISION'
        MODULO = 'MODULO'

    def __init__(self, token_type, value):
        # Token token_type
        self.type = token_type
        # Token value
        self.value = value

    def __str__(self):
        """ The string representation ot the class instance.
        Examples:
            Token( INTEGER, 1 )
            Token( PLUS, + )
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=self.value
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    """ The Pascal Interpreter class

    This is the main class of the project. It will take pascal source code and interpret the instructions.
    """

    def __init__(self, source_code):
        """ The Pascal Interpreter constructor

        Upon creating of an Interpreter instance you must pass an string containing Pascal source code so it can
        later be used for parsing and executing the code.
        """
        self.input_text = source_code
        # The current string index its analyzing.
        self.current_position = 0
        # The current token instance
        self.current_token = None
        # The current character that is being analyzed.
        self.current_character = self.input_text[self.current_position]

    def error(self, message='Error parsing input'):
        """ The error method

        This is heaviest used method when interpreting source code, because face it programmers have
        no idea what they're doing but sometimes it seems to work.
        :param message: An string that will be used to log or display what was going wrong.
        :return:
        """
        raise Exception(message)

    def advance(self):
        """ The advance method

        This method will advance the current position and current character to analyze.
        """

        self.current_position += 1
        # Are we past the end of the input?
        if self.current_position > len(self.input_text) - 1:
            # Yes, set the current char to None so the end of file token can be inserted.
            self.current_character = None
        else:
            # No, update update the current character so we can analyze its content.
            self.current_character = self.input_text[self.current_position]

    def integer(self):
        """ The integer method

        This method will read integer values from text and return it as an integer.
        :return:
        """
        result = ''
        while self.current_character is not None and self.current_character.isdigit():
            result += self.current_character
            self.advance()
        return int(result)

    def skip_whitespace(self):
        """ The whitespace method

        This method will read spaces and ignore them while advancing the
        current index pointer and update the character to analyze.
        :return:
        """
        while self.current_character is not None and self.current_character.isspace():
            self.advance()

    def get_next_token(self):
        """ The get next token method

        This method try's to find the next token in the sourcecode and return it or raise an "You're stupid".
        :return:
        """
        while self.current_character is not None:

            # If current character is an space, advance to some non whitespace characters.
            if self.current_character.isspace():
                self.skip_whitespace()
                continue

            # If the current character is an digit, start reading characters until an non digits turns up. Advance the
            # current character to the non digit one and return an integer token with the value of the digit sequence.
            if self.current_character.isdigit():
                return Token(Token.Type.INTEGER, self.integer())

            # If current character is an ADDITION operator, advance in code and return an ADDITION token.
            if self.current_character == ArithmeticOperator.ADDITION:
                self.advance()
                return Token(Token.Type.ADDITION, ArithmeticOperator.ADDITION)

            # If current character is an SUBTRACTION operator, advance in code and return an SUBTRACTION token.
            if self.current_character == ArithmeticOperator.SUBTRACTION:
                self.advance()
                return Token(Token.Type.SUBTRACTION, ArithmeticOperator.SUBTRACTION)

            # If current character is an MULTIPLICATION operator, advance in code and return an MULTIPLICATION token.
            if self.current_character == ArithmeticOperator.MULTIPLICATION:
                self.advance()
                return Token(Token.Type.MULTIPLICATION, ArithmeticOperator.MULTIPLICATION)

            # If current character is an DIVISION operator, advance in code and return an DIVISION token.
            if self.current_character == ArithmeticOperator.DIVISION:
                self.advance()
                return Token(Token.Type.DIVISION, ArithmeticOperator.DIVISION)

            # If the current character is not parseable into an token raise an exception.
            self.error(
                "Unrecognized character: The character '{0}' is not recognized as an valid language construct".format(
                    self.current_character
                )
            )
        return Token(Token.Type.EOF, None)

    def eat(self, token_type):
        """ The eat method

        This method will check if the current token matches an certain token type, if so advance to the next token or
        or raise an "That's not the type I was expecting, like your parents never expected anything from you"
        :param token_type: The type of token that is expected.
        :return:
        """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error(
                "Unexpected token type: The type {0} does not match the token: type {1}, value {2}.".format(
                    token_type.lower(),
                    self.current_token.type,
                    self.current_token.value
                )
            )

    def term(self):
        """ The term method

        This method will eat an integer token, so the parsers pointer is passed the integer and return the
        integer value it had read.
        :return:
        """
        token = self.current_token
        self.eat(Token.Type.INTEGER)
        return token.value

    def expression(self):
        """ The expression method

        The main function of the program.
        :return:
        """
        self.current_token = self.get_next_token()

        # The current term (Integers, Chars, etc)
        result = self.term()

        while self.current_token.type in (
                Token.Type.ADDITION,
                Token.Type.SUBTRACTION,
                Token.Type.MULTIPLICATION,
                Token.Type.DIVISION):

            current_operator = ArithmeticOperator.get_token_name(self.current_token.type, default=False)

            if current_operator:
                self.eat(current_operator)
                # Execute an arithmetic operation like: {result} {operator} {next_term}
                result = ArithmeticOperation.by_token_name(current_operator, result, self.term())

        return result
