'''Метод заключается в том, что создаётся новый массив данных, 
и в нём значение каждой точки высчитывается как среднее арифметическое 
предыдущих K значений из исходного набора.'''


def moving_average(timeseries, K):
    result = [] 
    current_sum = sum(timeseries[0:K])
    result.append(current_sum / K)
    for i in range(0, len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result 
