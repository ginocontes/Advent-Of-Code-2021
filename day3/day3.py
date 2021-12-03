import math

def parse_file(file_name):
    with open(file_name) as f:
        l = list(map(lambda x: x.rstrip(), f.readlines()))
    return l


def gamma_rate(bit_list):
    res = ''
    n = len(bit_list[0])
    for i in range(n):
        s = sum([int(x[i]) for x in bit_list])
        if s > len(bit_list)//2:
            res += '1'
        else:
            res += '0'
    return res

def complement(bits):
    res  = ''
    for bit in bits:
        if bit == '0':
            res += '1'
        else:
            res += '0'
    return res

def epsilon_rate(bit_list):
    return complement(gamma_rate(bit_list))

def submarine_power_consumption(bit_list):
    return int(gamma_rate(bit_list),2) * int(epsilon_rate(bit_list), 2)


def lists_with_most_common_value(bit_list, i, criteria='oxygen'):
    s = sum([ int(x[i]) for x in bit_list])
    if criteria == 'oxygen':
        if len(bit_list) == 2:
            if(s>=1):
                most_common_value = '1'
            else:
                most_common_value = '0'
        else:
            most_common_value = '1' if s >= math.floor(len(bit_list)//2)+1 else '0'
        return list(filter(lambda x: x[i] == most_common_value, bit_list))
    else:
        if len(bit_list) == 2:
            if(s>=1):
                least_common_value = '0'
            else:
                least_common_value = '1'
        else:
            least_common_value = '0' if s >= math.floor(len(bit_list)//2)+1 else '1'
        return list(filter(lambda x: x[i] == least_common_value, bit_list))


def oxygen_generator_rating(bit_list):
    n = len(bit_list[0])
    for i in range(n):
        bit_list = lists_with_most_common_value(bit_list, i, criteria='oxygen')
        if(len(bit_list)==1):
            return bit_list[0]
    return bit_list


def c02_scrabber(bit_list):
    n = len(bit_list[0])
    for i in range(n):
        bit_list = lists_with_most_common_value(bit_list, i, criteria='c02')
        if(len(bit_list)==1):
            return bit_list[0]
    return bit_list


def submarine_life_support_rating(bit_list):
    return int(oxygen_generator_rating(bit_list),2) * int(c02_scrabber(bit_list),2)


if __name__ == "__main__":
    # bit_list = parse_file('input1.txt')
    # print(submarine_power_consumption(bit_list))
    bit_list = parse_file('input2.txt')
    bit_list = "00100 11110 10110 10111 10101 01111 00111 11100 10000 11001 00010 01010".split(" ")
    # print(oxygen_generator_rating(bit_list))
    # print(c02_scrabber(bit_list))
    print(submarine_life_support_rating(bit_list))
