FILE_FORMAT = """import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # def test_simple_string(self):
    #     "test simple string"
    #     self.assertTrue(TestLexer.test("'Yanxi Palace - 2018'","'Yanxi Palace - 2018',<EOF>",101))

    # def test_complex_string(self):
    #     "test complex string"
    #     self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))
"""

SAMPLE_FOLDER = "./sample"

import os

def get_file_names(folder_path):
    file_names = []
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            name_without_extension, _ = os.path.splitext(filename)
            file_names.append(name_without_extension)
    return sorted(set(file_names))

def create_file_content():
    def preprocess_string(string):
        string = string.replace('\\', '\\\\')
        string = string.replace('"', '\\"')
        return string


    file_names = get_file_names(SAMPLE_FOLDER)
    file_output = FILE_FORMAT
    for fileName in file_names:
        file_path = os.path.join(SAMPLE_FOLDER, fileName)

        input_content = preprocess_string(''.join(open(file_path+".input", 'r').readlines()))
        output_content = preprocess_string(''.join(open(file_path+".output", 'r').readlines()))

        temp_text = f'''
        def test_{fileName}(self):
            self.assertTrue(TestLexer.test("""{input_content}""", """{output_content}""", "{fileName}"))
        '''

        file_output += temp_text

    return file_output

file_content = create_file_content()

with open("LexerSuite.py", 'w') as file:
    file.write(file_content)