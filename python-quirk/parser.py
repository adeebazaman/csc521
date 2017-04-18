import sys
import pprint

pp = pprint.PrettyPrinter(indent=3, depth=15)

'''Uncomment before printing'''
# tokens = ["VAR","IDENT:x","ASSIGN","LPAREN","NUMBER:5","MULT","NUMBER:2","RPAREN","DIV","NUMBER:5","RETURN","IDENT:x","EOF"]

#tokens= ["FUNCTION","IDENT;FOO","EOF"]
# tokens = ["PRINT","NUMBER:1","ADD","NUMBER:4","SUB","NUMBER:3","EOF"]
#begin utilities
def is_ident(tok):
    '''Determines if the token is of type IDENT.
    tok - a token
    returns True if IDENT is in the token or False if not.
    '''
    return -1 < tok.find("IDENT")


def is_number(tok):
    '''Determines if the token is of type NUMBER.
    tok - a token
    returns True if NUMBER is in the token or False if not.
    '''
    return -1 < tok.find("NUMBER")


##

def Program(token_index):
    '''
     <Program> ->
     <Statement> <Program>
     | <Statement>
     '''
    #<Statement>
    (success, returned_index, returned_subtree) = Statement(token_index)
    if success:
        subtree= ["Program0",returned_subtree]
        #return [True, returned_index,subtree]
    #<Program>
        (success, returned_index, returned_subtree) = Program(returned_index)
        if success:
            subtree.append(returned_subtree)
            return [True, returned_index, subtree]

    #<Statement>
    (success, returned_index, returned_subtree) = Statement(token_index)
    if success:
        subtree=["Program1",returned_subtree]
        return [True, returned_index,subtree]
    return [False, token_index, []]
def Statement(token_index):
    '''
    <Statement> ->
    <FunctionDeclaration>
     | <Assignment>
      | <Print>
      '''

##    #<FunctionDeclaration>
##    (success, returned_index, returned_subtree) = FunctionDeclaration(token_index) """ I cant get it to work, so commented it out"""
##    if success:
##        subtree= ["Statement0",returned_subtree]
##        return [True, returned_index,subtree]
    #<Assignment>
    (success, returned_index, returned_subtree) = Assignment(token_index)
    if success:
        subtree= ["Statement1", returned_subtree]
        return [True, returned_index,subtree]
    #<Print>
    (success, returned_index, returned_subtree) = Print(token_index)
    if success:
        subtree= ["Statement2", returned_subtree]
        return [True, returned_index, subtree]
    return [False, token_index, []]





def SingleAssignment(token_index):

    (success, returned_index, returned_subtree) = Expression(token_index)

    subtree = ["SingleAssignment0"]
    if "VAR" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Expression(
                returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]



    (success, returned_index, returned_subtree) = Expression(token_index)
    if success:

        return [True, returned_index, ["Statement0",returned_subtree]]

    return [False, token_index, []]

def FunctionDeclaration(token_index):
    '''
    <FunctionDeclaration> ->
     FUNCTION <Name> LPAREN <FunctionParams> LBRACE <FunctionBody> RBRACE
     '''

    #FUNCTION <Name> LPAREN <FunctionParams> LBRACE <FunctionBody> RBRACE
    if "FUNCTION" == tokens[token_index]:
        subtree = ["FUNCTIONDECLARATION0", returned_subtree]
        (success, returned_index, returned_subtree) = Name(token_index + 1)
        if success:
            subtree.append(returned_subtree)
            return [True, returned_index, subtree]
            if "LPAREN" == tokens[returned_index]:
                subtree.append(tokens[returned_index])
                (success, returned_index, returned_subtree) = FunctionParams(
                        returned_index + 1)
                if success:
                    subtree.append(returned_subtree)
                    return [True, returned_index, subtree]
                    if "LBRACE" == tokens[returned_index]:
                        subtree.append(tokens[returned_index])
                        return [True, returned_index, subtree]
                        (success, returned_index, returned_subtree) = FunctionBody(returned_index + 1)
                        if success:
                            subtree.append(returned_subtree)
                            return [True, returned_index, subtree]
                            if "RBRACE" == tokens[returned_index]:
                                subtree.append(tokens[token_index])
                                return [True, returned_index + 1, subtree]
        return [False, token_index, []]


def FunctionParams(token_index):
    '''
    <FunctionParams> ->
     <NameList> RPAREN
      | RPAREN
      '''

    #<NameList> RPAREN
    (success, returned_index, returned_subtree) = NameList(token_index)
    if success:
        subtree=["FunctionParams0", returned_subtree]
        if "RPAREN" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            return [True, returned_index + 1, subtree]
    return [False, token_index, []]

    #RPAREN
    if "RPAREN" == tokens[token_index]:
        subtree = ["FunctionCallParams1", tokens[token_index]]
        return [True, token_index + 1, subtree]
    return [False, token_index, []]

