#| 
Tile Coding Software version 3.0
by Rich Sutton
based on a program created by Steph Schaeffer and others
External documentation and recommendations on the use of this code is available in the 
reinforcement learning textbook by Sutton and Barto, and on the web.
These need to be understood before this code is.

This is an implementation of grid-style tile codings, based originally on
the UNH CMAC code (see http://www.ece.unh.edu/robots/cmac.htm), but by now highly changed. 
Here we provide a function, "tiles", that maps floating and integer
variables to a list of tiles, and a second function "tiles-wrap" that does the same while
wrapping some floats to provided widths (the lower wrap value is always 0).

The float variables are gridded at unit intervals, so generalization
will be by approximately 1 in each direction, and any scaling will have 
to be done externally before calling tiles.

Num-tilings should be a power of 2, e.g., 16. To make the offsetting work properly, it should
also be greater than or equal to four times the number of floats.

The first argument is either an index hash table of a given size (created by (make-iht size)), 
an integer "size" (range of the indices from 0), or nil (for testing, indicating that the tile 
coordinates are to be returned without being converted to indices).

Tests:
(q (loop for ti in (tiles nil 8 '(1.2 26.5 4.6) '(100 101)) do (print ti)))
(q (loop for ti in (tiles-wrap nil 8 '(1.2 26.5 4.6) '(100 101) nil '(2 nil 5)) do (print ti)))
(setq iht (make-iht 4096))
(tiles iht 16 '(1.2 25.7 4.5) '(1 2 3))
(time (loop repeat 100000 do (tiles 4096 16 '(1.2 25.7 4.5) '(1 2 3))))
(graph (loop with num-tiles = 8 with m = 4096 
             with tiles1 = (tiles m num-tiles '(5.5)) 
             for x from -2 to 14 by 0.01  
             collect (list x (length (intersection tiles1 (tiles m num-tiles (list x)))))))
(graph (loop with num-tiles = 8 with m = iht 
             with tiles1 = (tiles-wrap m num-tiles '(5.5) '(6)) 
             for x from -2 to 14 by 0.01  
             collect (list x (length (intersection tiles1 (tiles-wrap m num-tiles (list x) '(6)))))))
(loop for x = (random 10.0) for y = (random 10.0) do (tiles 4096 16 (list x y)))
|#

(defun tiles (iht-or-size num-tilings floats &optional ints)
  "returns num-tilings tile indices corresponding to the floats and ints"
  (let* ((qfloats (loop for f in floats collect (floor (* f num-tilings)))))
    (loop for tiling below num-tilings 
          for tiling*2 = (* tiling 2) 
          collect (hash-coords 
                   (cons tiling 
                         (nconc (loop for q in qfloats 
                                      for b from tiling by tiling*2
                                      collect (floor (+ q b) num-tilings))
                                ints))
                   iht-or-size))))

(defun tiles-wrap (iht-or-size num-tilings floats wrap-widths &optional ints)
  "returns num-tilings tile indices corresponding to the floats and ints, wrapping some floats"
  (let* ((qfloats (loop for f in floats collect (floor (* f num-tilings)))))
    (loop for tiling below num-tilings 
          for tiling*2 = (* tiling 2) 
          collect (hash-coords 
                   (cons tiling 
                         (nconc (loop for q in qfloats 
                                      for b from tiling by tiling*2
                                      for c = (floor (+ q (mod b num-tilings)) num-tilings)
                                      for width in wrap-widths
                                      collect (if width (mod c width) c))
                                ints))
                   iht-or-size))))

(defun hash-coords (coordinates iht-or-size)
  (etypecase iht-or-size
    (iht (iht-hash coordinates iht-or-size))
    (integer (mod (hash-unh coordinates) iht-or-size))
    (null coordinates))) ;for testing

(defParameter random-table 
  (make-array 2048 :initial-contents (loop repeat 2048 collect (random (floor most-positive-fixnum 256)))))

(defun hash-unh (ints &optional (increment 449))
  "a hashing ints using random table"
  (loop for i from 0
        for int in ints
        sum (aref random-table (mod (+ int (* increment i)) 2048))))

;--------------------Index hash tables-------------------

;An iht hashes objects to an index (positive integer less than the iht's size).
;Previously seen objects get that object's index. New objects get the next unseen index. 
;If the iht is full then we get a random (hashed) index from those previously seen. 

(defstruct (iht (:constructor make-iht (size)))
  size
  (count 0)
  (overfull-count 0)
  (hash-table (make-hash-table :test #'equal :rehash-threshold 1)))

(defun iht-fullp (iht)
  (with-slots (size count) iht
    (>= count size)))

(defun iht-hash (object iht)
  (let* ((ht (iht-hash-table iht))
         (index (gethash object ht)))
    (cond (index index)
          ((iht-fullp iht) 
           (when (= 0 (iht-overfull-count iht)) (print "index hash table full, starting to allow collisions"))
           (incf (iht-overfull-count iht))
           (mod (hash-unh object) (iht-size iht)))
          (t (with-slots (count) iht
               (prog1 (setf (gethash object ht) count)
                 (incf count)))))))