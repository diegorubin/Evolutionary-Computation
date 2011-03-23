;; Problema 1
;; Capitão Caverna S.A.
;;
;; Abordagem 1
;;
;; maxf(x) = 50x + 70y + 100z
;; sendo:
;; x a quantidade de jangadas. x <= 4
;; y a quantidade de canoa. y <= 8
;; z a quantidade de arcas. z <= 3
;; 
;; Cada embarcação precisa de um capitão.
;; A jangada precisa de 1 tripulante, a canoa
;; 2 e a arca 3.
;;
;; assim:
;; x + y + z <= 10
;; x + 2y + 3z <= 18
;;
;; Modelagem
;;
;; Serão necessarios 3 genes do tipo inteiro.
;; Cada individuo deve obedecer as restrições.
;; 

;; função de avaliação
(defn f
  [x y z]
  (apply + [(* 50 x) (* 70 y) (* 100 z)]))

(defn new_individual
  []
  {"x" (rand-int 18)
   "y" (rand-int 9)
   "z" (rand-int 6)})

(defn is_possible
  [individual]
  (and (= (+ (individual "x")(individual "y")(individual "z") ) 10) 
       (= (+ (individual "x") (*(individual "y") 2))(*(individual "z") 3) 18)))

(defn generate_individual
  []
  (loop [individual (new_individual)]
    (if-not(is_possible individual)
      (recur (new_individual)))))

(defn generate_population
  []
  ((def my-population [])
    (for [x (range 100)]
      (println (generate_individual)))))

(def population (generate_population))

