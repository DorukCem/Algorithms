def topdown_fib_dp(num):
   if num <= 1:
      return num
   
   dp = [None] * (num+1)
   dp[0] = 0
   dp[1] = 1

   def fib(num):
      if dp[num] == None:
         dp[num] = fib(num-1)+fib(num-2)

      return dp[num]
   
   return fib(num)

def bottomup_fib_dp(num):
   if num <= 1:
      return num
   
   dp = [None] * (num+1)
   dp[0] = 0
   dp[1] = 1
   for i in range(2, num+1):
      dp[i] = dp[i-2] + dp[i-1]
   
   return dp[num]

def fib_best(num):
   if num == 0:
      return 0
   
   a = 0
   b = 1

   for _ in range(2, num):
      sum_ab = a+b
      a = b
      b = sum_ab
   
   return a+b

for i in range(8):
   print(topdown_fib_dp(i))

print("----------")

for i in range(8):
   print(bottomup_fib_dp(i))

print("----------")

for i in range(8):
   print(fib_best(i))