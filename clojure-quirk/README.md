Homework 3 
Clojure-quirk


In this project, we would be implementing the Quirk programming language, the language created for this class. Unlike the Python implementation, this homework will be less separated into distinct stages but will have some structure:
clojure-quirk - A Leinigen Clojure project named clojure-quirk that contains a runnable version of your Quirk implementation. An important file in this project is the project.clj that contains your project settings (including where the main/runnable function is located) and dependencies.
clojure-quirk.clj - The Clojure code that contains your parser (also lexer thanks to Instaparse) and interpreter.
Quirk ENBF grammar - The ENBF form of the Quirk language grammar in your project's resource directory. This serves as input to Instaparse for the creation of the parser/lexer.
