class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    scoreOfString(s) {
        let total=0;
        for (let i=s.length-1;i>0;i--){
            total=total+Math.abs(s[i].charCodeAt(0)-s[i-1].charCodeAt(0))
        }
        return total;
    }
}
