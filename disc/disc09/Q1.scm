(define (fit total n)
  (define (f total n k)
    (if (and (= n 0) (= total 0))
        #t
        (if (< total (* k k))
            #f
            (or (f (- total (* k k)) (- n 1) (+ k 1))
                (f total n (+ k 1))))))
  (f total n 1))

(expect (fit 10 2) #t)

(expect (fit 9 1) #t)

(expect (fit 9 2) #f)

(expect (fit 9 3) #f)

(expect (fit 25 1) #t)

(expect (fit 25 2) #t)
