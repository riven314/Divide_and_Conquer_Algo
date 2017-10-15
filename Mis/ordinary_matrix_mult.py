x = [[1,2,3],[2,3,4],[8,9,7]]
y = [[3,4,5],[5,6,7],[8,10,7]]

def matrix_mult(x,y):
  r = len(x)
  w = len(x[0])
  return [[sum(list([x[i][k]*y[k][j] for k in range(w)])) for i in range(w)] for j in range(r)]