def FunctionBody(token_index):
    '''
    <FunctionBody> ->
     <Program> <Return>
      | <Return>
      '''
    #<Program> <Return>
    (success, returned_index, returned_subtree) = Program(token_index)
    if success:
        subtree=["FunctionBody0",returned_subtree]
        (success, returned_index, returned_subtree) = Return(returned_index)
        if success:
            subtree.append(returned_subtree)
            return [True, returned_index, subtree]

##        return [True, returned_index, ["FunctionBody0", returned_subtree]]

    #<Return>
    (success, returned_index, returned_subtree) = Return(token_index)
    if success:
        subtree=["FunctionBody1",returned_subtree]
        return [True, returned_index,subtree]
    return [False, token_index, []]



def Return(token_index):
    '''
    <Return> ->
     RETURN <ParameterList>
     '''

    #RETURN<ParameterList>

    if "RETURN" == tokens[token_index]:
        subtree = ["Return0", tokens[token_index]]
        (success, returned_index, returned_subtree) = ParameterList(token_index + 1)
        if success:
            subtree.append(returned_subtree)
            return [True, returned_index, subtree]
    return [False, token_index, []]


def Assignment(token_index):
    '''
    <Assignment> ->
     <SingleAssignment>
     | <MultiAssignment>
     '''

     #<SingleAssignment>
    (success, returned_index, returned_subtree) = SingleAssignment(token_index)
    if success:
        subtree= ["Assignment0", returned_subtree]
        return [True, returned_index, subtree]
    #<MultiAssignment>
    (success, returned_index, returned_subtree) = MultiAssignment(token_index)
    if success:
        subtree= ["Assignment1", returned_subtree]
        return [True, returned_index, subtree ]
    return [False, token_index, []]

def MultiAssignment(token_index):
    '''
    <MultiAssignment> ->
     VAR <NameList> ASSIGN <FunctionCall>
    '''

    #VAR <NameList> ASSIGN <FunctionCall>
    if "VAR" == tokens[token_index]:
        subtree = ["MultiAssignment0", tokens[token_index]]
        (success, returned_index, returned_subtree) = NameList(token_index + 1)
        if success:
            subtree.append(returned_subtree)
            return [True, returned_index, subtree]
            if "ASSIGN" == tokens[returned_index]:
                subtree.append(tokens[returned_index])
                (success, returned_index, returned_subtree) = FunctionCall(returned_index + 1)
                if success:
                    subtree.append(returned_subtree)
                    return [True, returned_index, subtree]
    return [False, token_index, []]

def Print(token_index):
    '''
    <Print> ->
     PRINT <Expression>
     '''
    #PRINT <Expression>
    if "PRINT" == tokens[token_index]:
        subtree = ["Print0", tokens[token_index]]
        (success, returned_index, returned_subtree) = Expression(token_index + 1)
        if success:
            subtree.append(returned_subtree)
            return [True, returned_index, subtree]
    return [False, token_index, []]

def NameList(token_index):
    '''
    <NameList> ->
     <Name> COMMA <NameList>
      | <Name>
      '''

    # <Name> COMMA <NameList>
    (success, returned_index, returned_subtree) = Name(token_index)
    if success:
        subtree = ["NameList0", returned_subtree]
        if "COMMA" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = NameList(returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]

    #<Name>
    (success, returned_index, returned_subtree) = Name(token_index)
    if success:
        subtree = ["NameList1", returned_subtree]
        return [True, returned_index,subtree]
    return [False, token_index, []]


def ParameterList(token_index):
    '''
    <ParameterList> ->
     <Parameter> COMMA <ParameterList>
      | <Parameter>
      '''
    #<Parameter> COMMA <ParameterList>
    (success, returned_index, returned_subtree) = Parameter(token_index)
    if success:
        subtree = ["ParameterList0", returned_subtree]
        if "COMMA" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            return [True, returned_index, subtree]
            (success, returned_index, returned_subtree) = ParameterList(returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]

    #<Parameter>
    (success, returned_index, returned_subtree) = Parameter(token_index)
    if success:
        subtree= ["ParameterList1", returned_subtree]
        return [True, returned_index, subtree]
    return [False, token_index, []]


def Parameter(token_index):
    '''
    <Parameter> ->
     <Expression>
      | <Name>
      '''

    #<Expression>
    (success, returned_index, returned_subtree) = Expression(token_index)
    if success:
        ["Parameter0", returned_subtree]
        return [True, returned_index, subtree]
    return [False, token_index, []]

    #<Name>
    (success, returned_index, returned_subtree) = Name(token_index)
    if success:
        subtree= ["Parameter1", returned_subtree]
        return [True, returned_index, subtree]
    return [False, token_index, []]



