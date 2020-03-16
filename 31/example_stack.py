def function2():
  raise RuntimeError

def function1():
  function2()

if __name__ == '__main__':
  function1()