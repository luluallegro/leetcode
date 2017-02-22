'''
#  ======================================================================
#     FileName: isPowerOfThree.py
#      Project: Leetcode
#       Author: Yong Yang, Department of Mathematics, UTA
#        Email: yongyang@uta.edu; yongyang.math@gmail.com
#      Created: 2017-02-22 11:15:36
#   LastChange: 2017-02-22 11:16:17
#  ======================================================================
'''
def isPowerOfThree(self, n):
        """
        Given an integer, write a function to determine if it is a power of three.
        :type n: int
        :rtype: bool
        """
        return n>0 and 1162261467%n==0
