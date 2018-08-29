from pyspark import SparkContext

def matrix_vector(matrix, vector):
    A = matrix.map(lambda l: [float(i) for i in l.split(',')])
    v = vector.map(lambda l: [float(i) for i in l.split(',')])

    A1 = A.zipWithIndex()
    A2 = A1.map(lambda l: (l[1], [(col, item) for col, item in enumerate(l[0])]))
    v1 = v.zipWithIndex()
    v2 = v1.map(lambda l: (l[1], l[0]))

    A3 = A2.flatMapValues(lambda l: [i for i in l]).map(lambda l: (l[1][0], (l[0], l[1][1])))
    v3 = v2.flatMapValues(lambda l: [i for i in l])

    Av = A3.join(v3)
    Av1 = Av.map(lambda l: (l[1][0][0], l[1][0][1] * l[1][1]))
    Av2 = Av1.reduceByKey(lambda n1, n2: n1 + n2)

    return Av2.collect()

if __name__ == '__main__':
    sc = SparkContext('local[1]', 'feiji')
    matrix = sc.textFile('/Users/sunduo/Downloads/ORIE5270/A.txt')
    vector = sc.textFile('/Users/sunduo/Downloads/ORIE5270/v.txt')
    answer = matrix_vector(matrix, vector)
    print(answer)

