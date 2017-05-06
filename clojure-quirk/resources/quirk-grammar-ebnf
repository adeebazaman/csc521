(ns clojure-quirk.core
(:require [instaparse.core :as insta]))

(def parser
  (insta/parser
   " Program = Statement Program | Statement 
     Statement = FunctionDeclaration | Assignment | Print



     FunctionDeclaration = FUNCTION Name LPAREN FunctionParams LBRACE FunctionBody RBRACE
     FunctionParams = NameList RPAREN | RPAREN
     FunctionBody = Program Return | Return
     Return = RETURN ParameterList

   

     Assignemnt = SingleAssignment | MultipleAssignment 
     SingleAssignment = VAR Name ASSIGN Expression
     MultipleAssignment = VAR NameList ASSIGN FunctionCall 

 
     Print = PRINT Expression
     

     NameList := Name COMMA NameList | Name
     ParameterList := Parameter COMMA ParameterList | Parameter
     Parameter := Expression | Name 

   
     Expression := Term ADD Expression | Term SUB Expression | Term
     Term := Factor MULT Term | Factor DIV Term | Factor
     Factor := SubExpression EXP Factor | SubExpression | FunctionCall | Value EXP Factor | Value
     FunctionCall :=  Name LPAREN FunctionCallParams COLON Number | Name LPAREN FunctionCallParams
     FunctionCallParams :=  ParameterList RPAREN | RPAREN
     SubExpression := LPAREN Expression RPAREN
     Value := Name | Number



     Name := IDENT | SUB IDENT | ADD IDENT
     Number := NUMBER | SUB NUMBER | ADD NUMBER


  

   VAR:= # "var"
   FUNCTION:= # "function"
   RETURN:= # "return"
   PRINT:= # "print"

   
  
  NUMBER:= #"((\d+(\.\d*)?)|(\.\d+))"
  IDENT:= # "[a-zA-Z]+[a-zA-Z0-9_]*"   

   ASSIGN := # "="
   ADD := # "\+"
   SUB := # "\-"
   MULT := # "\*"
   DIV :=  # "\/"
   EXP :=  # "\^"

   
   LAPREN := # "\("
   RPAREN := # "\)"
   RBRACE := # "\}"
   LBRACE := # "\{"
   COMMA := # "\,"
   COLON := # "\:"
  
  
")) 

(parser "print")

(ns clojure-quirk.core
(:require [instaparse.core :as insta]))


(def quirk
  (insta/parser (slurp "resources/quirk-grammar-ebnf")))
(quirk "( print5 )")
