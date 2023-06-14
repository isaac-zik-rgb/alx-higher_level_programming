#!/usr/bin/node
function factorial(n){
    if (n){
	if(n === 0){
	    return 1;
	}
	else if (n > 89){
	    return('Infinity');
	}
	return n * factorial(n - 1);
    }else
	return 1;
}


console.log(factorial(Number(process.argv[2])));
