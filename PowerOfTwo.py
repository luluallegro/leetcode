'''
#  ======================================================================
#     FileName: PowerOfTwo.py
#      Project: Leetcode
#       Author: Yong Yang, Department of Mathematics, UTA
#        Email: yongyang@uta.edu; yongyang.math@gmail.com
#      Created: 2017-02-20 22:21:54
#   LastChange: 2017-02-20 22:22:21
#  ======================================================================
'''
def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        Given an integer, write a function to determine if it is a power of two.
        """
        return n>0 and not(n&n-1)
