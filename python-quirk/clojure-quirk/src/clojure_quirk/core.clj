(ns clojure-quirk.core
(:require [instaparse.core :as insta]))


(def quirk
  (insta/parser (slurp "resources/quirk-grammar-ebnf")))
(println (quirk "print5"))
