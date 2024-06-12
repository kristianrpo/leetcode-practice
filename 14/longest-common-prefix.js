/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    shortestWord = findShortestWord(strs);
    let i = 0;
    let answer = ""
    while(i<shortestWord.length){
        prefixTemp = shortestWord.slice(0,i+1)
        let flag = true
        for(let word of strs){
            if (word.slice(0,i+1)===prefixTemp){
                continue
            }
            else{
                flag = false
                break;
            }
        }
        if (flag===false){
            return answer
        }
        else{
            answer=prefixTemp
        }
        i++
    }
    return answer
};

const findShortestWord = (strs) => {
    let min = 100000000;
    let shortestWord;
    for(word of strs){
        if (word.length<min){
            min = word.length
            shortestWord = word 
        }
    }
    return shortestWord
}