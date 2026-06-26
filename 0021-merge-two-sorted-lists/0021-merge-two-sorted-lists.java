class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode first=list1;
        ListNode second=list2;
        ListNode list3= new ListNode();
        ListNode current=list3;
        if(first!=null || second!=null)
        {
        while(first!=null || second!=null)
        {
            if(first==null)
            {
                current.val=second.val;
                second=second.next;
            }
            else if(second==null)
            {
                current.val=first.val;
                first=first.next;
            }
            else if(first.val < second.val)
            {
                current.val=first.val;
                first=first.next;
            }
            else
            {
                current.val=second.val;
                second=second.next;
            }
            if(first!=null || second!=null)
            {
                ListNode newnode = new ListNode();
                current.next=newnode;
                current=newnode;
            }
        }
        }
        else
        {
            return null;
        }
        return list3;
    }
}