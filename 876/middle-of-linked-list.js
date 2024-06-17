/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let count = 0
    let tempHead = head
    let objectElement = []
    while(tempHead!=null){
        objectElement.push(tempHead.val)
        tempHead = tempHead.next
        count++
    }
    let position = Math.floor(count/2)
    count = 0
    while(head != null){
        if(count===position){
            return head
        }
        else{
            head = head.next
            count++
        }
    }

};