def Expression(token_index):
    '''<Expression> ->
        <Term> ADD <Expression>
        | <Term> SUB <Expression>
        | <Term>

    '''


    # <Term> ADD <Expression>
    (success, returned_index, returned_subtree) = Term(token_index)
    if success:
        subtree = ["Expression0", returned_subtree]
        if "ADD" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Expression(
                returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]

##    # <Term> SUB <Expression>
    (success, returned_index, returned_subtree) = Term(token_index)
    if success:
        subtree = ["Expression1", returned_subtree]
        if "SUB" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Expression(
                returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]


    # <Term> COLON <Expression>
    (success, returned_index, returned_subtree) = Term(token_index)
    if success:
        subtree = ["Expression1", returned_subtree]
        if "COLON" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Expression(
                returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]

    # <Term> COLON <Expression>
    (success, returned_index, returned_subtree) = Term(token_index)
    if success:
        subtree = ["Expression1", returned_subtree]
        if "ASSIGN" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Expression(
                returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]


##    # <Term> COLON <Expression>
    (success, returned_index, returned_subtree) = Term(token_index)
    if success:
        subtree = ["Expression1", returned_subtree]
        if "PRINT" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Statement(
                returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]

    # <Term>
    (success, returned_index, returned_subtree) = Term(token_index)
    if success:
        return [True, returned_index, ["Expression2", returned_subtree]]
    return [False, token_index, []]


def Term(token_index):
    '''<Term> ->
        <Factor> MULT <Term>
        | <Factor> DIV <Term>
        | <Factor>
    '''
    # <Factor> MULT <Term>
    (success, returned_index, returned_subtree) = Factor(token_index)
    if success:
        subtree = ["Term0", returned_subtree]
        if "MULT" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Term(returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]
    # <Factor> DIV <Term>
    (success, returned_index, returned_subtree) = Factor(token_index)
    if success:
        subtree = ["Term1", returned_subtree]
        if "DIV" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Term(returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]
    # <Factor>
    (success, returned_index, returned_subtree) = Factor(token_index)
    if success:
        return [True, returned_index, ["Term2", returned_subtree]]
    return [False, token_index, []]


def Factor(token_index):
    '''
    <Factor> ->
        <SubExpression>
        | <SubExpression> EXP <Factor>
        | <FunctionCall>
        | <Value> EXP <Factor>
        | <Value>
    '''
    #<SubExpression> EXP <Factor>
    (success, returned_index, returned_subtree) = SubExpression(token_index)
    if success:
        subtree = ["Factor0", returned_subtree]
        if "EXP" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Factor(returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]
    #<SubExpression>
    (success, returned_index, returned_subtree) = SubExpression(token_index)
    if success:
        subtree = ["Factor1", returned_subtree]
        return [True, returned_index, subtree]
    #<FunctionCall>
    (success, returned_index, returned_subtree) = FunctionCall(token_index)
    if success:
        return [True, returned_index, ["Factor2", returned_subtree]]

    #<Value> EXP <Factor>
    (success, returned_index, returned_subtree) = Value(token_index)
    if success:
        subtree = ["Factor3", returned_subtree]
        if "EXP" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Factor(returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]

##    #<Value> ASSIGN <Factor>
##    (success, returned_index, returned_subtree) = Value(token_index)
##    if success:
##        subtree = ["Factor3", returned_subtree]
##        if "ASSIGN" == tokens[returned_index]:
##            subtree.append(tokens[returned_index])
##            (success, returned_index, returned_subtree) = Factor(returned_index + 1)
##            if success:
##                subtree.append(returned_subtree)
##                return [True, returned_index, subtree]



    #<Value> COMMA <Factor>
    (success, returned_index, returned_subtree) = Value(token_index)
    if success:
        subtree = ["Factor3", returned_subtree]
        if "COMMA" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Factor(returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]





    #<Value>
    (success, returned_index, returned_subtree) = Value(token_index)
    if success:
        return [True, returned_index, ["Factor4", returned_subtree]]
    return [False, token_index, []]


