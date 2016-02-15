;; Loading lisp files in emacs 
;; Not as easy as it seems

;; Load a file. Note the .el extension!
(load-file "~/some-file.el")

;; Slightlt better:
;; Add file to your loadpath
;; Note that packages installed via package manager will be automatically added to the load-path!!
;; A directory can be added like this. This will only add the root level. For recursive adding, and other 
;; nice things related to the load-path, see this: https://www.emacswiki.org/emacs/LoadPath
(add-to-list 'load-path "~/.emacs.d/elisp/")

;; After adding to the load path, you can use 
(load-library "pytest")
;; Or 
(require 'pytest)

;; difference is that the require requires that the files 'provides'  the package (provide 'pytest)

;; For more info on loading emacs files, including a nice funtion to work with an context, se
;; https://www.emacswiki.org/emacs/LoadingLispFiles
