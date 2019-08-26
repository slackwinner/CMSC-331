#lang racket
( define course-list (cons '("Dept" "Number" "Section" "Class Nbr" "Capacity" "Enrollment")
                             '(("CMSC" "201" "1" "1052" 100 30)
                             ("CMSC" "341" "6" "7447" 40 27)
                             ("CMSC" "341" "3" "7443" "40" 29)
                             ("CMSC" "331" "5" "7746" 40 36)
                             ("CMSC" "331" "6" "7747" 40 "40")
                             ("CMSC" "471" "3" "8196" 40 31))
                             
                      )
)

#|
define a function as (open-seats section)
section is a member of course-list
in this function we calculate the available seats by deducting Enrollement from Capacity
and we prepare a string to be printed to the standard output in the following form:
CMSC341 (Section 6) => 13
|#

(define (open-seats section)

  ; Variable Declaration
  (define cap (fifth section))
  (define enroll (sixth section))

  ; Calculates avaliable seats 
  (define remaining (- cap enroll))

  ; Builds the string output before outputting the results
  (string-append (first section) (second section) " (Section " (third section) ") => " (number->string remaining))
  
)

#|
define a function as (report-open-seats course-list)
In this function we iterate through course-list
for every course record we need to check whether both Enrollment and Capacity are numbers
If both are numbers then we call the function (open-seats ...) on the course record
if any of them is not a number we just ignore the record
and we print the returned string to the standard output
the result for every record should be printed on a new line
|#

(define (report-open-seats list-of-courses)
  (for ([i (in-list course-list)])
    
    ; Variable Declarations
    (define cap (fifth i))
    (define enroll (sixth i))

    (define capValid -1)
    (define enrollValid -1)
    (define inputValid -1)

    ; Determines if capacity value is an int
    (cond
         [(number? cap) (set! capValid 1)]
         [else (set! capValid 0)]
         
    )

    ; Determines if enrollment value is an int
    (cond
         [(number? enroll) (set! enrollValid 1)]
         [else (set! enrollValid 0)]
         
    )

    ; Determines if both cap and enroll values are valid inputs prior to execution
    (if( = capValid 1) (if( = enrollValid 1) (set! inputValid 1) (set! inputValid 0)) (set! inputValid 0))

    ; Calls the open-seats function
    (cond
         [(equal? inputValid 1) (displayln(open-seats i))]

    )
   )
  )
    
; leave the following function call intact
(report-open-seats course-list)
