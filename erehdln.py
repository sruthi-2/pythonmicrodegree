try:
    f=open('textfi.txt')
    print("works")
    a=p
except Exception:
    print("sorrry for incovinience,SMTG WENT WRONG,Were working on it")
# we get error for a=p also
# u can be specific by doin following
try:
    f=open('textfi.txt')
    print("works")
    a=p
except FileNotFoundError:
    print("sorrry for incovinience,SMTG WENT WRONG,Were working on it")
except Exception:
    print("general error")
#
#
#
try:
    f=open('textfi.txt')
    print("works")
    #a=p
    #user defined expectipns
    if f.name=="textfi.txt":
        #raise Exception
        raise TypeError("this is textfi file")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("general error",e)
else: #if the try stmt works completely
    print(f.read())
    f.close()
finally:
    print("this is finally statement")
    print("databases have been closed")