temp= {
    '월':25.5,
    '화':28.3,
    '수':33.2,
    '목':32.1,
    '금':30.5,
    '토':33.3,
    '일':29.3
    }
print("주간 최고 기온:", temp)

def min_temp(temp_dict):
    return min(temp_dict.values())
print("가장 낮은 최고 기온: ",min_temp(temp))

def max_temp(temp_dict):
    result=[]
    for i in temp_dict.values():
        if i >= 30:
            result.append(temp.key())
    print(result)