#!/usr/local/bin/guile \
--no-auto-compile -e main -s
!#

;; Creator: nik gaffney <nik@fo.am>
;; Created: 2023-10-23
;; Copyright ©️ 2023 FoAM oü
;; SPDX-License-Identifier: GPL-3.0-or-later

(define pandoc "pandoc")
(define template  "invoice-template.tex")
(define pdf-engine "xelatex")

;; compose & execute suitable pandoc command
(define (run-pandoc file)
  (let* ((output-file (basename file ".yaml"))
         (status (system
                  (format #f "~a '~a' -o '~a.pdf' --template='~a' --pdf-engine=~a --quiet"
                          pandoc file output-file template pdf-engine))))
    (if (eq? status 0)
        (display (format #f "successfully generated ~a.pdf\n" output-file))
        (display (format #f "error generating ~a.pdf\n" output-file)))))

(define (main args)
  (if (eq? (length args) 2)
      (run-pandoc (list-ref args 1))
      (display (format #f "usage: ~a <filename.yaml>\n" (car args)))))
