
#BY USING INBUILT FUNCTION
# loading gc
import gc
# get the current collection
# thresholds as a tuple
print("Garbage collection thresholds:",
      gc.get_threshold())

#BY FINDING MANUALLY
# Importing gc module
import gc

# Returns the number of
# objects it has collected
# and deallocated
collected = gc.collect()

# Prints Garbage collector
# as 0 object
print("Garbage collector: collected",
      "%d objects." % collected)