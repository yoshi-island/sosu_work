# -*- coding: utf-8 -*-
# ~/.pyenv/shims/python

# prime num list
prime_num_list = [2]
# target number
n = 3

while len(prime_num_list) < 10000:
  flag = 0

  for l in prime_num_list:
#    print("l: %s" % l)
    if n % l == 0:
      flag = 1
      n += 1
      break

  if flag == 0:
    prime_num_list.append(n)
    print("len: %s, number: %s" % (len(prime_num_list),n))
#    print("prime_num_list: %s" % prime_num_list)
    n += 1
