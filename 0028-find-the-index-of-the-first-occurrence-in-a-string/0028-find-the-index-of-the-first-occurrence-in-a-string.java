class Solution {
    public int strStr(String haystack, String needle) {
        for(int i=0;i<=haystack.length()-needle.length();i++)
        {
            if(haystack.charAt(i)==needle.charAt(0))
            {
                int k=0;
                for(int j=i;j<(i+needle.length());j++)
                {
                    
                    if(haystack.charAt(j)!=needle.charAt(k))
                    {
                        break;
                    }
                    k++;
                    if(k==needle.length())
                    {
                        return i;
                    }
                    
                }
            }
        }
        return -1;
    }
}