
import sys
import re

tokens= {

    'var':      'VAR',
    'function': 'FUNCTION',
    'return':   'RETURN',
    'print':    'PRINT',
    'x':        'ASSIGN',
    '+':        'ADD',
    '-':        'SUB',
    '*':        'MULT',
    '/':        'DIV',
    '^':        'EXP',
    '(':        'LPAREN',
    ')':        'RPAREN',
    '{':        'LBRACE',
    '}':        'RBRACE',
    ',':        'COMMA',
    ':':        'COLON',
    'EOF':      'EOF'
    }

IDENT=      '[a-zA-Z]+[a-zA-Z0-9_]*'
INDEX=     '[+-]?((\d+(\.\d*)?)|(\.\d+))'
NUMBER=      '[0-9]+'

ui= sys.stdin[-1]
user_input= open(ui,'r')
file_input= user_input.read()

def lexer( user_input, tokens):

    new_input=" "       ##new string
    split_text= user_input.split(" ")

    find_RE2= re.findall(INDEX,user_input)  ##get all the number in user_input

    for i in split_text:            ##for i in dictionary of tokens
        if i in tokens:
            new_input += tokens[i]+ " "
            
        else:
            if i in find_RE2:
                new_input += i.replace(i,"INDEX"+" ")
            
            else:
                new_input +="NUMBER:"+i+ " "
                

       
    return new_input


def main():
    user_input= raw_input( "what do you want to lex?")
    token_word= (lexer(user_input, tokens))
    output= token_word.split()

    for i in output:
        if i == "EOF":
            print i
            print
        else:
            print i
##    for i in token_word.split():
##        print i

if __name__=="__main__":

    main()



