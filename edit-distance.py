class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1=len(word1)
        length2=len(word2)
        nump=[(length1+1)*[0] for i in range(length2+1)]
        for i in range(length1+1):
            nump[0][i]=i
        for i in range(length2+1):
            nump[i][0]=i
        for i in range(1,length2+1):
            for j in range(1,length1+1):
                if word1[j-1] == word2[i-1]:
                    nump[i][j] = nump[i-1][j-1]
                else:
                    nump[i][j]=min(nump[i-1][j-1],nump[i-1][j],nump[i][j-1])+1
        """
        (一)、当word1[i]==word2[j]时,由于遍历到了i和j,说明word1的0~i-1和word2的0~j-1的匹配结果已经生成,
由于当前两个字符相同,因此无需做任何操作,dp[i][j]=dp[i-1][j-1]
(二)、当word1[i]!=word2[j]时,可以进行的操作有3个:
      ① 替换操作:可能word1的0~i-1位置与word2的0~j-1位置的字符都相同,
           只是当前位置的字符不匹配,进行替换操作后两者变得相同,
           所以此时dp[i][j]=dp[i-1][j-1]+1(这个加1代表执行替换操作)
      ②删除操作:若此时word1的0~i-1位置与word2的0~j位置已经匹配了,
         此时多出了word1的i位置字符,应把它删除掉,才能使此时word1的0~i(这个i是执行了删除操作后新的i)
         和word2的0~j位置匹配,因此此时dp[i][j]=dp[i-1][j]+1(这个加1代表执行删除操作)
      ③插入操作:若此时word1的0~i位置只是和word2的0~j-1位置匹配,
          此时只需要在原来的i位置后面插入一个和word2的j位置相同的字符使得
          此时的word1的0~i(这个i是执行了插入操作后新的i)和word2的0~j匹配得上,
          所以此时dp[i][j]=dp[i][j-1]+1(这个加1代表执行插入操作)
      ④由于题目所要求的是要最少的操作数:所以当word1[i] != word2[j] 时,
          需要在这三个操作中选取一个最小的值赋格当前的dp[i][j]
        """
        return nump[length2][length1]
