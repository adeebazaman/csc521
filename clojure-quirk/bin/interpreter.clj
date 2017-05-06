(ns clojure-quirk.core
  (:gen-class)
  (:require [instaparse.core :as insta]))

(defn third [aList] (nth aList 2))
(defn fourth [aList] (nth aList 3))

(defn 0 [aList] (nth aList 0))

(0 subtree)

(defn CallByLabel [funLabel & args]
  (apply (resolve (symbol (name funLabel))) args))


;the following functions reduce
;(CallByLabel (first (second subtree)) (second subtree) scope)
;to this:
;(CallByLabel (stSecond subtree) (second subtree) scope)

    (CallByLabel (stSecond subtree) (second subtree) scope)
(defn stFirst [subtree] (first (first subtree)))
(defn stSecond [subtree] (second (first subtree)))

(defn Program [subtree scope]
  ;<Program> -> <Statement> <Program> | <Statement>

 (println "PROGRAM")
 ;(println subtree)
 ;(println scope)
 ;[:Program [:Statement ...] [:Program ... ]]
 ;[:Program [:Statement ...]]
 (cond
   ;Program0
   (= :Program (first (third subtree)))
   ((CallByLabel (first (second subtree)) (second subtree) scope)
     (CallByLabel (first (third subtree)) (third subtree) scope))
   ;Program1
   :else
   (CallByLabel (first (second subtree)) (second subtree) scope)
  )
 )

(defn Statement [subtree scope]
 (println "STATEMENT")
 ;(println subtree)
 ;(println scope)
 ;<Statement> -> <FunctionDeclaration> | <Assignment> | <Print>
 ;[ :Statement [ :FunctionDeclaration...]]
 ;[ :Statement [ :Assignment...]]
 ;[ :Statement [ :Print...]]
 (cond 
   ;Statement0
   (= :Statement(first(third subtree)))
   ((CallByLabel (first (second subtree)) (second subtree) scope)
   ;Statement1
   ((CallByLabel (first (second subtree)) (second subtree) scope)
    ;Statement2
    :else
    ((CallByLabel (first (second subtree)) (second subtree) scope)
        )
      )
    )    
   )
 
 (defn FunctionDeclaration [subtree scope]
  (let [functionName (CallByLabel (first (third subtree)) (third subtree) scope)
        paramNames (CallByLabel (first (fifth subtree)) (fifth subtree) scope)
       ]
	(assoc scope functionName (paramNames (seventh subtree)))
  )
)
  (defn Statement [subtree scope]
 (println "ASSIGNMENT") 
 ;<Assignment>|<SingleAssignment>|<MultipleAssigment>
 ;[ :Assignment [ :SingleAssignment...]]
 ;[ :Assignment [ :MultipleAssignment...]]
  ;Statement0
   (= :Assignment(first(third subtree)))
   ((CallByLabel (first (second subtree)) (second subtree) scope)
   ;Statement1
   :else
   ((CallByLabel (first (second subtree)) (second subtree) scope)
     )
   )
  )
 )



 
 






(defn Expression [subtree scope]
  ;<Expression> -> <Term> ADD <Expression> | <Term> SUB <Expression> | <Term>
	(println "Expression")
	(println first( second subtree))

	(cond
   (= 2 (count subtree))
   (CallByLabel (first (second subtree)) (second subtree) scope) 
   (= :Term (first (second subtree)))
		((if (.equals :ADD (first (third subtree)))
			(+ (CallByLabel (first (second subtree))(second subtree) scope)
			(CallByLabel (first (fourth subtree))(fourth subtree) scope)))
		(if (.equals :SUB (first (third subtree)))
			(- (CallByLabel (first (second subtree))(second subtree) scope)
			(CallByLabel (first (fourth subtree))(fourth subtree) scope))))
	
	
	;:else
	;	(CallByLabel (first (second subtree)) (second subtree) scope))
			

); end Expression

 (defn Term [subtree scope]
	;(println "Term")
	;(println (count subtree))
	(if (= 2 (count subtree))
		(println (CallByLabel (first (second subtree))(second subtree) scope)))

	(if ( < 2 (count subtree))
		(cond (= :MULT (first (third subtree)))
				(*(CallByLabel (first (second subtree))(second subtree) scope)
				(CallByLabel (first (fourth subtree))(fourth subtree) scope))
			(= :DIV (first (third subtree)))
				(quot (CallByLabel (first (second subtree))(second subtree) scope)
				(CallByLabel (first (fourth subtree))(fourth subtree) scope))))

	;(println "Done Term")
); end Term

(defn Factor [subtree scope]
	;(println "Factor")
	;(println (count subtree))
	
	(if (= 2 (count subtree))
		(println (CallByLabel (first (second subtree))(second subtree) scope)))

	(if (< 2 (count subtree))
			(Math/pow (CallByLabel (first (second subtree))(second subtree) scope)
			(CallByLabel (first (fourth subtree)(fourth subtree)scope))))
		
	;(println "Done Factor")
); end Factor
;this return a map with local variable bindings when calling a function
;needs to have a list of values
(def VarBindLoop [paramList valueList]
  (if (= 1 (count paramList))
    (assoc {} (first paramList)  (first valueList))
    (merge (assoc {} (first paramList)  (first valueList)) 
      (VarBindLoop
        (rest paramList)
        (rest valueList)
        )
      
      )
   )
 )
 
(defn interpret-quirk [subtree scope] (CallByLabel (first subtree) subtree {}))
 

(defn -main [& args]
  ;sample for reading all stdin
  ;(def stdin (slurp *in*))
  ;(println stdin)
  
  ;(println (first *command-line-args*))
  (if (.equals "-pt" (first *command-line-args*))
    (def SHOW_PARSE_TREE true)
  )
  (def quirk-parser (insta/parser (slurp "resources/quirk-grammar-ebnf") :auto-whitespace :standard))
  (def parse-tree (quirk-parser "function foo (x, y) { return 3 + 4 + 2 / x ^ y} print foo(12, 12)"))
  (if (= true SHOW_PARSE_TREE) 
    (println parse-tree) 
    (interpret-quirk parse-tree {}))
  ;(interpret-quirk parse-tree {})
  ;(println "done!")
 )

(-main)