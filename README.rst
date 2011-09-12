Spotify Puzzles
===============

Best Before Puzzle 
------------------

http://www.spotify.com/us/jobs/tech/best-before/

Correct
~~~~~~~

::

    $ python bestbefore.py 
    2001/01/03
    2001-01-03
    
    $ python bestbefore.py 
    2001/03/01
    2001-01-03
    
    $ python bestbefore.py 
    03/01/01
    2001-01-03
    
    $ python bestbefore.py 
    03/01/112
    2112-01-03
    
    $ python bestbefore.py 
    12/11/10
    2010-11-12
    
    $ python bestbefore.py 
    10/11/12
    2010-11-12
    
    $ python bestbefore.py 
    11/12/10
    2010-11-12
    
    $ python bestbefore.py 
    11/30/999
    2999-11-30
    
    $ python bestbefore.py 
    11/32/1
    2032-01-11


Errors
~~~~~~

::

    $ python bestbefore.py 
    11/31/2001
    11/31/2001 is illegal
    
    $ python bestbefore.py 
    11/31/
    11/31/ is illegal

TODOs
~~~~~

This does not work, and it should!
Reason: datetime.date() does not allow 0's.

::

    $ python bestbefore.py 
    1/1/0
    1/1/0 is illegal

    $ python bestbefore.py 
    1/1/00
    1/1/00 is illegal

    $ python bestbefore.py 
    1/1/000
    1/1/000 is illegal