def FunctionCall(token_index):
    '''
    <FunctionCall> ->
        <Name> LPAREN <FunctionCallParams> COLON <Number>
        | <Name> LPAREN <FunctionCallParams>
    '''
    # <Name> LPAREN <FunctionCallParams> COLON <Number>
    (success, returned_index, returned_subtree) = Name(token_index)
    if success:

        subtree = ["FunctionCall0", returned_subtree]
        if "LPAREN" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = FunctionCallParams(
                returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                if "COLON" == tokens[returned_index]:
                    subtree.append(tokens[returned_index])
                    (success, returned_index, returned_subtree) = Number(
                        returned_index + 1)
                    if success:
                        subtree.append(returned_subtree)
                        return [True, returned_index, subtree]

    # <Name> LPAREN <FunctionCallParams>
        (success, returned_index, returned_subtree) = Name(token_index)
        if success:
            subtree = ["FunctionCall1", returned_subtree]
            if "LPAREN" == tokens[returned_index]:
                subtree.append(tokens[returned_index])
                (success, returned_index, returned_subtree) = FunctionCallParams(
                    returned_index + 1)
                if success:
                    subtree.append(returned_subtree)
                    return [True, returned_index, subtree]


    # Function
    if success:
        subtree = ["FunctionCall0", returned_subtree]
        if "FUNCTION" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = FunctionCallParams(
                returned_index + 1)
            return [True, returned_index, subtree]
    return [False, token_index, []]


def FunctionCallParams(token_index):
    '''
    <FunctionCallParams> ->
        <ParameterList> RPAREN
        | RPAREN
    '''
    #<ParameterList> RPAREN
    # todo after ParameterList is finished
    # RPAREN
    if "RPAREN" == tokens[token_index]:
        subtree = ["FunctionCallParams1", tokens[token_index]]
        return [True, token_index + 1, subtree]
    return [False, token_index, []]


def SubExpression(token_index):
    '''<SubExpression> ->
        LPAREN <Expression> RPAREN
    '''
    if "LPAREN" == tokens[token_index]:
        subtree = ["SubExpression0", tokens[token_index]]
        (success, returned_index, returned_subtree) = Expression(token_index + 1)
        if success:
            subtree.append(returned_subtree)
            if "RPAREN" == tokens[returned_index]:
                subtree.append(tokens[returned_index])
                return [True, returned_index + 1, subtree]
    return [False, token_index, []]


def Value(token_index):
    '''
    <Value> ->
        <Name>
        | <Number>
    '''
##    # try in order!
    #<name>
##    (success, returned_index, returned_subtree) = Variable(token_index)
##    if success:
##        (success, returned_index, returned_subtree) = Variable(token_index)
##        return [True, returned_index, ["Variable0", returned_subtree]]

    #<name>
    (success, returned_index, returned_subtree) = Name(token_index)
    if success:
        (success, returned_index, returned_subtree) = Name(token_index)
        return [True, returned_index, ["Value0", returned_subtree]]

    #<number>
    (success, returned_index, returned_subtree) = Number(token_index)
    if success:
        return [True, returned_index, ["Value1", returned_subtree]]

    return [False, token_index, []]



def Variable(token_index):

    '''<Name> ->
        IDENT
        | VAR IDENT
    '''
    subtree = []
    if is_variable(tokens[token_index]):
        subtree = ["Assignment0", tokens[token_index]]
        return [True, token_index + 1, subtree]

    if "VAR" == tokens[token_index]:
        if is_variable(tokens[token_index + 1]):
                subtree = ["Assignment1", tokens[token_index], tokens[token_index + 1]]
                return [True, token_index + 2, subtree]

    return [False, token_index, subtree]


def Name(token_index):
    '''<Name> ->
        IDENT
        | SUB IDENT
        | ADD IDENT
    '''
    subtree = []

    if is_ident(tokens[token_index]):
        subtree = ["Name0", tokens[token_index]]
        return [True, token_index + 1, subtree]

    if "SUB" == tokens[token_index]:
        if is_ident(tokens[token_index + 1]):
            subtree = ["Name1", tokens[token_index], tokens[token_index + 1]]
            return [True, token_index + 2, subtree]
    if "ADD" == tokens[token_index]:
        if is_ident(tokens[token_index + 1]):
            subtree = ["Name2", tokens[token_index], tokens[token_index + 1]]
            return [True, token_index + 2, subtree]
    return [False, token_index, subtree]


def Number(token_index):
    '''<Number> ->
        NUMBER
        | SUB NUMBER
        | ADD NUMBER
    '''
    subtree = []
    if is_number(tokens[token_index]):
        subtree = ["Number0", tokens[token_index]]
        return [True, token_index + 1, subtree]


    if "SUB" == tokens[token_index]:
        if is_number(tokens[token_index + 1]):
            subtree = ["Number1", tokens[token_index], tokens[token_index + 1]]
            return [True, token_index + 2, subtree]
    if "ADD" == tokens[token_index]:
        if is_number(tokens[token_index + 1]):
            subtree = ["Number2", tokens[token_index], tokens[token_index + 1]]
            return [True, token_index + 2, subtree]
    return [False, token_index, subtree]



if __name__ == '__main__':
    print("starting __main__")
    pp.pprint(Program(0))
