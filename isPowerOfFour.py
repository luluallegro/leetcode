'''
#  ======================================================================
#     FileName: isPowerOfFour.py
#      Project: Leetcode
#       Author: Yong Yang, Department of Mathematics, UTA
#        Email: yongyang@uta.edu; yongyang.math@gmail.com
#      Created: 2017-02-22 11:52:06
#   LastChange: 2017-02-22 11:52:16
#  ======================================================================
'''
def isPowerOfFour(self, num):
        """
        Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
        :type num: int
        :rtype: bool
        """
        return num>0 and not(num&(num-1)) and len(bin(num))%2==1
