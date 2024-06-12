/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function(arr1, arr2) {
    let objeto = {}
    let answer = []
    for (let element of arr2){
       objeto[element] = 0
    }
    for (let element of arr1){
        objeto[element]=0;
    }
    for (let element of arr1){
        objeto[element]++;
    }
    for(let i=0; i<arr2.length;i++){
        for(let j=0; j<objeto[arr2[i]]; j++){
            answer.push(arr2[i])
        }
        delete objeto[arr2[i]]
    }

    for(let element in objeto){
        for(let i = 0; i<objeto[element]; i++){
            answer.push(parseInt(element))
        }
    }
    return answer
};