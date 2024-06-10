# student_test.py

import unittest
from unittest.mock import patch
from student import Student, ChattyStudent
import io

class TestStudent(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_says_hello(self, mock_stdout):
        student = Student()
        student.hello()
        expected_output = "Hey there I'm so excited to learn stuff.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_raises_hand(self, mock_stdout):
        student = Student()
        student.raise_hand()
        expected_output = "Pick me!\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

class TestChattyStudent(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_says_hello(self, mock_stdout):
        chatty_student = ChattyStudent()
        chatty_student.hello()
        expected_output = ("Hey there I'm so excited to learn stuff.\n" +
                           "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy What, you don't want any spoilers? Okay well let me just tell you who died...\n")
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_raises_hand(self, mock_stdout):
        chatty_student = ChattyStudent()
        chatty_student.raise_hand()
        expected_output = "Pick me!\nPick me!\nPick me!\nPick me!\nPick me!\nPick me!\nPick me!\nPick me!\nPick me!\nPick me!\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
