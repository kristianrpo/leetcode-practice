/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    if(trust.length===0){
        if (n>1){
            return -1
        }
        else{
            return n
        }
    }
    let objectTrusted = {}
    for(let i = 1; i<=n;i++){
        objectTrusted[i] = [0,[]]
    }
    for(let i=0; i<trust.length;i++){
        objectTrusted[trust[i][1]][0]++; // cantidad de votos para la persona index 0
        objectTrusted[trust[i][0]][1].push(trust[i][1]) // a quien votaron ellos index 1
    }
    let max = [0,0] // index 0: cantidad de votos, index1: persona
    for(let element in objectTrusted){
        if(objectTrusted[element][0]>max[0]){
            max = [objectTrusted[element][0],element]
        }
    }

    if(objectTrusted[max[1]][1].length>0){
        return -1
    }
    console.log(max[1])
    console.log(objectTrusted)
    for(let element in objectTrusted){
        if(element!=max[1]){
            if(objectTrusted[element][1].length==0){return -1}
            let flag = objectTrusted[element][1].some(arrayElements => !arrayElements==max[1])
            if(flag){
                return -1
            }
        }
    }

        return max[1]


};