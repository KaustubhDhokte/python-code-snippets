try:
    print 'In try!'
    #raise Exception() # does not hit else even if except Exception is commented out.
    '''
    In try!
    Inside Exception
    Inside finally
    '''
except IndexError:
    print 'Inside IndexError'
#except Exception:
#    print 'Inside Exception'
else:
    print 'Inside else'
    # Called when no exception generated in try
finally:
    print 'Inside finally'