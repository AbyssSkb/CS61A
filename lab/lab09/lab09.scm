(define (over-or-under num1 num2)
  (if (= num1 num2)
      0
      (if (< num1 num2)
          -1
          1)))

(define (make-adder num)
  (lambda (inc) (+ num inc)))

(define (composed f g) (lambda (x) (f (g x))))

(define (repeat f n)
  (lambda (x)
    (if (= n 1)
        (f x)
        ((repeat f (- n 1)) (f x)))))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (if (zero? b)
      a
      (gcd b (modulo a b))))
